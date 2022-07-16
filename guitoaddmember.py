# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addnewgui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gettext import gettext
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import cv2
import os
flag=0
name="name"
img_name="d"

class Ui_MainWindow(object):
    def capture(self):
            print("Clicking Image!!")
            cam=cv2.VideoCapture(0)
            #cv2.namedWindow("Python Webcam")
            img_counter=0
            flag=0
            while flag==0:
                ret,frame=cam.read()

                if not ret:
                  print("Failed")
                  break

                cv2.imshow("test",frame)
                k=cv2.waitKey(1) 
                #if k%256 == 27: 
                 # print("Escape Hit!!Closing")
                  #break

                if k%256 == 32:
                  self.tname=self.namebutton.text()
                  img_name = "owners//"+self.tname + '.png'
                  #'C:/Users/HP/Desktop/'+
                  print(img_name)
                  cv2.imwrite(img_name,frame)
                  print("Picture taken")
                  cv2.imshow(img_name,frame)
                  #self.retake()
                  #break
                  #img_counter+=1
                  flag=flag+1

            cam.release()

            cv2.destroyWindow("test")

    def retakepic(self):
            self.capture()
    def savepic(self):
        #cv2.destroyWindow("opencv_frame_0.png")
                print("Saved")
                cv2.destroyAllWindows()
                quit()
    #    name=self.namefield.text()
     #   name2=".png"
      #  name3= " ".join([name,name2])
        #cv2.imwrite(name3,name3)
       # os. rename(img_name,name3) 
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 691)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(106, 164, 176);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 30, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 20, 91, 91))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("iconsforgui\\add.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.namebutton = QtWidgets.QLineEdit(self.centralwidget)
        self.namebutton.setGeometry(QtCore.QRect(520, 160, 191, 61))
        self.namebutton.setStyleSheet("background-color: rgb(46, 139, 192);\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(177, 212, 224);")
        self.namebutton.setText("")
        self.namebutton.setObjectName("namebutton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 170, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.captureimagebutton = QtWidgets.QPushButton(self.centralwidget)
        self.captureimagebutton.setGeometry(QtCore.QRect(430, 270, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.captureimagebutton.setFont(font)
        self.captureimagebutton.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.895522 rgba(32, 99, 119, 255));")
        self.captureimagebutton.setText("Capture Image")
        self.captureimagebutton.setObjectName("captureimagebutton")
        self.captureimagebutton.clicked.connect(self.capture)

        
        self.retake = QtWidgets.QPushButton(self.centralwidget)
        self.retake.setGeometry(QtCore.QRect(430, 360, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.retake.setFont(font)
        self.retake.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:0.895522 rgba(32, 99, 119, 255));\n"
"")
        self.retake.setObjectName("retake")
        self.retake.clicked.connect(self.retakepic)

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(440, 460, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.179104 rgba(43, 69, 96, 255), stop:0.890547 rgba(107, 116, 119, 255));\n"
"color: rgb(0, 0, 0);\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconsforgui\\save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon)
        self.save.setIconSize(QtCore.QSize(60, 60))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.savepic)
        self.image1 = QtWidgets.QLabel(self.centralwidget)
        self.image1.setGeometry(QtCore.QRect(70, 150, 241, 241))
        self.image1.setText("")
        self.image1.setPixmap(QtGui.QPixmap("iconsforgui\\images1.png"))
        self.image1.setScaledContents(True)
        self.image1.setObjectName("image1")
        self.image2 = QtWidgets.QLabel(self.centralwidget)
        self.image2.setGeometry(QtCore.QRect(750, 160, 251, 231))
        self.image2.setText("")
        self.image2.setPixmap(QtGui.QPixmap("iconsforgui\\images.png"))
        self.image2.setScaledContents(True)
        self.image2.setObjectName("image2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">      Add New Member!!</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Enter name </span></p></body></html>"))
        self.retake.setText(_translate("MainWindow", "Retake"))
        self.save.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())