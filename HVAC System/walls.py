# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'walls.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_walls(object):
    def setupUi(self, walls):
        walls.setObjectName("walls")
        walls.resize(723, 470)
        walls.setMinimumSize(QtCore.QSize(723, 470))
        walls.setMaximumSize(QtCore.QSize(723, 470))
        walls.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(41, 48, 54, 255), stop:1 rgba(101, 91, 76, 255));")
        self.centralwidget = QtWidgets.QWidget(walls)
        self.centralwidget.setObjectName("centralwidget")
        self.door_text_2 = QtWidgets.QLabel(self.centralwidget)
        self.door_text_2.setGeometry(QtCore.QRect(270, 180, 121, 20))
        self.door_text_2.setStyleSheet("background:none;\n"
"font: 12pt \"Tahoma\";\n"
"color:white;")
        self.door_text_2.setObjectName("door_text_2")
        self.lng_temp_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lng_temp_2.setGeometry(QtCore.QRect(270, 270, 131, 20))
        self.lng_temp_2.setStyleSheet("background:none;\n"
"font:  \"Tahoma\";\n"
"color:black;")
        self.lng_temp_2.setObjectName("lng_temp_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 380, 161, 16))
        self.label_2.setStyleSheet("background:none;\n"
"font: 8pt \"Tahoma\";\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.doordropdown_3 = QtWidgets.QComboBox(self.centralwidget)
        self.doordropdown_3.setGeometry(QtCore.QRect(270, 210, 131, 22))
        self.doordropdown_3.setStyleSheet("background:none;\n"
"font:  \"Tahoma\";\n"
"color:black;")
        self.doordropdown_3.setObjectName("doordropdown_3")
        self.doordropdown_3.addItem("")
        self.doordropdown_3.addItem("")
        self.doordropdown_3.addItem("")
        self.doordropdown_3.addItem("")
        self.textortation_3 = QtWidgets.QLabel(self.centralwidget)
        self.textortation_3.setGeometry(QtCore.QRect(480, 170, 61, 20))
        self.textortation_3.setStyleSheet("background:none;\n"
"font: 12pt \"Tahoma\";\n"
"color:white;")
        self.textortation_3.setObjectName("textortation_3")
        self.floor_2 = QtWidgets.QComboBox(self.centralwidget)
        self.floor_2.setGeometry(QtCore.QRect(480, 210, 81, 22))
        self.floor_2.setStyleSheet("background:none;\n"
"font:  \"Tahoma\";\n"
"color:black;")
        self.floor_2.setObjectName("floor_2")
        self.floor_2.addItem("")
        self.floor_2.addItem("")
        self.lenghttext_2 = QtWidgets.QLabel(self.centralwidget)
        self.lenghttext_2.setGeometry(QtCore.QRect(150, 260, 111, 31))
        self.lenghttext_2.setStyleSheet("background:none;\n"
"font: 12pt \"Tahoma\";\n"
"color:white;")
        self.lenghttext_2.setObjectName("lenghttext_2")
        self.rl_2 = QtWidgets.QLabel(self.centralwidget)
        self.rl_2.setGeometry(QtCore.QRect(340, 380, 55, 16))
        self.rl_2.setStyleSheet("background:none;\n"
"font: 8pt \"Tahoma\";\n"
"color:white;")
        self.rl_2.setObjectName("rl_2")
        self.next3_2 = QtWidgets.QPushButton(self.centralwidget)
        self.next3_2.setGeometry(QtCore.QRect(540, 410, 91, 23))
        self.next3_2.setStyleSheet("background:none;\n"
"font:  \"Tahoma\";\n"
"color:black;")
        self.next3_2.setObjectName("next3_2")
        self.widthtext_2 = QtWidgets.QLabel(self.centralwidget)
        self.widthtext_2.setGeometry(QtCore.QRect(150, 310, 91, 21))
        self.widthtext_2.setStyleSheet("background:none;\n"
"font: 12pt \"Tahoma\";\n"
"color:white;")
        self.widthtext_2.setObjectName("widthtext_2")
        self.wd_temp_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.wd_temp_2.setGeometry(QtCore.QRect(270, 310, 131, 20))
        self.wd_temp_2.setStyleSheet("background:none;\n"
"font:  \"Tahoma\";\n"
"color:black;")
        self.wd_temp_2.setObjectName("wd_temp_2")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(260, 50, 241, 71))
        self.title.setStyleSheet("background:none;\n"
"font: 28pt \"Tahoma\";\n"
"color:white;")
        self.title.setObjectName("title")
        self.backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(30, 50, 91, 23))
        self.backbutton.setStyleSheet("background:none;\n"
"font:  \"Tahoma\";\n"
"color:black;")
        self.backbutton.setObjectName("backbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 150, 111, 31))
        self.label.setStyleSheet("background:none;\n"
"font: 8pt \"Tahoma\";\n"
"color:white;")
        self.label.setObjectName("label")
        walls.setCentralWidget(self.centralwidget)

        self.retranslateUi(walls)
        QtCore.QMetaObject.connectSlotsByName(walls)

    def retranslateUi(self, walls):
        _translate = QtCore.QCoreApplication.translate
        walls.setWindowTitle(_translate("walls", "MainWindow"))
        self.door_text_2.setText(_translate("walls", "Orientation"))
        self.label_2.setText(_translate("walls", "The total Radiation load is "))
        self.doordropdown_3.setItemText(0, _translate("walls", "North"))
        self.doordropdown_3.setItemText(1, _translate("walls", "South"))
        self.doordropdown_3.setItemText(2, _translate("walls", "East"))
        self.doordropdown_3.setItemText(3, _translate("walls", "West"))
        self.textortation_3.setText(_translate("walls", "Floor"))
        self.floor_2.setItemText(0, _translate("walls", "Ground"))
        self.floor_2.setItemText(1, _translate("walls", "First"))
        self.lenghttext_2.setText(_translate("walls", "Length(ft)"))
        self.rl_2.setText(_translate("walls", ""))
        self.next3_2.setText(_translate("walls", "NEXT"))
        self.widthtext_2.setText(_translate("walls", "Width (ft)"))
        self.title.setText(_translate("walls", "HVAC CEP"))
        self.backbutton.setText(_translate("walls", "back"))
        self.label.setText(_translate("walls", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    walls = QtWidgets.QMainWindow()
    ui = Ui_walls()
    ui.setupUi(walls)
    walls.show()
    sys.exit(app.exec_())
