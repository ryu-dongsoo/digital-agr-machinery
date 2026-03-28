import numpy as np
import rasterio
from rasterio.transform import from_origin
import os
import urllib.request
import io
import matplotlib.pyplot as plt

def create_realistic_field_from_satellite(red_path, nir_path, rgb_path):
    """
    QGIS 환경과 동일하게, 오픈소스 고해상도 위성 영상 타일(ArcGIS World Imagery)을
    실시간으로 다운로드한 뒤 영상 처리를 통해 RED, NIR 다중분광 데이터를 시뮬레이션합니다.
    (학생들의 명확한 이해를 위해 작물 열과 토양이 뚜렷하게 구별되는 캘리포니아 포도 농장 타일 사용)
    """
    print("고해상도 위성 영상(Satellite Tile) 기반 다중분광 데이터셋 생성 중...")
    
    # 1. 뚜렷한 농경지(포도원) 구조가 보이는 고해상도 타일 URL (Zoom 18)
    url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/18/100659/41953"
    
    try:
        req = urllib.request.urlopen(url)
        img = plt.imread(io.BytesIO(req.read()), format='jpg')
    except Exception as e:
        print(f"위성 영상 다운로드 실패: {e}")
        # 실패 시 대비용 그라데이션 배열
        shape = (256, 256)
        img = np.random.uniform(0.1, 0.4, (*shape, 3)).astype(np.float32)
        
    shape = img.shape[:2]
    img_float = img.astype(np.float32) / 255.0
    
    # 원본 RGB 이미지(학생 시각적 확인용) 별도 저장
    plt.imsave(rgb_path, np.clip(img_float, 0, 1))
    
    R = img_float[:, :, 0]
    G = img_float[:, :, 1]
    
    # 2. 광학 센서의 파장대별 반사 특성 시뮬레이션
    # 식생 구역(포도나무 열)은 초록색(G)이 높으므로, NDVI 대비가 극명해지도록 NIR을 대폭 증폭
    red = R
    nir = R + np.maximum(G - R, 0) * 4.0  # 명확한 구분을 위해 증폭률 상향
    
    # 사진의 자연스러운 느낌을 살리되 극선명한 NDVI 분포가 나오도록 클리핑
    nir = np.clip(nir, 0.01, 1.0).astype(np.float32)
    red = np.clip(red, 0.01, 1.0).astype(np.float32)
    
    # 3. Rasterio 공간정보(GeoTIFF) 매핑
    transform = from_origin(126.852, 35.786, 0.0001, 0.0001)
    meta = {
        'driver': 'GTiff',
        'height': shape[0],
        'width': shape[1],
        'count': 1,
        'dtype': 'float32',
        'crs': '+proj=latlong',
        'transform': transform
    }

    with rasterio.open(red_path, 'w', **meta) as dst:
        dst.write(red, 1)
    with rasterio.open(nir_path, 'w', **meta) as dst:
        dst.write(nir, 1)
    
    print(f"✅ 실제 위성 영상 기반 데이터 저장 완료: {red_path}, {nir_path}, {rgb_path}")
    return red, nir, shape

def calculate_ndvi(red_path, nir_path, rgb_path, output_path):
    """
    RED와 NIR 밴드 TIF 파일을 읽어 NDVI 연산을 수행하고 변환 과정을 화면에 표시합니다.
    """
    # 1. 파일 경로 확인 방어 로직
    if not os.path.exists(red_path) or not os.path.exists(nir_path) or not os.path.exists(rgb_path):
        create_realistic_field_from_satellite(red_path, nir_path, rgb_path)

    print(f"[{red_path}] 및 [{nir_path}] 로딩 중...")

    # 2. Rasterio 밴드 데이터 로드 (Float32 변환)
    with rasterio.open(red_path) as src_red:
        red = src_red.read(1).astype('float32')
        meta = src_red.meta

    with rasterio.open(nir_path) as src_nir:
        nir = src_nir.read(1).astype('float32')

    # 3. NDVI 연산 전 전처리 (분모 합산)
    print("NDVI 연산 시작...")
    bottom = (nir + red)
    
    # 분모가 0인 경우 경고 회피 -> 해당 픽셀 0으로 처리, 식이 (NIR - RED) / (NIR + RED)
    ndvi = np.where(bottom == 0, 0, (nir - red) / bottom)

    # 4. 결과 저장 준비 (데이터 타입 Float32 지정)
    meta.update(dtype=rasterio.float32, count=1)

    with rasterio.open(output_path, 'w', **meta) as dst:
        dst.write(ndvi, 1)

    print(f"✅ NDVI 산출 완료. 저장 경로: {output_path}")
    print(f"[검증 통계] Min: {np.nanmin(ndvi):.3f}, Max: {np.nanmax(ndvi):.3f}")

    # 5. 원본 이미지와 NDVI 결과 동시 비교 시각화 (학생 확인용)
    print("원본 위성 영상과 산출된 NDVI 맵을 비교 출력합니다...")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 원본 RGB 이미지 로딩
    rgb_img = plt.imread(rgb_path)
    axes[0].imshow(rgb_img)
    axes[0].set_title("Original Satellite View (RGB)")
    axes[0].axis('off')
    
    # 계산된 NDVI 출력
    im1 = axes[1].imshow(ndvi, cmap='RdYlGn', vmin=-0.1, vmax=0.9)
    axes[1].set_title("Calculated NDVI Map")
    axes[1].axis('off')
    fig.colorbar(im1, ax=axes[1], label="NDVI Value")
    
    plt.tight_layout()
    
    # 자동 이미지 저장
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step1_result.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✅ 결과 비교 이미지가 저장되었습니다: {save_path}")
    
    plt.show()

    return ndvi

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RED_FILE = os.path.join(BASE_DIR, "sample_red.tif")
    NIR_FILE = os.path.join(BASE_DIR, "sample_nir.tif")
    RGB_FILE = os.path.join(BASE_DIR, "sample_rgb.jpg")
    OUTPUT_FILE = os.path.join(BASE_DIR, "output_ndvi.tif")
    
    calculate_ndvi(RED_FILE, NIR_FILE, RGB_FILE, OUTPUT_FILE)
