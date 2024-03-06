from cryptography.fernet import Fernet
import os

def load_key(key_file='C:/Users/alber/Documents/Soreta3E/key.key'):
    with open(key_file, 'rb') as f:
        key = f.read()
    return key


def decrypt_file(input_file_path, output_file_path, key):
    cipher_suite = Fernet(key)
    with open(input_file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file_path, 'wb') as f:
        f.write(decrypted_data)


def check_payment(payment_amount):
    user_payment = float(input("Please enter the payment first"))
    if user_payment >= payment_amount:
        print("decrypted pay.")
        return True
    else:
        print("Insufficient.")
        return False


def main():
    base_dir = 'C:/Users/alber/Documents/Soreta3E/'
    data_dir = os.path.join(base_dir, 'F')

   
    payment_amount = 1000

  
    key = load_key()

   
    if not check_payment(payment_amount):
        return

    
    encrypted_text_path = os.path.join(data_dir, 'file_encrypted.txt')
    decrypted_text_path = os.path.join(data_dir, 'file.txt')
    decrypt_file(encrypted_text_path, decrypted_text_path, key)
   
    os.remove(encrypted_text_path)

  
    encrypted_image_path = os.path.join(base_dir, 'img_encrypted.jpg')
    decrypted_image_path = os.path.join(base_dir, 'img.jpg')
    decrypt_file(encrypted_image_path, decrypted_image_path, key)
  
    os.remove(encrypted_image_path)

    print("Decryption completed.")

if __name__ == "__main__":
    main()
