import sys
from PIL import Image
import numpy as np
import hashlib

def calculate_image_hash(image_path):
    """Computes SHA-256 hash of the image."""
    with open(image_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def add_adv_gray_noise(input_path, output_path, noise_level=3):
    """
    Adds subtle gray noise to an image to make it harder for AI to recognize, 
    while keeping it visually undetectable to humans.

    :param input_path: Path to the input image file
    :param output_path: Path to save the output image file
    :param noise_level: Standard deviation of noise; higher values increase AI confusion
    """
    # Open image and convert to grayscale to extract luminance
    img = Image.open(input_path).convert("RGB")
    data = np.array(img, dtype=np.float32)

    # Generate slight gray noise targeting all color channels equally
    noise = np.random.normal(loc=0, scale=noise_level, size=data.shape)
    
    # Subtle noise application to avoid human detection
    noisy_image = data + noise

    # Ensure values stay within valid range
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    # Convert back to an image
    noisy_img = Image.fromarray(noisy_image)

    # Save the noisy image
    noisy_img.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: `python script.py <input_image_path> <output_image_path>` or \
        `python script.py <input_image_path> <output_image_path> <noise_level>`")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    noise_level = int(sys.argv[3])
    
    original_hash = calculate_image_hash(input_path)
    add_adv_gray_noise(input_path, output_path, noise_level)
    modified_hash = calculate_image_hash(output_path)

    print(f"Original Image Hash: {original_hash}")
    print(f"Modified Image Hash: {modified_hash}")





    