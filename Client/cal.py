import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDate, QFileInfo
import client, group_client

file_list = ['test.txt','fuck.fuck','씨발','파일개샛기']
list = ['1111','22222','333333','',''] # here get db group
group_name = ""
holidays = []
text = "개ㅅㅂ 일정 받아오는것임"
now_date = ''
my_ID = ''

class MyMain(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self)
        self.layout_name = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_2 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_3 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_4 = QBoxLayout(QBoxLayout.LeftToRight)
        self.layout_5 = QBoxLayout(QBoxLayout.LeftToRight)

        self.layout.addLayout(self.layout_name)
        self.layout.addLayout(self.layout_2)
        self.layout.addLayout(self.layout_3)
        self.layout.addLayout(self.layout_4)
        self.layout.addLayout(self.layout_5)

        self.setLayout(self.layout)
        self.setupUI()

    def setupUI(self):
        global group_name, file_list, text, holidays
        print(group_name)
        self.setWindowTitle('C A L E N D A R')
        self.setFixedWidth(900)
        self.setFixedHeight(1000)

        self.group_name = QLabel("%s" %group_name)
        # self.group_name = QLabel("Group Name")
        self.group_name.setFont(QFont("Apple SD Gothic Neo", 30))

        file_list = client.get_file_list(group_name)
        holidays = client.get_date_list(group_name)

        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.setVerticalHeaderFormat(0)
        self.cal.setFixedHeight(400)
        self.cal.setFixedWidth(400)
        self.make_calendar()
        self.cal.clicked.connect(self.cal_clicked)

        self.it_textEdit = QTextEdit()
        self.it_textEdit.setFixedHeight(400)
        self.it_textEdit.setFixedWidth(400)
        self.it_textEdit.setDisabled(True)

        self.null = QLabel()
        self.null.setFixedWidth(600)
        self.null2 = QLabel()
        self.null2.setFixedWidth(600)

        # this is up load button
        self.change_btn = QPushButton("modify", self)
        self.change_btn.setFont(QFont("Times", 15))
        self.change_btn.setFixedHeight(30)
        self.change_btn.setFixedWidth(80)
        self.change_btn.clicked.connect(self.change_btn_clicked)

        self.OK_btn = QPushButton("OK", self)
        self.OK_btn.setFont(QFont("Times", 15))
        self.OK_btn.setFixedHeight(30)
        self.OK_btn.setFixedWidth(80)
        self.OK_btn.clicked.connect(self.OK_btn_clicked)

        self.filetable = QTableWidget(self)
        self.filetable.setFixedHeight(400)
        self.filetable.setFixedWidth(830)
        self.filetable.setRowCount(len(file_list)) #받아온 파일 리스트 갯수 세어서 넣어주면 됨
        self.filetable.setColumnCount(1)
        self.filetable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.filetable.setDisabled(True)
        self.setTableWidgetData()

        self.files_text = QTextEdit()
        self.files_text.setFixedHeight(400)
        self.files_text.setFixedWidth(830)

        self.file_name = QLineEdit()
        self.file_name.setFixedWidth(740)

        # this is up load button
        self.upload_btn = QPushButton("▲", self)
        self.upload_btn.setFont(QFont("Times", 20))
        self.upload_btn.setFixedHeight(30)
        self.upload_btn.setFixedWidth(80)
        self.upload_btn.clicked.connect(self.upload_btn_clicked)

        # this is down load button
        self.download_btn = QPushButton("▼", self)
        self.download_btn.setFont(QFont("Times", 20))
        self.download_btn.setFixedHeight(30)
        self.download_btn.setFixedWidth(80)
        self.download_btn.clicked.connect(self.download_btn_clicked)

        self.layout_name.addWidget(self.group_name)
        self.layout_2.addWidget(self.cal)
        self.layout_2.addWidget(self.it_textEdit)
        self.layout_3.addWidget(self.null)
        self.layout_3.addWidget(self.change_btn)
        self.layout_3.addWidget(self.OK_btn)
        self.layout_4.addWidget(self.filetable)
        self.layout_5.addWidget(self.null2)
        self.layout_5.addWidget(self.upload_btn)
        self.layout_5.addWidget(self.download_btn)

    def closeEvent(self, event):
        self.myGroup = group_client.MyMain()
        print("11")
        self.myGroup.show()
        print("User has clicked the red x on the main window")
        event.accept()

    def setTableWidgetData(self):
        column_headers = ['FILES']
        self.filetable.setHorizontalHeaderLabels(column_headers)
        count = 0
        while count < len(file_list):
            self.filetable.setItem(count, 0, QTableWidgetItem("%s" %file_list[count]))
            count = count + 1
        # self.filetable.resizeRowsToContents()

    def cal_clicked(self):
        global text, now_date

        now_date = getdate(str(self.cal.selectedDate()))
        print(now_date)
        text = client.find_schedule(now_date, group_name)
        print(text)
        if not text == "False":
            self.it_textEdit.setText(text)
        else:
            self.it_textEdit.setText('')


    def make_calendar(self):
        fm = QTextCharFormat()
        fm.setBackground(Qt.yellow)

        for dday in holidays:
            dday2 = QDate.fromString(dday, "yyyyMMdd")
            self.cal.setDateTextFormat(dday2, fm)

    def change_btn_clicked(self):
        self.it_textEdit.setEnabled(True)


    def OK_btn_clicked(self):
        global text
        text = self.it_textEdit.toPlainText()
        self.it_textEdit.setPlainText(text)
        self.it_textEdit.setDisabled(True)
        client.send_schedule(now_date, text, group_name)
        self.make_calendar()

    def upload_btn_clicked(self):
        #compare id, pwd in mongo db
        #true -> go login //  false -> make warning.

        fname = QFileDialog.getOpenFileName(self, 'Open file', "", "All Files(*);; Python Files(*.py)", '/home')
        if fname[0]:
            client.fileupload_client(fname[0])
            print(fname[0])
        else:
            QMessageBox.about(self, "Warning", "Please select a file!")

    def download_btn_clicked(self):
        #compare id, pwd in mongo db
        #true -> go login //  false -> make warning.
        print(type(file_list[self.filetable.currentRow()]))
        print(file_list[self.filetable.currentRow()])
        client.filedownload(group_name, file_list[self.filetable.currentRow()])
        QMessageBox.about(self, "DOWN", "%s"%file_list[self.filetable.currentRow()])

def print_group_name(str):
    global group_name
    group_name = str
    print(group_name)

def print_ID(str):
    global my_ID
    my_ID = str
    print(my_ID)

def getdate(string):
    if len(string) == 31:
        year = string[19:23]
        month = string[25:27]
        day = string[29]
        string = year + month + str('0') + day
        # string = year + month + day
        return string
    else:
        year = string[19:23]
        month = string[25:27]
        day = string[29:31]
        string = year + month + day
        return string


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyMain()
    myWindow.show()
    app.exec_()