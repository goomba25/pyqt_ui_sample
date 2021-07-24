import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QAction, qApp
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        filemenu = menubar.addMenu('&Edit')
        filemenu = menubar.addMenu('&View')
        filemenu = menubar.addMenu('&Tools')
        filemenu = menubar.addMenu('&Help')

        self.statusBar().showMessage('Ready')
        

        btn = QPushButton('Quit', self)
        btn.move(150, 150)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("Felix's Gui")
        self.setGeometry(700, 300, 400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())