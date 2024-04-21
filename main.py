# Main Code

import playfair_cipher
import image_encryption

def main():
    # Playfair Cipher
    user_key = input("Enter the key for encryption (max length 36 characters): ")
    key_matrix = playfair_cipher.generate_key(user_key)
    text = input("Enter the text to encrypt: ").lower()
    encrypted_text = playfair_cipher.encrypt_text(text, key_matrix)
    print("Encrypted message:", encrypted_text)
    decrypted_text = playfair_cipher.decrypt_text(encrypted_text, key_matrix)
    print("Decrypted message:", decrypted_text)

    # Image Encryption
    image_path = input("Enter the path of the image: ")
    image = plt.imread(image_path)
    key = random.sample(range(256), 256)
    encrypted_image = image_encryption.encrypt_image(image, key)
    plt.title("Encrypted Image")
    plt.imshow(encrypted_image)
    plt.show()
    decrypted_image = image_encryption.decrypt_image(encrypted_image, key)
    plt.title("Decrypted Image")
    plt.imshow(decrypted_image)
    plt.show()

if __name__ == "__main__":
    main()
