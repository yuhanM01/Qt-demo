import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from firstMainWin import *

class MyMainWinow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWinow,self).__init__(parent)
        self.setupUi(self)

        self.close_WinBtn.clicked.connect(self.on_pushButton_clicked)

    # 槽函数
    def on_pushButton_clicked(self):
        print('shouyi:', self.doubleSpinBox_returns_min.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWinow()
    myWin.show()
    sys.exit(app.exec())