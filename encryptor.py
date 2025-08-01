from PIL import Image
import os

class Encrypt:
    def __init__(self, image_path, unencrypted_message):
        self.image_path = image_path
        self.unencrypted_message = unencrypted_message
        self.img = None
        self.pixels = None

    def load_image(self):
        try:
            self.img = Image.open(self.image_path).convert('RGB')
            self.pixels = self.img.load()
        except FileNotFoundError:
            print(f"Error: Could not find image '{self.image_path}'.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while loading image: {e}")
            return False
        return True

    def text_to_bin(self):
        binary_message = ''.join(format(ord(char), '08b') for char in self.unencrypted_message)
        return binary_message + '00000000'


    def check_capacity(self, binary_message):
        width, height = self.img.size
        max_bits = width * height * 3
        if len(binary_message) > max_bits:
            print(f"Error: Message too large to fit in image. Max bits: {max_bits}, Message bits: {len(binary_message)}")
            return False
        return True

    def encrypt(self, output_path="Encrypted.png"):
        if self.img is None or self.pixels is None:
            print("Error: Image not loaded. Please load image first.")
            return False
        
        binary_message = self.text_to_bin()
        if not self.check_capacity(binary_message):
            return False

        width, height = self.img.size
        bit_index = 0

        for y in range(height):
            for x in range(width):
                if bit_index >= len(binary_message):
                    break

                r, g, b = self.pixels[x, y]
                r = (r & ~1) | int(binary_message[bit_index]) if bit_index < len(binary_message) else r
                bit_index += 1

                g = (g & ~1) | int(binary_message[bit_index]) if bit_index < len(binary_message) else g
                bit_index += 1

                b = (b & ~1) | int(binary_message[bit_index]) if bit_index < len(binary_message) else b
                bit_index += 1

                self.pixels[x, y] = (r, g, b)

            if bit_index >= len(binary_message):
                break
        
        try:
            output_folder = os.path.dirname(output_path)
            if output_folder and not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            self.img.save(output_path)
            print(f"Message encrypted and saved as '{output_path}'")
            return output_path
        except Exception as e:
            print(f"Error saving encrypted image: {e}")
            return False
