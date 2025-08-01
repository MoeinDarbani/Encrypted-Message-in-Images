and Pillow

This is a simple Python project that allows you to hide (encrypt) text messages inside images and retrieve (decrypt) them later. The project uses the Pillow library for image processing and demonstrates a basic steganography technique by modifying the pixel values to embed ASCII data.

## Features

- Hide a text message inside an image without visibly altering the image.
- Extract the hidden message from the modified image.
- Supports common image formats such as PNG, JPEG, BMP, GIF, TIFF, etc.
- Simple command-line interface to choose between encryption and decryption.

## How It Works

1. The input message is converted into ASCII values.
2. These values are encoded into the pixels of the input image by slightly changing the pixel RGB values.
3. The modified image is saved as a new file.
4. To retrieve the message, the program reads the encoded pixels and converts the data back to text.

## Installation

Make sure you have Python installed (version 3.6 or higher).

Install required dependencies:

```
pip install Pillow
```

Usage

Run the main script and follow the prompts:

```
python main.py
```

You will be asked to:

Choose to encrypt a message into an image or decrypt a message from an image.

Provide the message text (for encryption).

Provide the filename of the image (make sure it’s in the correct folder).


The encrypted image will be saved in a separate folder.

Notes

This is a beginner-level project aimed at learning Python, image processing, and basic steganography concepts.

The project was developed with the help of AI tools for guidance and troubleshooting, but all the code has been carefully written and understood by the author.


Acknowledgements

Thanks to Jadi for the inspiration and ideas that helped me build this project!
