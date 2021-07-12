from logger import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
import sys
from uiConfig import *


class StartUtility(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.utility = Window()
        self.utility.show()


class Window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.dragFrame.mouseMoveEvent = self.mouseMoveEvent
        self.dragPos = QtCore.QPoint()
        # self.setWindowIcon(QIcon('images/mouse2.png'))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        KeyLogger.init_ui(self)
        self.ui.log = ""
        keyboard.on_release(callback=self.keyboard_action)

    def keyboard_action(self, event):
        """
        This callback is invoked whenever a keyboard event occurs
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
        self.ui.scriptIndicator.setText(name.replace("\n", ""))
        self.ui.log += name

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == "__main__":
    app = StartUtility(sys.argv)
    sys.exit(app.exec_())