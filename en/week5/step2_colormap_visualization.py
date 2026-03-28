import numpy as np
import matplotlib.pyplot as plt
import rasterio
import os

def visualize_ndvi_comparison(red_array, nir_array, ndvi_array):
    """
    Displays RED band, NIR band, and computed NDVI map in a side-by-side
    3-panel layout for intuitive understanding of vegetation index principles.
    """
    print("Rendering 3-panel NDVI comparison visualization...")
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # RED band: vegetation absorbs red light → appears dark
    im0 = axes[0].imshow(red_array, cmap='gray')
    axes[0].set_title("1. RED Band (Visible)")
    axes[0].axis('off')
    fig.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)
    
    # NIR band: chlorophyll spongy tissue reflects infrared → vegetation appears bright
    im1 = axes[1].imshow(nir_array, cmap='gray')
    axes[1].set_title("2. NIR Band (Infrared)")
    axes[1].axis('off')
    fig.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)
    
    # NDVI map: RdYlGn colormap projects crop vitality as color gradient
    im2 = axes[2].imshow(ndvi_array, cmap='RdYlGn', vmin=-0.2, vmax=0.9)
    axes[2].set_title("3. Output NDVI Health Map")
    axes[2].axis('off')
    fig.colorbar(im2, ax=axes[2], label='NDVI Value', fraction=0.046, pad=0.04)
    
    plt.tight_layout()
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "step2_result.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✅ Comparison visualization saved: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RED_FILE = os.path.join(BASE_DIR, "sample_red.tif")
    NIR_FILE = os.path.join(BASE_DIR, "sample_nir.tif")
    NDVI_FILE = os.path.join(BASE_DIR, "output_ndvi.tif")
    
    if not os.path.exists(NDVI_FILE) or not os.path.exists(RED_FILE):
        print("Warning: TIF files not found. Please run step1_ndvi_calculation.py first.")
    else:
        with rasterio.open(RED_FILE) as src:
            real_red = src.read(1)
        with rasterio.open(NIR_FILE) as src:
            real_nir = src.read(1)
        with rasterio.open(NDVI_FILE) as src:
            real_ndvi = src.read(1)
            
        visualize_ndvi_comparison(real_red, real_nir, real_ndvi)
