import sys
import mysql.connector
from PyQt5 import QtWidgets

config = {
    'user' : 'munezuka',
    'password' : 'munezou',
    'host' : 'raspi04.local',
    'database' : 'munezuka',
    'charset' : 'utf8',
}
def sql_connect():
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor(buffered=True)
    sql = "show tables;"
    cur.execute(sql)
    for (table) in cur:
        print(table)
    cur.close()
    cnx.close()



class window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()




    def init_ui(self):
        self.l1 = QtWidgets.QLabel('社員登録')
        self.l2 = QtWidgets.QLabel("ID")
        self.l3 = QtWidgets.QLabel("Name")
        self.l4 = QtWidgets.QLabel("Price")
        self.le1 = QtWidgets.QLineEdit()
        self.le2 = QtWidgets.QLineEdit()
        self.le3 = QtWidgets.QLineEdit()
        self.le4 = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Add')
        self.b2 = QtWidgets.QPushButton('Clear')
        self.b3 =  QtWidgets.QPushButton("Getnum")


        h_box = QtWidgets.QHBoxLayout()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.l1)
        buttonLayout = QtWidgets.QVBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.b1)
        buttonLayout.addWidget(self.b2)

        g_box = QtWidgets.QGridLayout()
        g_box.addWidget(self.l2,0,0)
        g_box.addWidget(self.l3,1,0)
        g_box.addWidget(self.l4,2,0)

        g_box.addWidget(self.le2,0,1)
        g_box.addWidget(self.le3,1,1)
        g_box.addWidget(self.le4,2,1)

        h_box.addLayout(g_box)
        h_box.addLayout(buttonLayout)
        v_box.addLayout(h_box)
        v_box.addStretch()
        #        self.setLayout(v_box)
        self.setLayout(v_box)
        self.setWindowTitle("Testprogram001")

        self.b1.clicked.connect(self.btn_click)
        self.b2.clicked.connect(self.btn_click)
        self.b3.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        sender = self.sender()
        if sender.text() == 'Add':
            print("sender = add")
            sql_connect()
        else:
            print("other")


app = QtWidgets.QApplication(sys.argv)
a_window =window()
sys.exit(app.exec())
