import signup, group_client, client, group
from PyQt5.QtWidgets import *

class MyMain(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.layout_2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_3 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_4 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_5 = QBoxLayout(QBoxLayout.LeftToRight)

        self.layout.addLayout(self.layout_2)
        self.layout.addLayout(self.layout_3)
        self.layout.addLayout(self.layout_4)
        self.layout.addLayout(self.layout_5)

        self.setLayout(self.layout)
        self.setupUI()

    def setupUI(self):
        self.setFixedWidth(220)
        self.setFixedHeight(150)
        self.setWindowTitle('LOGIN')

        self.ID_qlabel = QLabel("ID     : ", self)
        self.ID_lineEdit = QLineEdit("", self)
        self.ID_lineEdit.textChanged

        self.PWD_qlabel = QLabel("PWD : ", self)
        self.PWD_lineEdit = QLineEdit("", self)
        self.PWD_lineEdit.setEchoMode(QLineEdit.Password)
        self.PWD_lineEdit.textChanged

        self.login_btn = QPushButton("LOGIN", self)
        self.signup_btn = QPushButton("SIGN UP", self)
        self.login_btn.clicked.connect(self.login_btn_clicked)
        self.signup_btn.clicked.connect(self.signup_btn_clicked)

        self.NULL1 = QLabel('     ')
        self.NULL2 = QLabel('     ')

        self.layout_2.addWidget(self.ID_qlabel)
        self.layout_2.addWidget(self.ID_lineEdit)
        self.layout_3.addWidget(self.PWD_qlabel)
        self.layout_3.addWidget(self.PWD_lineEdit)
        self.layout_4.addWidget(self.NULL1)
        self.layout_4.addWidget(self.login_btn)
        self.layout_5.addWidget(self.NULL2)
        self.layout_5.addWidget(self.signup_btn)


    def login_btn_clicked(self):
        #compare id, pwd in mongo db
        #true -> go login //  false -> make warning.

        ID = self.ID_lineEdit.text()
        PWD = self.PWD_lineEdit.text()

        if ID:
            if PWD:
                if (client.send_id(ID) == 'False'): # check mongo db
                    QMessageBox.about(self, "Warning", "Please Check your ID.")
                    print("bad")
                elif(client.login(ID, PWD) == False):
                    QMessageBox.about(self, "Warning", "Please Check your Password.")
                    print("bad")
                else:
                    group_client.print_group_list(client.login(ID, PWD))
                    print("good")
                    group.print_ID(ID)
                    group_client.print_ID(ID)
                    # print(group_client.print_group_list(client.login(ID, PWD)))
                    self.myGroup = group_client.MyMain()
                    print("11")
                    self.myGroup.show()
                    self.close()
            else:
                QMessageBox.about(self, "Warning", "Please Enter your Password.")
                print("bad")
        else:
            QMessageBox.about(self, "Warning", "Please Enter your Id.")
            print("bad")


    def signup_btn_clicked(self):
        #compare id, pwd in mongo db
        #true -> go login //  false -> make warning.
        self.mySignup = signup.MySignup()
        self.mySignup.show()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     client.connect()
#     myWindow = MyMain()
#     myWindow.show()
#     app.exec_()