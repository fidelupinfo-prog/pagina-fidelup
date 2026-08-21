import os
import glob
from PIL import Image, ImageDraw

input_dir = '/home/yadied/.gemini/antigravity/brain/57bfb608-7906-45f1-a0d1-1034557ae45b/'
output_dir = 'assets/'

image_files = glob.glob(os.path.join(input_dir, 'media__*.png'))

def remove_background(input_path, output_path):
    try:
        img = Image.open(input_path).convert('RGBA')
        w, h = img.size
        
        # Create a mask image using floodfill from corners
        mask = Image.new('L', (w, h), 0)
        ImageDraw.floodfill(mask, (0, 0), 255, thresh=20)
        ImageDraw.floodfill(mask, (w-1, 0), 255, thresh=20)
        ImageDraw.floodfill(mask, (0, h-1), 255, thresh=20)
        ImageDraw.floodfill(mask, (w-1, h-1), 255, thresh=20)
        
        pixels = img.load()
        mask_pixels = mask.load()
        
        for y in range(h):
            for x in range(w):
                if mask_pixels[x, y] == 255:
                    pixels[x, y] = (0, 0, 0, 0)
        
        img.save(output_path, 'PNG')
        print(f'Processed and saved to {output_path}')
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

for i, img_path in enumerate(image_files):
    output_path = os.path.join(output_dir, f'nino_chameleon_{i+1}.png')
    remove_background(img_path, output_path)
