import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import QFont


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        # QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Quit', self)
        btn.move(150, 150)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')

        self.setWindowTitle("Felix's Gui")
        # self.setWindowIcon(QIcon('./web.png'))
        # self.move(700, 300)
        # self.resize(400, 200)
        self.setGeometry(700, 300, 400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())