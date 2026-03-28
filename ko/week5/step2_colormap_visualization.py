import numpy as np
import matplotlib.pyplot as plt
import rasterio
import os

def visualize_ndvi_comparison(red_array, nir_array, ndvi_array):
    """
    RED 대역, NIR 대역 원본 이미지와 산출된 NDVI 맵을 3분할(Side-by-side)로
    한눈에 비교하여 식생 지수의 원리를 직관적으로 이해할 수 있도록 시각화
    """
    print("NDVI 3분할 비교 시각화 렌더링 시작...")
    
    # 1. 1x3 서브플롯 캔버스 생성
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # 2. RED 밴드 시각화 (인간의 눈에 보이는 흑백 밝기)
    # 식물이 있는 곳은 빨간빛을 많이 흡수하므로 어둡게(값이 낮게) 표시됨
    im0 = axes[0].imshow(red_array, cmap='gray')
    axes[0].set_title("1. RED Band (Visible)")
    axes[0].axis('off')
    fig.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)
    
    # 3. NIR 밴드 시각화 (식물 반사 스펙트럼)
    # 엽록소의 스펀지 조직이 적외선을 강하게 반사하므로 식물이 하얗게(값이 높게) 빛남
    im1 = axes[1].imshow(nir_array, cmap='gray')
    axes[1].set_title("2. NIR Band (Infrared)")
    axes[1].axis('off')
    fig.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)
    
    # 4. NDVI 시각화 (RED와 NIR의 수학적 조합)
    # RdYlGn (적-황-녹) 컬러맵을 통해 생육 활력도를 색상으로 투영
    im2 = axes[2].imshow(ndvi_array, cmap='RdYlGn', vmin=-0.2, vmax=0.9)
    axes[2].set_title("3. Output NDVI Health Map")
    axes[2].axis('off')
    fig.colorbar(im2, ax=axes[2], label='NDVI Value', fraction=0.046, pad=0.04)
    
    plt.tight_layout()
    # 학생 보고서 제출 로직: 화면 전시 전 자동 저장 실시
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "step2_result.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✅ 비교 시각화 이미지가 성공적으로 저장되었습니다: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RED_FILE = os.path.join(BASE_DIR, "sample_red.tif")
    NIR_FILE = os.path.join(BASE_DIR, "sample_nir.tif")
    NDVI_FILE = os.path.join(BASE_DIR, "output_ndvi.tif")
    
    if not os.path.exists(NDVI_FILE) or not os.path.exists(RED_FILE):
        print("경고: 연산된 TIF 파일들이 없습니다. step1_ndvi_calculation.py를 먼저 실행하세요.")
    else:
        # 실제 TIF 파일들에서 데이터 로딩
        with rasterio.open(RED_FILE) as src:
            real_red = src.read(1)
        with rasterio.open(NIR_FILE) as src:
            real_nir = src.read(1)
        with rasterio.open(NDVI_FILE) as src:
            real_ndvi = src.read(1)
            
        visualize_ndvi_comparison(real_red, real_nir, real_ndvi)
