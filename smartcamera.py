# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smartcamera.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SmartCamera(object):
    def setupUi(self, SmartCamera):
        SmartCamera.setObjectName("SmartCamera")
        SmartCamera.resize(595, 482)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 152, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 152, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 152, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        SmartCamera.setPalette(palette)
        self.Addnewmember = QtWidgets.QPushButton(SmartCamera)
        self.Addnewmember.setGeometry(QtCore.QRect(180, 160, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.Addnewmember.setFont(font)
        self.Addnewmember.setAutoFillBackground(True)
        self.Addnewmember.setObjectName("Addnewmember")
        self.activate = QtWidgets.QPushButton(SmartCamera)
        self.activate.setGeometry(QtCore.QRect(180, 260, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.activate.setFont(font)
        self.activate.setAutoFillBackground(True)
        self.activate.setObjectName("activate")
        self.label = QtWidgets.QLabel(SmartCamera)
        self.label.setGeometry(QtCore.QRect(220, 60, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(SmartCamera)
        QtCore.QMetaObject.connectSlotsByName(SmartCamera)

    def retranslateUi(self, SmartCamera):
        _translate = QtCore.QCoreApplication.translate
        SmartCamera.setWindowTitle(_translate("SmartCamera", "Dialog"))
        self.Addnewmember.setText(_translate("SmartCamera", "Add New Member"))
        self.activate.setText(_translate("SmartCamera", "Activate Smart Camera"))
        self.label.setText(_translate("SmartCamera", "WELCOME!!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SmartCamera = QtWidgets.QDialog()
    ui = Ui_SmartCamera()
    ui.setupUi(SmartCamera)
    SmartCamera.show()
    sys.exit(app.exec_())
