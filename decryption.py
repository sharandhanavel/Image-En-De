import numpy as np

def decrypt_image(img, key):
    rows, cols, _ = img.shape
    decrypted_img = np.zeros_like(img, dtype=int)
    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                decrypted_img[i][j][k] = key.index(img[i][j][k])
    return decrypted_img
