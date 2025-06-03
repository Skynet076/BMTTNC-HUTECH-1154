# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.railfence import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Gán các nút
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)  # ENCRYPT
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)  # DECRYPT

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5050/api/railfence/encrypt"
        try:
            key = int(self.ui.textEdit.toPlainText())  # Key phải là số nguyên
            payload = {
                "plain_text": self.ui.plainTextEdit.toPlainText(),
                "key": key
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_2.setText(data["encrypted_text"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API: ", response.text)
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Key must be an integer")
            msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5050/api/railfence/decrypt"
        try:
            key = int(self.ui.textEdit.toPlainText())  # Key phải là số nguyên
            payload = {
                "cipher_text": self.ui.textEdit_2.toPlainText(),
                "key": key
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit.setPlainText(data["decrypted_text"])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API: ", response.text)
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Key must be an integer")
            msg.exec_()
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())