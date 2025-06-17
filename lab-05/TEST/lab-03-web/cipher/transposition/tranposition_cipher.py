class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        decrypted_text = [''] * ((len(text) + key - 1) // key)
        row, col = 0, 0
        for symbol in text:
            decrypted_text[row] += symbol
            row += 1
            if row == len(decrypted_text) or (row == len(decrypted_text) - 1 and col >= len(text) % key):
                row = 0
                col += 1
        return ''.join(decrypted_text)