# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\desktop2\2021\scripts\python\PyCharmProjects\keylogger\logger.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 201)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dragFrame = QtWidgets.QFrame(self.centralwidget)
        self.dragFrame.setStyleSheet("QFrame {\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"    background-color: rgb(83, 83, 83);\n"
"}")
        self.dragFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dragFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dragFrame.setObjectName("dragFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dragFrame)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.dragFrame)
        self.pushButton.setStyleSheet("border: none;\n"
"background-image: url(:/imgs/images/16x16/cil-notes.png);\n"
"background-color: none;\n"
"background-repeat: no-repeat;\n"
"color: #fff;\n"
"padding:3px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.minimize = QtWidgets.QPushButton(self.dragFrame)
        self.minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimize.setStyleSheet("\n"
"QPushButton {\n"
"    image: url(:/imgs/images/24x24/cil-window-minimize.png);\n"
"background-color: rgb(83, 83, 83);\n"
"border:none;\n"
"padding:3px;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #666666;\n"
"}")
        self.minimize.setText("")
        self.minimize.setObjectName("minimize")
        self.horizontalLayout.addWidget(self.minimize)
        self.close = QtWidgets.QPushButton(self.dragFrame)
        self.close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close.setStyleSheet("\n"
"QPushButton {\n"
"    \n"
"    image: url(:/imgs/images/24x24/cil-x.png);\n"
"    background-color: rgb(83, 83, 83);\n"
"border:none;\n"
"padding:3px;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: tomato;\n"
"}")
        self.close.setText("")
        self.close.setObjectName("close")
        self.horizontalLayout.addWidget(self.close)
        self.verticalLayout.addWidget(self.dragFrame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: #727272;\n"
"color: #fff;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame_5)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.mins = QtWidgets.QSpinBox(self.frame_5)
        self.mins.setStyleSheet("background-color: rgba(148, 148, 148, 102);\n"
"border-radius:3px;\n"
"padding:5px;\n"
"font-size:15px;")
        self.mins.setAlignment(QtCore.Qt.AlignCenter)
        self.mins.setMinimum(1)
        self.mins.setMaximum(60)
        self.mins.setObjectName("mins")
        self.verticalLayout_2.addWidget(self.mins)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stopBtn = QtWidgets.QPushButton(self.frame_6)
        self.stopBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stopBtn.setStyleSheet("QPushButton {\n"
"    image: url(:/imgs/images/24x24/cil-media-stop.png);\n"
"background-color:#ff6f6f;\n"
"padding:5px;\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:#ff4c4c;\n"
"}")
        self.stopBtn.setText("")
        self.stopBtn.setObjectName("stopBtn")
        self.verticalLayout_4.addWidget(self.stopBtn)
        self.startBtn = QtWidgets.QPushButton(self.frame_6)
        self.startBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startBtn.setStyleSheet("QPushButton {\n"
"    image: url(:/imgs/images/24x24/cil-media-play.png);\n"
"background-color: #84c184;\n"
"padding: 5px;\n"
"border-radius: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #66b266;\n"
"}")
        self.startBtn.setText("")
        self.startBtn.setObjectName("startBtn")
        self.verticalLayout_4.addWidget(self.startBtn)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.logUpdate = QtWidgets.QLabel(self.frame_7)
        self.logUpdate.setObjectName("logUpdate")
        self.horizontalLayout_4.addWidget(self.logUpdate, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.keyLoggerLog = QtWidgets.QListWidget(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.keyLoggerLog.setFont(font)
        self.keyLoggerLog.setStyleSheet("background-color: rgba(148, 148, 148, 102);\n"
"border-radius:3px;\n"
"padding:5px;\n"
"font-size: 10px;")
        self.keyLoggerLog.setObjectName("keyLoggerLog")
        self.verticalLayout_5.addWidget(self.keyLoggerLog)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 7)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setStyleSheet("background-color: #727272;\n"
"color: #fff;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scriptIndicator = QtWidgets.QLabel(self.frame_8)
        self.scriptIndicator.setText("")
        self.scriptIndicator.setAlignment(QtCore.Qt.AlignCenter)
        self.scriptIndicator.setObjectName("scriptIndicator")
        self.verticalLayout_6.addWidget(self.scriptIndicator)
        self.verticalLayout.addWidget(self.frame_8)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("QFrame {\n"
"border-bottom-right-radius: 5px;\n"
"border-bottom-left-radius: 5px;\n"
"    background-color: rgb(83, 83, 83);\n"
"color: lightgray;\n"
"font-weight: bold;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setStyleSheet("image: url(:/imgs/images/16x16/cil-heart.png);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.updateTime = QtWidgets.QLabel(self.frame_3)
        self.updateTime.setObjectName("updateTime")
        self.horizontalLayout_2.addWidget(self.updateTime, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "     KeyLogger"))
        self.label_10.setText(_translate("MainWindow", "Save Logs Every x"))
        self.label_3.setText(_translate("MainWindow", "Minute(s)"))
        self.stopBtn.setToolTip(_translate("MainWindow", "Stop Auto Clicker!"))
        self.startBtn.setToolTip(_translate("MainWindow", "Start Auto Clicker!"))
        self.label_2.setText(_translate("MainWindow", "Logs"))
        self.logUpdate.setText(_translate("MainWindow", "Updated: 00:00:00 am"))
        self.label.setText(_translate("MainWindow", "Made With       By Gabe    "))
        self.updateTime.setText(_translate("MainWindow", "00:00:00 am"))
import icons_rc
