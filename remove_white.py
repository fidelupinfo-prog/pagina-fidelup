from PIL import Image

def make_white_transparent(input_path, output_path, threshold=240):
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # item is (R, G, B, A)
            if item[0] > threshold and item[1] > threshold and item[2] > threshold:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Successfully processed {input_path}")
    except Exception as e:
        print(f"Error: {e}")

make_white_transparent('assets/hero_journey.png', 'assets/hero_journey_t.png')
