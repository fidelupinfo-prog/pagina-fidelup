from PIL import Image, ImageDraw

def remove_background(input_path, output_path):
    try:
        img = Image.open(input_path).convert('RGBA')
        w, h = img.size
        
        # Create a mask image using floodfill from corners
        mask = Image.new('L', (w, h), 0)
        # We assume background is white-ish at the corners.
        # Use a higher threshold if the white is not perfect.
        thresh = 30
        
        # Floodfill from corners
        ImageDraw.floodfill(mask, (0, 0), 255, thresh=thresh)
        ImageDraw.floodfill(mask, (w-1, 0), 255, thresh=thresh)
        ImageDraw.floodfill(mask, (0, h-1), 255, thresh=thresh)
        ImageDraw.floodfill(mask, (w-1, h-1), 255, thresh=thresh)
        
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

remove_background('assets/hero_journey.png', 'assets/hero_journey_t.png')
