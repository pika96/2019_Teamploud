import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import client, group_client, login

grouplist = []
my_ID = ''

class MySignup(QWidget):
    def __init__(self):
        super().__init__()

        # 레이아웃 선언 및 Form Widget에 설정
        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.layout_2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.null = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_3 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_4 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_5 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_6 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_7 = QBoxLayout(QBoxLayout.LeftToRight)

        # 부모 레이아웃에 자식 레이아웃을 추가
        self.layout.addLayout(self.layout_2)
        self.layout.addLayout(self.null)
        self.layout.addLayout(self.layout_3)
        self.layout.addLayout(self.layout_4)
        self.layout.addLayout(self.layout_5)
        self.layout.addLayout(self.layout_6)
        self.layout.addLayout(self.layout_7)

        self.setLayout(self.layout)
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('MAKE GROUP')
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        self.NULL = QLabel(" ")
        self.ID_qlabel = QLabel("Group Name: ")
        self.ID_lineEdit = QLineEdit("")
        self.ID_lineEdit.textChanged
        self.group_check_btn = QPushButton("Check")
        self.group_check_btn.clicked.connect(self.group_check_btn_clicked)

        self.NAME_qlabel = QLabel("MEMBER1   : ")
        self.NAME_1_lineEdit = QLineEdit("")
        self.NAME_1_lineEdit.setDisabled(True)
        self.NAME_1_put_btn = QPushButton("PUT")
        self.NAME_1_put_btn.setDisabled(True)
        self.NAME_1_put_btn.clicked.connect(self.NAME_1_btn_clicked)
        self.NAME_1_lineEdit.textChanged

        self.NAME_qlabel2 = QLabel("MEMBER2   : ")
        self.NAME_2_lineEdit = QLineEdit("")
        self.NAME_2_lineEdit.setDisabled(True)
        self.NAME_2_put_btn = QPushButton("PUT")
        self.NAME_2_put_btn.setDisabled(True)
        self.NAME_2_put_btn.clicked.connect(self.NAME_2_btn_clicked)
        self.NAME_2_lineEdit.textChanged

        self.NAME_qlabel3 = QLabel("MEMBER3   : ")
        self.NAME_3_lineEdit = QLineEdit("")
        self.NAME_3_lineEdit.setDisabled(True)
        self.NAME_3_put_btn = QPushButton("PUT")
        self.NAME_3_put_btn.setDisabled(True)
        self.NAME_3_put_btn.clicked.connect(self.NAME_3_btn_clicked)
        self.NAME_3_lineEdit.textChanged

        self.NAME_qlabel4 = QLabel("MEMBER4   : ")
        self.NAME_4_lineEdit = QLineEdit("")
        self.NAME_4_lineEdit.setDisabled(True)
        self.NAME_4_put_btn = QPushButton("PUT")
        self.NAME_4_put_btn.setDisabled(True)
        self.NAME_4_put_btn.clicked.connect(self.NAME_4_btn_clicked)
        self.NAME_4_lineEdit.textChanged

        self.make_group_btn = QPushButton("Make Group", self)
        self.make_group_btn.setDisabled(True)
        self.make_group_btn.clicked.connect(self.make_group_btn_clicked)

        self.layout_2.addWidget(self.ID_qlabel)
        self.layout_2.addWidget(self.ID_lineEdit)
        self.layout_2.addWidget(self.group_check_btn)

        self.null.addWidget(self.NULL)

        self.layout_3.addWidget(self.NAME_qlabel)
        self.layout_3.addWidget(self.NAME_1_lineEdit)
        self.layout_3.addWidget(self.NAME_1_put_btn)

        self.layout_4.addWidget(self.NAME_qlabel2)
        self.layout_4.addWidget(self.NAME_2_lineEdit)
        self.layout_4.addWidget(self.NAME_2_put_btn)

        self.layout_5.addWidget(self.NAME_qlabel3)
        self.layout_5.addWidget(self.NAME_3_lineEdit)
        self.layout_5.addWidget(self.NAME_3_put_btn)

        self.layout_6.addWidget(self.NAME_qlabel4)
        self.layout_6.addWidget(self.NAME_4_lineEdit)
        self.layout_6.addWidget(self.NAME_4_put_btn)

        self.layout_7.addWidget(self.make_group_btn, alignment=Qt.AlignRight)

    def group_check_btn_clicked(self):
        global grouplist
        #check id in mongo db
        # when id in mongo db -> warning
        if client.send_group(self.ID_lineEdit.text()): # if true
            QMessageBox.about(self, "WARINIG", "Change your Group Name!")
            print("bad")

        # true then go next
        else:
            if self.ID_lineEdit.text():
                print('myID is : '+my_ID)
                grouplist.append(self.ID_lineEdit.text())
                grouplist.append(my_ID)
                print("group name :"+self.ID_lineEdit.text())
                print(grouplist)
                self.NAME_1_put_btn.setEnabled(True)
                self.NAME_1_lineEdit.setEnabled(True)
                self.make_group_btn.setEnabled(True)
                self.ID_lineEdit.setDisabled(True)
                self.group_check_btn.setDisabled(True)
                QMessageBox.about(self, " ", "Put your Group Members")
            else: #no text
                QMessageBox.about(self, " ", "Make your Group Name")
    def NAME_1_btn_clicked(self):
        global grouplist
        # when id in mongo db -> GOOD!!
        if (self.NAME_1_lineEdit.text() == my_ID):
            QMessageBox.about(self, "WARINIG", "Same Member!\nPlease change member!")
        else:
            if client.send_id(self.NAME_1_lineEdit.text()) =='True':
                grouplist.append(self.NAME_1_lineEdit.text())
                QMessageBox.about(self, " ", "'%s' put your group" %self.NAME_1_lineEdit.text())
                self.NAME_2_put_btn.setEnabled(True)
                self.NAME_2_lineEdit.setEnabled(True)
                self.NAME_1_lineEdit.setDisabled(True)
                self.NAME_1_put_btn.setDisabled(True)
            # no text or not in db
            else:
                QMessageBox.about(self, "WARINIG", "Change your Member!")
    def NAME_2_btn_clicked(self):
        global grouplist
        # when id in mongo db -> GOOD!!
        #if same member -> change message box
        if(self.NAME_2_lineEdit.text() == self.NAME_1_lineEdit.text()and
                self.NAME_2_lineEdit.text() == my_ID):
            QMessageBox.about(self, "WARINIG", "Same Member!\nPlease change member!")
        else:
            if client.send_id(self.NAME_2_lineEdit.text())=='True':
                grouplist.append(self.NAME_2_lineEdit.text())
                QMessageBox.about(self, " ", "'%s' put your group" %self.NAME_2_lineEdit.text())
                self.NAME_3_put_btn.setEnabled(True)
                self.NAME_3_lineEdit.setEnabled(True)
                self.NAME_2_lineEdit.setDisabled(True)
                self.NAME_2_put_btn.setDisabled(True)
            # no text or not in db
            else:
                QMessageBox.about(self, "WARINIG", "Change your Member!")
    def NAME_3_btn_clicked(self):
        global grouplist
        # when id in mongo db -> GOOD!!
        #if same member -> change message box
        if(self.NAME_3_lineEdit.text() == self.NAME_1_lineEdit.text() and
             self.NAME_3_lineEdit.text() == self.NAME_2_lineEdit.text() and
            self.NAME_3_lineEdit.text() == my_ID):
            QMessageBox.about(self, "WARINIG", "Same Member!\nPlease change member!")
        else:
            if client.send_id(self.NAME_3_lineEdit.text())=='True':
                grouplist.append(self.NAME_3_lineEdit.text())
                QMessageBox.about(self, " ", "'%s' put your group" %self.NAME_3_lineEdit.text())
                self.NAME_4_put_btn.setEnabled(True)
                self.NAME_4_lineEdit.setEnabled(True)
                self.NAME_3_lineEdit.setDisabled(True)
                self.NAME_3_put_btn.setDisabled(True)
            # no text or not in db
            else:
                QMessageBox.about(self, "WARINIG", "Change your Member!")
    def NAME_4_btn_clicked(self):
        global grouplist
        # when id in mongo db -> GOOD!!
        #if same member -> change message box
        if(self.NAME_4_lineEdit.text() == self.NAME_1_lineEdit.text() and
             self.NAME_4_lineEdit.text() == self.NAME_2_lineEdit.text()and
             self.NAME_4_lineEdit.text() == self.NAME_3_lineEdit.text()and
                self.NAME_4_lineEdit.text() == my_ID):
            QMessageBox.about(self, "WARINIG", "Same Member!\nPlease change member!")
        else:
            if client.send_id(self.NAME_4_lineEdit.text())=='True':
                grouplist.append(self.NAME_4_lineEdit.text())
                QMessageBox.about(self, " ", "'%s' put your group" %self.NAME_4_lineEdit.text())
                self.NAME_4_lineEdit.setDisabled(True)
                self.NAME_4_put_btn.setDisabled(True)
            # no text or not in db
            else:
                QMessageBox.about(self, "WARINIG", "Change your Member!")
    def make_group_btn_clicked(self):
        global grouplist
        #send group data to mongo database

        QMessageBox.about(self, " ", "make group.")
        # setGroup(self)
        print("afsdfsadfasdfsadfsadfsafdasfd")
        getGroup()
        client.mk_group(grouplist)
        QMessageBox.about(self, "WARNING", "종료후 다시 로그인 해 주세요.")
        self.myGroup = group_client.MyMain()
        self.myGroup.show()
        self.close()
#
# def setGroup(self):
#     global grouplist
#     # grouplist.append(self.ID_lineEdit.text())
#     grouplist.append(self.NAME_1_lineEdit.text())
#     grouplist.append(self.NAME_2_lineEdit.text())
#     grouplist.append(self.NAME_3_lineEdit.text())
#     grouplist.append(self.NAME_4_lineEdit.text())

def getGroup():
    global grouplist
    print(grouplist)
    # return grouplist

def print_ID(str):
    global my_ID
    my_ID = str
    # print(my_ID)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MySignup()
#     myWindow.show()
#     app.exec_()