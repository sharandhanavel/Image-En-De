import numpy as np

def encrypt_image(img, key):
    rows, cols, _ = img.shape
    encrypted_img = np.zeros_like(img, dtype=int)
    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                encrypted_img[i][j][k] = key[img[i][j][k]]
    return encrypted_img

def decrypt_image(encrypted_img, key):
    rows, cols, _ = encrypted_img.shape
    decrypted_img = np.zeros_like(encrypted_img, dtype=int)
    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                decrypted_img[i][j][k] = key.index(encrypted_img[i][j][k])
    return decrypted_img
