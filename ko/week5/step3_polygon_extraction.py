import numpy as np
import matplotlib.pyplot as plt
import rasterio
import os

def extract_treatment_polygon(ndvi_array, threshold=0.45):
    """
    NDVI 배열에서 식생 건강이 지정된 임계값(Threshold) 이하인 떨어지는 영역을
    마스킹(Masking)하여 방제(Treatment) 필요 구역 이진 맵으로 추출
    """
    print(f"방제 의심 구역 탐색 시작 (임계값: NDVI < {threshold})")
    
    # 이진 분할 (토양 배경 0.2 이하 제외, 식생 중에서 건강이 나쁜 구역만 추출)
    # NDVI가 0.2보다 크고(식물이고) 임계값보다 작은 경우 방제 대상(1)으로 마크
    treatment_mask = ((ndvi_array > 0.2) & (ndvi_array < threshold)).astype(np.uint8)
    
    # 추출 면적 비율(픽셀 수) 계산
    total_pixels = ndvi_array.size
    target_pixels = np.sum(treatment_mask)
    target_ratio = (target_pixels / total_pixels) * 100
    
    print(f"방제 필요 의심 구역 픽셀: {target_pixels} px (전체 대비 {target_ratio:.1f}%)")
    
    return treatment_mask

def visualize_extraction(original_ndvi, treatment_mask):
    """원래 NDVI 맵과 분할된 마스크 맵을 나란히 비교 시각화"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 원본
    im0 = axes[0].imshow(original_ndvi, cmap='RdYlGn', vmin=-0.1, vmax=0.9)
    axes[0].set_title("Original NDVI Map")
    fig.colorbar(im0, ax=axes[0])
    
    # 마스킹 결과
    # 의심 구역(1)은 붉은색, 정상 구역(0)은 흰색 계열 투영
    im1 = axes[1].imshow(treatment_mask, cmap='Reds', vmin=0, vmax=1)
    axes[1].set_title("Treatment Required Mask (Binary)")
    fig.colorbar(im1, ax=axes[1])
    
    plt.tight_layout()
    
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "step3_result.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✅ 방제 의심 구역 마스크 결과 이미지가 저장되었습니다: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    NDVI_FILE = os.path.join(BASE_DIR, "output_ndvi.tif")
    
    if not os.path.exists(NDVI_FILE):
        print("경고: 연산된 NDVI TIF 파일이 없습니다. step1_ndvi_calculation.py를 먼저 실행하세요.")
    else:
        with rasterio.open(NDVI_FILE) as src:
            real_ndvi = src.read(1)
            
        # 0.45 미만인 식생을 병해/수분부족 스트레스 구역으로 판단하여 추출
        mask = extract_treatment_polygon(real_ndvi, threshold=0.45)
        visualize_extraction(real_ndvi, mask)
