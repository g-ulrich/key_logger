from PyQt5.QtCore import QTimer, QTime
from PyQt5 import QtGui
import keyboard
# from threading import Timer
from datetime import datetime
import os


def current_time():
    t = QTime.currentTime().toString()
    am_pm = "pm" if 12 < int(t[:2]) < 23 else "am"
    return t + " " + am_pm


class KeyLogger:
    """
    System / Ui
    """
    def ui_log(self, message):
        t, c = current_time(), self.ui.keyLoggerLog.count()
        self.ui.keyLoggerLog.setCurrentRow(c - 1)
        if c > 100:
            self.ui.keyLoggerLog.clear()
            self.ui.keyLoggerLog.addItem("CLEARED --> {}".format(t))
        self.ui.keyLoggerLog.takeItem(c - 1)
        self.ui.keyLoggerLog.addItem("{} - {}".format(t, message))
        self.ui.keyLoggerLog.addItem("")
        self.ui.logUpdate.setText("Updated: " + current_time())

    def read_log(self):
        f = open(f"logs/{self.ui.current_file_name}.txt", "r")
        contents = f.read()
        f.close()
        return contents

    def write_log(self):
        if self.ui.log:
            if not os.path.exists("logs"):
                os.makedirs("logs")
            self.ui.current_file_name = str(datetime.now()).replace(" ", "_").replace(":", "-").replace(".", "_")
            # os.mknod(f"logs/{self.ui.current_file_name}.txt")
            f = open(f"logs/{self.ui.current_file_name}.txt", "w")
            f.write(self.ui.log)
            f.close()
            KeyLogger.ui_log(self, f"Logged {len(self.ui.log)} Chars!")
            self.ui.log = ""
        else:
            KeyLogger.ui_log(self, "Nothing to log.")

    def update_time(self):
        self.ui.updateTime.setText(current_time())

    def init_ui(self):
        self.setFixedWidth(350)
        self.setFixedHeight(200)
        self.ui.updateTime.setText(current_time())
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.startBtn.clicked.connect(lambda: KeyLogger.start(self))
        self.ui.stopBtn.clicked.connect(lambda: KeyLogger.stop(self))
        self.ui.scriptIndicator.setText("")
        self.ui.timer = QTimer()
        self.ui.timer.timeout.connect(lambda: KeyLogger.update_time(self))
        self.ui.timer.start(1000)

    """
    Logger
    """
    def start(self):
        try:
            self.ui.submit_log.stop()
        except:
            pass
        self.ui.submit_log = QTimer()
        self.ui.submit_log.timeout.connect(lambda: KeyLogger.write_log(self))
        self.ui.submit_log.start(60000*self.ui.mins.value())
        self.ui.log = ""
        self.ui.scriptIndicator.setText("Started!")
        KeyLogger.ui_log(self, "Started!")
        self.ui.startBtn.setEnabled(False)
        self.ui.stopBtn.setEnabled(True)

    def stop(self):
        try:
            self.ui.submit_log.stop()
        except:
            pass
        self.ui.scriptIndicator.setText("Stopped!")
        KeyLogger.ui_log(self, "Stopped!")
        self.ui.stopBtn.setEnabled(False)
        self.ui.startBtn.setEnabled(True)

