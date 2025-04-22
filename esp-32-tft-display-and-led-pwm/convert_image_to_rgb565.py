from PIL import Image

def rgb_to_rgb565(r, g, b):
    return (((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)) & 0xFFFF

def image_to_rgb565_array(image_path, resize=None):
    img = Image.open(image_path).convert('RGB')
    
    if resize:
        img = img.resize(resize)

    width, height = img.size
    pixels = list(img.getdata())
    
    result = "{{"
    for y in range(height):
        row = "{"
        for x in range(width):
            r, g, b = pixels[y * width + x]
            rgb565 = rgb_to_rgb565(r, g, b)
            row += f"0x{rgb565:04X},"
        row = row.rstrip(',') + "},\n"
        result += row
    result = result.rstrip(',\n') + "}}"
    return result

output = image_to_rgb565_array("c:\\in\\test.png", resize=(100, 100))

with open("c:\\out\\image_rgb565_array.txt", "w") as f:
    f.write(output)
