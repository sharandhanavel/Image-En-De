import matplotlib.pyplot as plt
import numpy as np
import random

def encrypt_image(image, key):
    encrypted_image = np.zeros(image.shape, dtype=int)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for k in range(3):
                encrypted_image[i][j][k] = key[image[i][j][k]]
    return encrypted_image

def decrypt_image(encrypted_image, key):
    decrypted_image = np.zeros(encrypted_image.shape, dtype=int)
    for i in range(encrypted_image.shape[0]):
        for j in range(encrypted_image.shape[1]):
            for k in range(3):
                decrypted_image[i][j][k] = key.index(encrypted_image[i][j][k])
    return decrypted_image