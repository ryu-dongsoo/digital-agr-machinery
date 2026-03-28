import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import rasterio
import os

def create_interactive_ndvi_mask(ndvi_data):
    """
    NDVI 임계값을 슬라이더로 조절하며 방제/질병 마스크(이진화) 영역이
    실시간으로 어떻게 변하는지 직관적으로 학습하기 위한 인터랙티브 시각화 스크립트
    """
    print("인터랙티브 NDVI 슬라이더 시각화 실행 중...")

    # 초기 임계값 설정
    init_threshold = 0.45

    # 1. 캔버스 및 서브플롯 구성
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    plt.subplots_adjust(bottom=0.25) # 하단에 슬라이더 공간 확보

    # 좌측: 원본 NDVI 맵 (고정)
    im1 = ax1.imshow(ndvi_data, cmap='RdYlGn', vmin=-0.1, vmax=0.9)
    ax1.set_title("Original NDVI Health Map")
    fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)

    # 우측: 임계값 기반 이진 마스크 (초기치 적용)
    # 식물 구역(>0.2) 중에서 기준치(Threshold) 미만인 구역만 방제 대상(1)으로 추출
    mask = ((ndvi_data > 0.2) & (ndvi_data < init_threshold)).astype(np.uint8)
    
    im2 = ax2.imshow(mask, cmap='Reds', vmin=0, vmax=1)
    ax2.set_title(f"Treatment Mask (Threshold < {init_threshold:.2f})")
    
    # 2. 슬라이더 UI 축 스팬 추가
    ax_thresh = plt.axes([0.25, 0.1, 0.50, 0.03]) # [왼쪽, 아래, 너비, 높이]
    
    # 슬라이더 생성 (범위: 0.20 ~ 0.80)
    thresh_slider = Slider(
        ax=ax_thresh,
        label='NDVI Threshold',
        valmin=0.20,
        valmax=0.80,
        valinit=init_threshold,
        color='maroon'
    )

    # 3. 이벤트 업데이트 콜백 함수
    def update(val):
        """
        슬라이더 값이 변할 때마다 호출되어 마스크 화면을 다시 그림
        """
        current_threshold = thresh_slider.val
        # 새로운 임계값으로 마스크 재연산
        new_mask = ((ndvi_data > 0.2) & (ndvi_data < current_threshold)).astype(np.uint8)
        
        # 우측 이미지 데이터 업데이트
        im2.set_data(new_mask)
        ax2.set_title(f"Treatment Mask (Threshold < {current_threshold:.2f})")
        
        # 캔버스 갱신
        fig.canvas.draw_idle()

    # 슬라이더 변경 이벤트에 콜백 바인딩
    thresh_slider.on_changed(update)

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "step4_result.png")
    plt.savefig(save_path, dpi=300)
    print(f"✅ 인터랙티브 시각화 초기 상태 이미지가 저장되었습니다: {save_path}")

    print("화면 하단의 슬라이더를 마우스로 조작해 보세요.")
    plt.show()

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    NDVI_FILE = os.path.join(BASE_DIR, "output_ndvi.tif")
    
    if not os.path.exists(NDVI_FILE):
        print("경고: 연산된 NDVI TIF 파일이 없습니다. step1_ndvi_calculation.py를 먼저 실행하세요.")
    else:
        with rasterio.open(NDVI_FILE) as src:
            real_ndvi = src.read(1)
            
        create_interactive_ndvi_mask(real_ndvi)
