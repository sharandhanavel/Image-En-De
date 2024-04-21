def generate_key(user_key):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    key = []
    for char in user_key:
        if char not in key:
            key.append(char)
    for char in alphabet:
        if char not in user_key:
            key.append(char)
    key_matrix = [key[i:i+6] for i in range(0, 36, 6)]
    return key_matrix

def search(char, key_matrix):
    for i in range(6):
        for j in range(6):
            if key_matrix[i][j] == char:
                return i, j

def encrypt_text(text, key_matrix):
    encrypted_text = ""
    index = 0
    while index < len(text):
        if index == len(text) - 1:
            encrypted_text += text[index]
        else:
            char1 = text[index]
            char2 = text[index+1]
            row1, col1 = search(char1, key_matrix)
            row2, col2 = search(char2, key_matrix)
            if char1 == char2:
                encrypted_text += char1 + "@"
            elif row1 == row2:
                encrypted_text += key_matrix[row1][(col1+1) % 6] + key_matrix[row2][(col2+1) % 6]
            elif col1 == col2:
                encrypted_text += key_matrix[(row1+1) % 6][col1] + key_matrix[(row2+1) % 6][col2]
            else:
                encrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]
        index += 2
    return encrypted_text

def decrypt_text(encrypted_text, key_matrix):
    decrypted_text = ""
    index = 0
    while index < len(encrypted_text):
        if index == len(encrypted_text) - 1:
            decrypted_text += encrypted_text[index]
        elif encrypted_text[index] == "@" or encrypted_text[index+1] == "@":
            if encrypted_text[index] != "@":
                decrypted_text += encrypted_text[index] + encrypted_text[index]
            else:
                decrypted_text += encrypted_text[index+1] + encrypted_text[index+1]
        else:
            char1 = encrypted_text[index]
            char2 = encrypted_text[index+1]
            row1, col1 = search(char1, key_matrix)
            row2, col2 = search(char2, key_matrix)
            if row1 == row2:
                decrypted_text += key_matrix[row1][(col1-1) % 6] + key_matrix[row2][(col2-1) % 6]
            elif col1 == col2:
                decrypted_text += key_matrix[(row1-1) % 6][col1] + key_matrix[(row2-1) % 6][col2]
            else:
                decrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]
        index += 2
    return decrypted_text