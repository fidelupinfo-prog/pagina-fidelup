from PIL import Image, ImageDraw

img = Image.open('assets/nino.png').convert('RGBA')
w, h = img.size

# Create a mask image using floodfill from corners
# The mask will be 255 where background is, 0 otherwise
mask = Image.new('L', (w, h), 0)
ImageDraw.floodfill(mask, (0, 0), 255, thresh=20)
ImageDraw.floodfill(mask, (w-1, 0), 255, thresh=20)
ImageDraw.floodfill(mask, (0, h-1), 255, thresh=20)
ImageDraw.floodfill(mask, (w-1, h-1), 255, thresh=20)

pixels = img.load()
mask_pixels = mask.load()

# Optional: soften edges (anti-aliasing)
# To avoid a harsh cut, we can find boundary pixels and give them partial transparency
for y in range(h):
    for x in range(w):
        if mask_pixels[x, y] == 255:
            # It's background
            pixels[x, y] = (0, 0, 0, 0)
        else:
            # Check for fringing on the border? Simple approach: if it's white-ish and near the border, reduce alpha.
            pass

img.save('assets/nino_transparent.png', 'PNG')
print('Saved assets/nino_transparent.png')
