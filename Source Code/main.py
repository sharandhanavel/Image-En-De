import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import random
import image_encryption

class ImageEncryptionApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Encryption & Decryption")

        self.img_label = tk.Label(self, text="Selected Image")
        self.img_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.select_button = tk.Button(self, text="Select Image", command=self.choose_file)
        self.select_button.grid(row=2, column=0, padx=10, pady=10)

        self.encrypt_button = tk.Button(self, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=2, column=1, padx=10, pady=10)

        self.decrypt_button = tk.Button(self, text="Decrypt", command=self.decrypt, state="disabled")
        self.decrypt_button.grid(row=2, column=2, padx=10, pady=10)

        self.img = None
        self.encrypted_img = None
        self.decrypted_img = None
        self.key = None

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if file_path:
            self.img = Image.open(file_path).convert("RGB")
            self.show_image(self.img)

    def encrypt(self):
        if self.img is not None:
            self.key = self.generate_key()
            self.encrypted_img = image_encryption.encrypt_image(np.array(self.img), self.key)
            self.show_image(self.encrypted_img)
            self.decrypt_button.config(state="normal")

    def decrypt(self):
        if self.encrypted_img is not None and self.key is not None:
            self.decrypted_img = image_encryption.decrypt_image(self.encrypted_img, self.key)
            self.show_image(self.decrypted_img)

    def generate_key(self):
        key = []
        while len(key) != 256:
            j = random.randrange(0, 256)
            if j not in key:
                key.append(j)
        return key

    def show_image(self, img):
        if isinstance(img, np.ndarray):
            img = Image.fromarray(img.astype("uint8"))
        img = ImageTk.PhotoImage(img)
        self.canvas.image = img  # to prevent garbage collection
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

if __name__ == "__main__":
    app = ImageEncryptionApp()
    app.mainloop()