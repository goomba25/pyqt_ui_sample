import sys
from PyQt5.QtWidgets import QApplication, QWidget

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Felix's Gui")
        self.move(700, 300)
        self.resize(400, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())