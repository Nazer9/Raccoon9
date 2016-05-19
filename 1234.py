import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


def initUI(self):
    qbtn = QPushButton('Вихід', self)
    qbtn_1 = QPushButton('Нова гра', self)
    qbtn_2 = QPushButton('Інструкція до гри', self)
    qbtn.clicked.connect(QCoreApplication.instance().quit)
    #qbtn_1.clicked.connect(QCoreApplication.instance())
    qbtn_2.clicked.connect(self.help)
    qbtn.resize(300,100)
    qbtn_1.resize(300, 100)
    qbtn_2.resize(300, 100)
    qbtn.move(250, 320)
    qbtn_1.move(250, 120)
    qbtn_2.move(250, 220)
    self.setGeometry(280, 50, 800, 600)
    self.setWindowTitle('Меню')
    self.show()

def help(self):
    f=open("help.txt","r")
    #print(f.read())
    t=f.read()
    msg = QMessageBox()
    msg.setText(t)
    #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #msg.show()
    retval = msg.exec_()

def closeEvent(self, event):
    reply = QMessageBox.question(self, 'Вихід з гри', "Ви точно хочете покинути гру?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if reply == QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())