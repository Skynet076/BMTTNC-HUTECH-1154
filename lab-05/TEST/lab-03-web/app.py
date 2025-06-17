import subprocess
from flask import Flask, request, jsonify, render_template
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# ========== OPEN FORMS ==========

@app.route('/open-caesar')
def open_caesar():
    try:
        subprocess.Popen(['python', './caesar_cipher.py'])
        return jsonify({'status': 'Form Caesar Cipher đã được mở'})
    except Exception as e:
        return jsonify({'status': f'Lỗi mở form: {str(e)}'}), 500

@app.route('/open-vigenere')
def open_vigenere():
    try:
        subprocess.Popen(['python', './vigenere_cipher.py'])
        return jsonify({'status': 'Form Vigenère Cipher đã được mở'})
    except Exception as e:
        return jsonify({'status': f'Lỗi mở form: {str(e)}'}), 500

@app.route('/open-railfence')
def open_railfence():
    try:
        subprocess.Popen(['python', './railfence_cipher.py'])
        return jsonify({'status': 'Form Rail Fence Cipher đã được mở'})
    except Exception as e:
        return jsonify({'status': f'Lỗi mở form: {str(e)}'}), 500

@app.route('/open-playfair')
def open_playfair():
    try:
        subprocess.Popen(['python', './playfair_cipher.py'])
        return jsonify({'status': 'Form Playfair Cipher đã được mở'})
    except Exception as e:
        return jsonify({'status': f'Lỗi mở form: {str(e)}'}), 500

# ========== API ROUTES (Giữ nguyên) ==========

# Caesar Cipher
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Vigenère Cipher
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypt_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypt_text': decrypt_text})

# Rail Fence Cipher
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypt_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypt_text': decrypt_text})

# Playfair Cipher
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({'playfair_matrix': playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return jsonify({'decrypted_text': decrypted_text})

# Transposition Cipher
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# ========== RUN APP ==========
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
