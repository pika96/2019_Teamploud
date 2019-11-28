import login, client
import sys
from PyQt5.QtWidgets import *

class MyMain(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.layout_2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_3 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_4 = QBoxLayout(QBoxLayout.LeftToRight)

        self.layout.addLayout(self.layout_2)
        self.layout.addLayout(self.layout_3)
        self.layout.addLayout(self.layout_4)

        self.setLayout(self.layout)
        self.setupUI()

    def setupUI(self):
        self.setFixedWidth(220)
        self.setFixedHeight(150)
        self.setWindowTitle('PORT')

        self.IP_label = QLabel("↓↓ INSERT SERVER IP ↓↓")
        self.IP_lineedit = QLineEdit("")
        self.NULL = QLabel("       ")
        self.IP_btn = QPushButton("INSERT")
        self.IP_btn.clicked.connect(self.IP_btn_clicked)

        self.layout_2.addWidget(self.IP_label)
        self.layout_3.addWidget(self.IP_lineedit)
        self.layout_4.addWidget(self.NULL)
        self.layout_4.addWidget(self.IP_btn)

    def IP_btn_clicked(self):
        print(self.IP_lineedit.text())
        server_ip = self.IP_lineedit.text()
        client.connect(server_ip)
        self.myWindow = login.MyMain()
        self.myWindow.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyMain()
    myWindow.show()
    app.exec_()