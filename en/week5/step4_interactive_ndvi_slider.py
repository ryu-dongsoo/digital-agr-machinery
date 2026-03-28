import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import rasterio
import os

def create_interactive_ndvi_mask(ndvi_data):
    """
    Interactive visualization that allows real-time NDVI threshold adjustment
    via slider, showing how treatment mask boundaries change dynamically.
    """
    print("Launching interactive NDVI slider visualization...")

    init_threshold = 0.45

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    plt.subplots_adjust(bottom=0.25)

    # Left: Original NDVI map (fixed)
    im1 = ax1.imshow(ndvi_data, cmap='RdYlGn', vmin=-0.1, vmax=0.9)
    ax1.set_title("Original NDVI Health Map")
    fig.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)

    # Right: Binary mask based on threshold
    mask = ((ndvi_data > 0.2) & (ndvi_data < init_threshold)).astype(np.uint8)
    
    im2 = ax2.imshow(mask, cmap='Reds', vmin=0, vmax=1)
    ax2.set_title(f"Treatment Mask (Threshold < {init_threshold:.2f})")
    
    # Slider UI
    ax_thresh = plt.axes([0.25, 0.1, 0.50, 0.03])
    
    thresh_slider = Slider(
        ax=ax_thresh,
        label='NDVI Threshold',
        valmin=0.20,
        valmax=0.80,
        valinit=init_threshold,
        color='maroon'
    )

    def update(val):
        """Callback: recompute mask when slider value changes."""
        current_threshold = thresh_slider.val
        new_mask = ((ndvi_data > 0.2) & (ndvi_data < current_threshold)).astype(np.uint8)
        
        im2.set_data(new_mask)
        ax2.set_title(f"Treatment Mask (Threshold < {current_threshold:.2f})")
        fig.canvas.draw_idle()

    thresh_slider.on_changed(update)

    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "step4_result.png")
    plt.savefig(save_path, dpi=300)
    print(f"✅ Interactive visualization initial state saved: {save_path}")

    print("Drag the slider at the bottom to adjust the threshold interactively.")
    plt.show()

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    NDVI_FILE = os.path.join(BASE_DIR, "output_ndvi.tif")
    
    if not os.path.exists(NDVI_FILE):
        print("Warning: NDVI TIF file not found. Please run step1_ndvi_calculation.py first.")
    else:
        with rasterio.open(NDVI_FILE) as src:
            real_ndvi = src.read(1)
            
        create_interactive_ndvi_mask(real_ndvi)
