import os
import encryptor
import decryptor

def ensure_folder_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def main():
    ensure_folder_exists("Uncrypted_Photo")
    ensure_folder_exists("Encrypted_Photo")

    while True:
        print("\nPlease Choose One Option:" 
              "\n1. Encrypt Message into Image" 
              "\n2. Decrypt Message from Image"
              "\n3. Exit\n: ", end='')

        try:
            option = int(input())
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")
            continue

        if option == 1:
            message = input("Enter the message to encrypt: ").strip()
            if not message:
                print("Message cannot be empty!")
                continue

            photo_name = input(
                "Enter the photo file name (PNG, JPEG, PPM, GIF, TIFF, BMP) "
                "inside the 'Uncrypted_Photo' folder: ").strip()

            photo_path = f"Uncrypted_Photo/{photo_name}"
            enc = encryptor.Encrypt(photo_path, message)
            if not enc.load_image():
                continue

            base_name = os.path.splitext(photo_name)[0]
            output_path = f"Encrypted_Photo/encrypted_{base_name}.png"
            success = enc.encrypt(output_path)
            if success:
                print(f"Encryption successful! Saved as '{output_path}'.")
            else:
                print("Encryption failed.")

        elif option == 2:
            photo_name = input(
                "Enter the encrypted photo file name (PNG, JPEG, PPM, GIF, TIFF, BMP) "
                "inside the 'Encrypted_Photo' folder: ").strip()

            photo_path = f"Encrypted_Photo/{photo_name}"
            decrypted_message = decryptor.decrypt(photo_path)
            print("\nDecrypted message:")
            print(decrypted_message)

        elif option == 3:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
