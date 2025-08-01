from PIL import Image

def decrypt(image_path):
    try:
        img = Image.open(image_path).convert('RGB')
    except FileNotFoundError:
        print(f"Error: Could not find image '{image_path}'.")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred while loading image: {e}")
        return ""

    pixels = img.load()
    width, height = img.size

    bits = []

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bits.append(r & 1)
            bits.append(g & 1)
            bits.append(b & 1)

    chars = []
    for i in range(0, len(bits), 8):
        byte_bits = bits[i:i+8]
        if len(byte_bits) < 8:
            break

        byte_val = 0
        for bit in byte_bits:
            byte_val = (byte_val << 1) | bit

        if byte_val == 0:
            break

        chars.append(chr(byte_val))

    return ''.join(chars)
