from PyQt5.QtWidgets import *
import socket
import hashlib
import client, login

class MySignup(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.layout_2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_3 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_4 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_5 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_6 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_7 = QBoxLayout(QBoxLayout.LeftToRight)

        self.layout.addLayout(self.layout_2)
        self.layout.addLayout(self.layout_3)
        self.layout.addLayout(self.layout_4)
        self.layout.addLayout(self.layout_5)
        self.layout.addLayout(self.layout_6)
        self.layout.addLayout(self.layout_7)

        self.setLayout(self.layout)
        self.setupUI()

    def setupUI(self):
        self.setFixedWidth(250)
        self.setFixedHeight(200)
        self.setWindowTitle('SIGNUP')

        self.ID_qlabel = QLabel("ID        : ")
        self.ID_lineEdit = QLineEdit("")
        self.ID_lineEdit.textChanged

        self.check_btn = QPushButton("Check ID")
        self.check_btn.clicked.connect(self.check_btn_clicked)

        self.PWD_qlabel = QLabel("PWD    : ")
        self.PWD_lineEdit = QLineEdit("")
        self.PWD_lineEdit.textChanged

        self.NAME_qlabel = QLabel("NAME   : ")
        self.NAME_lineEdit = QLineEdit("")
        self.NAME_lineEdit.textChanged

        self.signup_btn = QPushButton("SIGN UP")
        self.signup_btn.clicked.connect(self.signup_btn_clicked)
        self.signup_btn.setDisabled(True)

        self.NULL1 = QLabel('     ')
        self.NULL2 = QLabel('     ')
        self.NULL3 = QLabel('     ')

        self.layout_2.addWidget(self.ID_qlabel)
        self.layout_2.addWidget(self.ID_lineEdit)
        self.layout_3.addWidget(self.NULL1)
        self.layout_3.addWidget(self.check_btn)
        self.layout_4.addWidget(self.NULL2)
        self.layout_5.addWidget(self.PWD_qlabel)
        self.layout_5.addWidget(self.PWD_lineEdit)
        self.layout_6.addWidget(self.NAME_qlabel)
        self.layout_6.addWidget(self.NAME_lineEdit)
        self.layout_7.addWidget(self.NULL3)
        self.layout_7.addWidget(self.signup_btn)

    def closeEvent(self, event):
        print("User has clicked the red x on the main window")
        event.accept()

    def check_btn_clicked(self):
        #check id in mongo db
        # when id in mongo db -> warning
        # if is_Check_Ok == :
        print("씨발"+client.send_id(self.ID_lineEdit.text()))
        if (client.send_id(self.ID_lineEdit.text()) == "True"):
            QMessageBox.about(self, "Warning", "Change your ID.")
            self.signup_btn.setDisabled(True)
            print("bad")

        # true then go next
        else:
            if self.ID_lineEdit.text():
                print(self.ID_lineEdit.text())
                print("good")
                self.signup_btn.setEnabled(True)
                self.ID_lineEdit.setDisabled(True)
                self.check_btn.setDisabled(True)
            else:
                print("no text.")

    def signup_btn_clicked(self):
        #write id, pwd, name in mongo db
        ID = self.ID_lineEdit.text()
        PWD = self.PWD_lineEdit.text()
        NAME = self.NAME_lineEdit.text()
        client.send_userinfo(ID, PWD, NAME)
        QMessageBox.about(self, "Success", "Make your ID successfully!!\n\nPlease Sign in")

        #then close
        self.close()