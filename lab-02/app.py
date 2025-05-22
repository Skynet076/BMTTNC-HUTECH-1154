from flask import Flask, render_template, request
import sys
import os

# Đảm bảo import từ thư mục ex01
sys.path.append(os.path.join(os.path.dirname(__file__), 'ex01'))

# Import các Cipher
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar", methods=["GET", "POST"])
def caesar():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        action = request.form["action"]
        try:
            key = int(key)
            cipher = CaesarCipher()
            if action == "encrypt":
                result = cipher.encrypt_text(text, key)
            elif action == "decrypt":
                result = cipher.decrypt_text(text, key)
        except ValueError:
            result = "Key must be an integer from 0-25."
    return render_template("caesar.html", result=result)

@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        action = request.form["action"]
        cipher = VigenereCipher()
        if action == "encrypt":
            result = cipher.vigenere_encrypt(text, key)
        else:
            result = cipher.vigenere_decrypt(text, key)
    return render_template("vigenere.html", result=result)


@app.route("/railfence", methods=["GET", "POST"])
def railfence():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        action = request.form["action"]
        try:
            key = int(key)
            cipher = RailFenceCipher()
            if action == "encrypt":
                result = cipher.rail_fence_encrypt(text, key)
            else:
                result = cipher.rail_fence_decrypt(text, key)
        except ValueError:
            result = "Key must be an integer."
    return render_template("railfence.html", result=result)


@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        action = request.form["action"]
        cipher = PlayFairCipher()
        matrix = cipher.create_playfair_matrix(key)
        if action == "encrypt":
            result = cipher.playfair_encrypt(text, matrix)
        else:
            result = cipher.playfair_decrypt(text, matrix)
    return render_template("playfair.html", result=result)

@app.route("/transposition", methods=["GET", "POST"])
def transposition():
    result = ""
    if request.method == "POST":
        text = request.form["text"]
        key = request.form["key"]
        action = request.form["action"]
        try:
            key = int(key)
            cipher = TranspositionCipher()
            if action == "encrypt":
                result = cipher.encrypt(text, key)
            else:
                result = cipher.decrypt(text, key)
        except ValueError:
            result = "Key must be an integer."
    return render_template("transposition.html", result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5055, debug=True)
