# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets

# Đảm bảo Qt có thể tìm thấy plugin nếu lỗi hiển thị
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = r"C:\Users\thaih\AppData\Local\Programs\Python\Python313\Lib\site-packages\PyQt5\Qt5\plugins\platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 749)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 160, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 270, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 410, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.txtPlaintext = QtWidgets.QTextEdit(self.centralwidget)
        self.txtPlaintext.setGeometry(QtCore.QRect(260, 160, 551, 87))
        self.txtPlaintext.setObjectName("txtPlaintext")

        self.txtKey = QtWidgets.QTextEdit(self.centralwidget)
        self.txtKey.setGeometry(QtCore.QRect(260, 270, 551, 41))
        self.txtKey.setObjectName("txtKey")

        self.txtCiphertext = QtWidgets.QTextEdit(self.centralwidget)
        self.txtCiphertext.setGeometry(QtCore.QRect(260, 380, 551, 171))
        self.txtCiphertext.setObjectName("txtCiphertext")

        self.btnEncrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnEncrypt.setGeometry(QtCore.QRect(280, 590, 93, 41))
        self.btnEncrypt.setObjectName("btnEncrypt")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 80, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(80)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.btnDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnDecrypt.setGeometry(QtCore.QRect(660, 590, 93, 41))
        self.btnDecrypt.setObjectName("btnDecrypt")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 995, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ======= Áp dụng QSS =======
        MainWindow.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
                font-family: Arial;
                font-size: 14px;
            }
            QLabel {
                color: #333;
            }
            QTextEdit {
                background-color: #ffffff;
                border: 2px solid #cccccc;
                border-radius: 8px;
                padding: 6px;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border-radius: 10px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #005fa3;
            }
            QPushButton:pressed {
                background-color: #004e8c;
            }
            QLabel#label_4 {
                color: #0078d7;
            }
        """)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caesar Cipher"))
        self.label.setText(_translate("MainWindow", "Plain Text:"))
        self.label_2.setText(_translate("MainWindow", "Key:"))
        self.label_3.setText(_translate("MainWindow", "Cipher Text:"))
        self.btnEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.label_4.setText(_translate("MainWindow", "CAESAR CIPHER"))
        self.btnDecrypt.setText(_translate("MainWindow", "Decrypt"))

# Chạy ứng dụng
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
