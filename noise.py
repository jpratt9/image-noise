import sys
from PIL import Image
import numpy as np

def add_noise_to_image(input_path, output_path):
    # Open an image file
    img = Image.open(input_path)

    # Convert image to numpy array
    data = np.array(img)

    # Add random noise
    noise = np.random.normal(0, 1, data.shape)
    noisy_image = data + noise

    # Ensure values are valid
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    # Convert back to an image
    noisy_img = Image.fromarray(noisy_image)

    # Save the noisy image
    noisy_img.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_image_path> <output_image_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    add_noise_to_image(input_path, output_path)
