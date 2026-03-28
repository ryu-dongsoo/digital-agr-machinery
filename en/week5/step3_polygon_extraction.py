import numpy as np
import matplotlib.pyplot as plt
import rasterio
import os

def extract_treatment_polygon(ndvi_array, threshold=0.45):
    """
    Extracts a binary mask of areas where NDVI falls below a given threshold,
    identifying zones that may require treatment (pesticide or irrigation).
    """
    print(f"Scanning for treatment-required zones (threshold: NDVI < {threshold})")
    
    # Binary segmentation: exclude bare soil (NDVI <= 0.2), flag stressed vegetation
    treatment_mask = ((ndvi_array > 0.2) & (ndvi_array < threshold)).astype(np.uint8)
    
    total_pixels = ndvi_array.size
    target_pixels = np.sum(treatment_mask)
    target_ratio = (target_pixels / total_pixels) * 100
    
    print(f"Treatment-suspected pixels: {target_pixels} px ({target_ratio:.1f}% of total)")
    
    return treatment_mask

def visualize_extraction(original_ndvi, treatment_mask):
    """Side-by-side comparison of the original NDVI map and the extracted treatment mask."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    im0 = axes[0].imshow(original_ndvi, cmap='RdYlGn', vmin=-0.1, vmax=0.9)
    axes[0].set_title("Original NDVI Map")
    fig.colorbar(im0, ax=axes[0])
    
    im1 = axes[1].imshow(treatment_mask, cmap='Reds', vmin=0, vmax=1)
    axes[1].set_title("Treatment Required Mask (Binary)")
    fig.colorbar(im1, ax=axes[1])
    
    plt.tight_layout()
    
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "step3_result.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✅ Treatment mask result image saved: {save_path}")
    
    plt.show()

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    NDVI_FILE = os.path.join(BASE_DIR, "output_ndvi.tif")
    
    if not os.path.exists(NDVI_FILE):
        print("Warning: NDVI TIF file not found. Please run step1_ndvi_calculation.py first.")
    else:
        with rasterio.open(NDVI_FILE) as src:
            real_ndvi = src.read(1)
            
        # Extract vegetation zones with NDVI < 0.45 as disease/water stress candidates
        mask = extract_treatment_polygon(real_ndvi, threshold=0.45)
        visualize_extraction(real_ndvi, mask)
