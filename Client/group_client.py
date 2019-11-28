import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate
import group, cal, client, login

list = ['', '', '', '', ''] # here get db group
my_ID = ''


class MyMain(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.layout_2 = QBoxLayout(QBoxLayout.TopToBottom)

        self.layout.addLayout(self.layout_2)

        self.setLayout(self.layout)
        self.setupUI()

    def setupUI(self):
        global list
        self.setWindowTitle('MAKE GROUP')
        self.setFixedWidth(200)
        self.setFixedHeight(300)

        if not list:
            list = ['', '', '', '', '']
        print(list)
        self.group1_btn = QPushButton("+")
        self.group1_btn.setFixedHeight(40)
        if not list[0]:
            self.group1_btn.setText('+')
            self.group1_btn.clicked.connect(self.makegroup_btn_clicked)
            # self.close()
        else:
            self.group1_btn.setText(list[0])
            self.group1_btn.clicked.connect(self.group1_btn_clicked)
            # self.close()

        self.group2_btn = QPushButton("+")
        self.group2_btn.setFixedHeight(40)
        if not list[1]:
            self.group2_btn.setText('+')
            self.group2_btn.clicked.connect(self.makegroup_btn_clicked)
            # self.close()
        else:
            # self.close()
            self.group2_btn.setText(list[1])
            self.group2_btn.clicked.connect(self.group2_btn_clicked)

        self.group3_btn = QPushButton("+")
        self.group3_btn.setFixedHeight(40)
        if not list[2]:
            self.group3_btn.setText('+')
            self.group3_btn.clicked.connect(self.makegroup_btn_clicked)
            # self.close()
        else:
            # self.close()
            self.group3_btn.setText(list[2])
            self.group3_btn.clicked.connect(self.group3_btn_clicked)

        self.group4_btn = QPushButton("+")
        self.group4_btn.setFixedHeight(40)
        if not list[3]:
            self.group4_btn.setText('+')
            self.group4_btn.clicked.connect(self.makegroup_btn_clicked)
            # self.close()
        else:
            # self.close()
            self.group4_btn.setText(list[3])
            self.group4_btn.clicked.connect(self.group4_btn_clicked)

        self.group5_btn = QPushButton("+")
        self.group5_btn.setFixedHeight(40)
        if not list[4]:
            self.group5_btn.setText('+')
            self.group5_btn.clicked.connect(self.makegroup_btn_clicked)
            # self.close()
        else:
            # self.close()
            self.group5_btn.setText(list[4])
            self.group5_btn.clicked.connect(self.group5_btn_clicked)

        self.layout_2.addWidget(self.group1_btn)
        self.layout_2.addWidget(self.group2_btn)
        self.layout_2.addWidget(self.group3_btn)
        self.layout_2.addWidget(self.group4_btn)
        self.layout_2.addWidget(self.group5_btn)

#그룹이름에 해당하는 서버쪽의 디렉토리에서 파일목록을 받아와야함.
    def group1_btn_clicked(self):
        global list
        #그룹이름 서버쪽으로 보낸뒤 파일목록 받아오기.

        cal.print_group_name(list[0])
        print(list[0])
        self.myCalender = cal.MyMain()
        QMessageBox.about(self, "WARINIG", "%s"%list[0])
        self.myCalender.show()
        self.close()

    def group2_btn_clicked(self):
        global list
        # 그룹이름 서버쪽으로 보낸뒤 파일목록 받아오기.

        QMessageBox.about(self, "WARINIG", "%s"%list[1])
        cal.print_group_name(list[1])
        self.myCalender = cal.MyMain()
        self.myCalender.show()
        self.close()

    def group3_btn_clicked(self):
        global list
        # 그룹이름 서버쪽으로 보낸뒤 파일목록 받아오기.

        cal.print_group_name(list[2])
        QMessageBox.about(self, "WARINIG", "%s"%list[2])
        self.myCalender = cal.MyMain()
        self.myCalender.show()
        self.close()

    def group4_btn_clicked(self):
        global list
        # 그룹이름 서버쪽으로 보낸뒤 파일목록 받아오기.

        cal.print_group_name(list[3])
        QMessageBox.about(self, "WARINIG", "%s"%list[3])
        self.myCalender = cal.MyMain()
        self.myCalender.show()
        self.close()

    def group5_btn_clicked(self):
        global list
        # 그룹이름 서버쪽으로 보낸뒤 파일목록 받아오기.

        cal.print_group_name(list[4])
        QMessageBox.about(self, "WARINIG", "%s"%list[4])
        self.myCalender = cal.MyMain()
        self.myCalender.show()
        self.close()

    def makegroup_btn_clicked(self):
        global list
        #compare id, pwd in mongo db
        #true -> go login //  false -> make warning.
        self.mySignup = group.MySignup()
        self.mySignup.show()
        self.close()

    # def closeEvent(self, event):
    #
    #     print("User has clicked the red x on the main window")
    #     event.accept()

def print_ID(str):
    global my_ID
    my_ID = str
    print(my_ID)

def print_group_list(grouplist):
    global list
    list = grouplist
    print(list)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MyMain()
#     myWindow.show()
#     app.exec_()