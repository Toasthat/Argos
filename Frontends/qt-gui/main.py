import sys
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QTextBrowser,
    QPushButton,
    QAction,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from argos_common import ARGOS_HOME, ARGOS_CONFIG, load_config


class main(QMainWindow):
    def __init__(self):
        super(main, self).__init__()
        self.title = "Argos"
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 180
        self.initUI()

    def initUI(self):
        super().__init__(self)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create Title Box
        self.titlebox = QTextBrowser(self)
        self.titlebox.move(20, 5)
        self.titlebox.resize(280, 60)
        self.titlebox.append(
            "Please Insert First Name \n* Please Ensure that your face is the only face in view"
        )

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 70)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton("Submit", self)
        self.button.move(110, 120)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        # QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = main()
    sys.exit(app.exec_())
