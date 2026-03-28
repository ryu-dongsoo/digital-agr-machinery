import numpy as np
import rasterio
from rasterio.transform import from_origin
import os
import urllib.request
import io
import matplotlib.pyplot as plt

def create_realistic_field_from_satellite(red_path, nir_path, rgb_path):
    """
    Downloads a high-resolution satellite tile (ArcGIS World Imagery) in real time,
    then simulates RED and NIR multispectral band data through image processing.
    (Uses a California vineyard tile where crop rows and soil are clearly distinguishable)
    """
    print("Generating multispectral dataset from high-resolution satellite tile...")
    
    # 1. High-resolution tile URL showing clear vineyard structure (Zoom 18)
    url = "https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/18/100659/41953"
    
    try:
        req = urllib.request.urlopen(url)
        img = plt.imread(io.BytesIO(req.read()), format='jpg')
    except Exception as e:
        print(f"Satellite image download failed: {e}")
        # Fallback gradient array
        shape = (256, 256)
        img = np.random.uniform(0.1, 0.4, (*shape, 3)).astype(np.float32)
        
    shape = img.shape[:2]
    img_float = img.astype(np.float32) / 255.0
    
    # Save original RGB image for visual comparison
    plt.imsave(rgb_path, np.clip(img_float, 0, 1))
    
    R = img_float[:, :, 0]
    G = img_float[:, :, 1]
    
    # 2. Simulate spectral reflectance characteristics
    # Vegetation (vine rows) has high G values; amplify NIR for clear NDVI contrast
    red = R
    nir = R + np.maximum(G - R, 0) * 4.0  # Increased amplification for clarity
    
    # Clip to maintain natural appearance while producing sharp NDVI distribution
    nir = np.clip(nir, 0.01, 1.0).astype(np.float32)
    red = np.clip(red, 0.01, 1.0).astype(np.float32)
    
    # 3. GeoTIFF spatial reference mapping via Rasterio
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
    
    print(f"✅ Satellite-based data saved: {red_path}, {nir_path}, {rgb_path}")
    return red, nir, shape

def calculate_ndvi(red_path, nir_path, rgb_path, output_path):
    """
    Reads RED and NIR band TIF files, computes NDVI, and displays a side-by-side comparison.
    """
    # 1. Auto-generate data if files are missing
    if not os.path.exists(red_path) or not os.path.exists(nir_path) or not os.path.exists(rgb_path):
        create_realistic_field_from_satellite(red_path, nir_path, rgb_path)

    print(f"Loading [{red_path}] and [{nir_path}]...")

    # 2. Load band data via Rasterio (Float32)
    with rasterio.open(red_path) as src_red:
        red = src_red.read(1).astype('float32')
        meta = src_red.meta

    with rasterio.open(nir_path) as src_nir:
        nir = src_nir.read(1).astype('float32')

    # 3. NDVI computation: (NIR - RED) / (NIR + RED)
    print("Starting NDVI computation...")
    bottom = (nir + red)
    
    # Avoid division by zero — set those pixels to 0
    ndvi = np.where(bottom == 0, 0, (nir - red) / bottom)

    # 4. Save result as Float32 GeoTIFF
    meta.update(dtype=rasterio.float32, count=1)

    with rasterio.open(output_path, 'w', **meta) as dst:
        dst.write(ndvi, 1)

    print(f"✅ NDVI computation complete. Saved to: {output_path}")
    print(f"[Validation Stats] Min: {np.nanmin(ndvi):.3f}, Max: {np.nanmax(ndvi):.3f}")

    # 5. Side-by-side visualization: Original RGB vs NDVI Map
    print("Rendering comparison of original satellite image and computed NDVI map...")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    rgb_img = plt.imread(rgb_path)
    axes[0].imshow(rgb_img)
    axes[0].set_title("Original Satellite View (RGB)")
    axes[0].axis('off')
    
    im1 = axes[1].imshow(ndvi, cmap='RdYlGn', vmin=-0.1, vmax=0.9)
    axes[1].set_title("Calculated NDVI Map")
    axes[1].axis('off')
    fig.colorbar(im1, ax=axes[1], label="NDVI Value")
    
    plt.tight_layout()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_path = os.path.join(base_dir, "step1_result.png")
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✅ Comparison image saved: {save_path}")
    
    plt.show()

    return ndvi

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    RED_FILE = os.path.join(BASE_DIR, "sample_red.tif")
    NIR_FILE = os.path.join(BASE_DIR, "sample_nir.tif")
    RGB_FILE = os.path.join(BASE_DIR, "sample_rgb.jpg")
    OUTPUT_FILE = os.path.join(BASE_DIR, "output_ndvi.tif")
    
    calculate_ndvi(RED_FILE, NIR_FILE, RGB_FILE, OUTPUT_FILE)
