from cryptography.fernet import Fernet
import os

# Function to load or generate the encryption key
def load_or_generate_key(key_file='C:/Users/alber/Documents/Soreta3E/key.key'):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    return key

# Function to encrypt a file
def encrypt_file(input_file_path, output_file_path, key):
    cipher_suite = Fernet(key)
    with open(input_file_path, 'rb') as f:
        data = f.read()
    encrypted_data = cipher_suite.encrypt(data)
    with open(output_file_path, 'wb') as f:
        f.write(encrypted_data)

# Main function
def main():
    base_dir = 'C:/Users/alber/Documents/Soreta3E/'
    data_dir = os.path.join(base_dir, 'F')

    # Create data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Load or generate encryption key
    key = load_or_generate_key()

    # Encrypt text file
    input_text_path = os.path.join(data_dir, 'file.txt')
    encrypted_text_path = os.path.join(data_dir, 'file_encrypted.txt')
    encrypt_file(input_text_path, encrypted_text_path, key)
    os.remove(input_text_path)  # Remove original text file after encryption

    # Encrypt image file
    input_image_path = os.path.join(base_dir, 'img.jpg')
    encrypted_image_path = os.path.join(base_dir, 'img_encrypted.jpg')
    encrypt_file(input_image_path, encrypted_image_path, key)
    os.remove(input_image_path)  # Remove original image file after encryption

    print("Encryption completed.")

if __name__ == "__main__":
    main()
