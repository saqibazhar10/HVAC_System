# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cep.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from cep2 import Ui_door_win
from cep4 import Ui_select_win
from Roof import Ui_Roof
from walls import Ui_walls
from app import Ui_app

class Ui_fst_window(object):
    def setupUi(self, fst_window):
        fst_window.setObjectName("fst_window")
        fst_window.resize(563, 419)
        fst_window.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(41, 48, 54, 255), stop:1 rgba(101, 91, 76, 255));")
        self.centralwidget = QtWidgets.QWidget(fst_window)
        self.centralwidget.setObjectName("centralwidget")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(269, 301, 75, 23))
        self.next.setStyleSheet("background:none;\n"
"color:black;")
        self.next.setObjectName("next")
        self.textcity = QtWidgets.QLabel(self.centralwidget)
        self.textcity.setGeometry(QtCore.QRect(109, 121, 141, 20))
        self.textcity.setStyleSheet("background:none;\n"
"color:white;")
        self.textcity.setObjectName("textcity")
        self.outdoor_temp_max = QtWidgets.QLineEdit(self.centralwidget)
        self.outdoor_temp_max.setGeometry(QtCore.QRect(259, 198, 131, 20))
        self.outdoor_temp_max.setStyleSheet("background:none;\n"
"")
        self.outdoor_temp_max.setText("")
        self.outdoor_temp_max.setObjectName("outdoor_temp_max")
        self.Ambiebt_temp_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Ambiebt_temp_2.setGeometry(QtCore.QRect(259, 161, 131, 20))
        self.Ambiebt_temp_2.setStyleSheet("background:none;\n"
"")
        self.Ambiebt_temp_2.setText("")
        self.Ambiebt_temp_2.setObjectName("Ambiebt_temp_2")
        self.Ambiebt_temp = QtWidgets.QLabel(self.centralwidget)
        self.Ambiebt_temp.setGeometry(QtCore.QRect(98, 161, 141, 20))
        self.Ambiebt_temp.setStyleSheet("background:none;\n"
"color:white;")
        self.Ambiebt_temp.setObjectName("Ambiebt_temp")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(190, 50, 241, 41))
        self.title.setStyleSheet("font: 28pt \"Helvetica\";\n"
"background:none;\n"
"color:white;")
        self.title.setObjectName("title")
        self.Max_temp = QtWidgets.QLabel(self.centralwidget)
        self.Max_temp.setGeometry(QtCore.QRect(76, 197, 181, 20))
        self.Max_temp.setStyleSheet("background:none;\n"
"color:white;")
        self.Max_temp.setObjectName("Max_temp")
        self.city = QtWidgets.QComboBox(self.centralwidget)
        self.city.setGeometry(QtCore.QRect(259, 121, 131, 22))
        self.city.setStyleSheet("background:none;\n"
"")
        self.city.setObjectName("city")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.outdoor_temp_min = QtWidgets.QLineEdit(self.centralwidget)
        self.outdoor_temp_min.setGeometry(QtCore.QRect(260, 260, 131, 20))
        self.outdoor_temp_min.setStyleSheet("background:none;\n"
"")
        self.outdoor_temp_min.setText("")
        self.outdoor_temp_min.setObjectName("outdoor_temp_min")
        self.Min_Temp = QtWidgets.QLabel(self.centralwidget)
        self.Min_Temp.setGeometry(QtCore.QRect(91, 260, 151, 20))
        self.Min_Temp.setStyleSheet("background:none;\n"
"color:white;")
        self.Min_Temp.setObjectName("Min_Temp")
        self.Min_Temp_2 = QtWidgets.QLabel(self.centralwidget)
        self.Min_Temp_2.setGeometry(QtCore.QRect(193, 231, 61, 20))
        self.Min_Temp_2.setStyleSheet("background:none;\n"
"color:white;")
        self.Min_Temp_2.setObjectName("Min_Temp_2")
        self.city_2 = QtWidgets.QComboBox(self.centralwidget)
        self.city_2.setGeometry(QtCore.QRect(259, 231, 131, 22))
        self.city_2.setStyleSheet("background:none;\n"
"")
        self.city_2.setObjectName("city_2")
        self.city_2.addItem("")
        self.city_2.addItem("")
        fst_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(fst_window)
        QtCore.QMetaObject.connectSlotsByName(fst_window)

        
        self.next.clicked.connect(self.nxt)

    def nxt(self):
        self.City = str(self.city.currentText())
        self.ATemp = self.Ambiebt_temp_2.text()
        self.Mtemp = self.outdoor_temp_max.text()
        self.Mintemp= self.outdoor_temp_min.text()

        self.window = QtWidgets.QMainWindow()
        self.window_ui = Ui_select_win()
        self.window_ui.setupUi(self.window)
        self.window.show()
        fst_window.hide()
        self.window_ui.backbutton.clicked.connect(self.back_2)
        self.window_ui.next.clicked.connect(self.nxt1)

    def nxt1(self):
        sel=str(self.window_ui.Selection.currentText())
        if sel=="Door":
            self.window_2 = QtWidgets.QMainWindow()
            self.window_ui_2 = Ui_door_win()
            self.window_ui_2.setupUi(self.window_2)
            self.window_2.show()
            self.window.hide()
            self.window_ui_2.backbutton.clicked.connect(self.back)
            self.window_ui_2.nextpushButton.clicked.connect(self.nxt2)
            

        elif (sel=="Window"):
            self.window_2 = QtWidgets.QMainWindow()
            self.window_ui_2 = Ui_door_win()
            self.window_ui_2.setupUi(self.window_2)
            self.window_ui_2.doortypetext.setText("Windows Type")
            self.window_ui_2.door_text.setText("Window")
            self.window_ui_2.nextpushButton.clicked.connect(self.nxt2)
            self.window_ui_2.backbutton.clicked.connect(self.back)
            self.window_2.show()
            self.window.hide()

        elif (sel=="Roof"):
            self.window_2 = QtWidgets.QMainWindow()
            self.window_ui_2 = Ui_Roof()
            self.window_ui_2.setupUi(self.window_2)
            self.window_2.show()
            self.window_ui_2.backbutton.clicked.connect(self.back)
            self.window.hide()
            self.window_ui_2.next3.clicked.connect(self.nxt3)

        elif(sel=="Walls"):
            self.window_2 = QtWidgets.QMainWindow()
            self.window_ui_2 = Ui_walls()
            self.window_ui_2.setupUi(self.window_2)
            self.window_2.show()
            self.window.hide()
            self.window_ui_2.next3_2.clicked.connect(self.nxt4)
            self.window_ui_2.backbutton.clicked.connect(self.back)

        elif(sel=="Appliances"):
            self.window_2 = QtWidgets.QMainWindow()
            self.window_ui_2 = Ui_app()
            self.window_ui_2.setupUi(self.window_2)
            self.window_2.show()
            self.window.hide()
            self.window_ui_2.backbutton.clicked.connect(self.back)
            self.window_ui_2.cal_1.clicked.connect(self.nxt5_1)
            self.window_ui_2.cal_2.clicked.connect(self.nxt5_2)
            self.window_ui_2.cal_3.clicked.connect(self.nxt5_3)
            self.window_ui_2.cal_4.clicked.connect(self.nxt5_4)
            self.window_ui_2.cal_5.clicked.connect(self.nxt5_5)
            

    def back(self):
        self.window_2.close()
        self.window.show()

    def back_2(self):
        self.window.close()
        fst_window.show()



        


    def nxt4(self):
        self.floor= str(self.window_ui_2.floor_2.currentText())
        self.orient= str(self.window_ui_2.doordropdown_3.currentText())
        length = self.window_ui_2.lng_temp_2.text()
        width = self.window_ui_2.wd_temp_2.text()
        if length=="" or width=="":
            self.window_ui_2.label.setText("Incomplete Data")
        else:
            area= float(length)*float(width)
            u=0.21
            if (self.City =="Karachi" and self.floor =="Ground" ):
                if self.orient =="North":
                    Cltd=11
                elif self.orient =="East":
                    Cltd =29
                elif self.orient =="South":
                    Cltd =8
                else:
                    Cltd =10
            elif ((self.City =="Dir" or self.City =="Chitral") and self.floor =="Ground"):
                if self.orient =="North":
                    Cltd=10
                elif self.orient =="East":
                    Cltd =35
                elif self.orient =="South":
                    Cltd =12
                else:
                    Cltd =10
            elif ((self.City =="Dir" or self.City =="Chitral") and self.floor =="First"):
                if self.orient =="North":
                    Cltd=10
                elif self.orient =="East":
                    Cltd =0
                elif self.orient =="South":
                    Cltd =12
                else:
                    Cltd =10

            elif (self.City =="Karachi" and self.floor =="First"):
                if self.orient =="North":
                    Cltd=10
                elif self.orient =="East":
                    Cltd =0
                elif self.orient =="South":
                    Cltd =12
                else:
                    Cltd =10
            if (self.City =="Karachi"):
                Tm= 99.4
            elif (self.City=="Dir"):
                Tm= 79.6
            else:
                Tm = 88.6

            Cltd = Cltd + (78-78.6) + (Tm-85)
            final = u*area*Cltd
            self.window_ui_2.rl_2.setText(str(round(final,3)))

        
    def nxt3(self):
        self.floor= str(self.window_ui_2.floor.currentText())
        length = self.window_ui_2.lng_temp_1.text()
        width = self.window_ui_2.wd_temp_1.text()
        if length=="" or width=="":
            self.window_ui_2.label_2.setText("Incomplete Data")
        else:
            area= float(length)*float(width)
            if (self.City =="Karachi" ):
                if self.floor=="Ground" :
                    u= 1.96
                    cldt1 =64.0
                elif self.floor=="First":
                    u= 1.96
                    cldt1 =75.8
            elif self.City=="Dir":
                if self.floor=="Ground":
                        u= 1.96
                        cldt1 =63.0
                elif self.floor=="First":
                        u= 1.96
                        cldt1 =56.8
            elif self.City=="Chitral":
                if self.floor=="Ground":
                        u= 1.96
                        cldt1 =63.0
                elif self.floor=="First":
                        u= 1.96
                        cldt1 =65.8

            load= u*area*cldt1
            self.window_ui_2.rl.setText(str(load))

    def nxt2(self):
        self.door_type= str(self.window_ui_2.doordropdown.currentText())
        self.floor= str(self.window_ui_2.floor.currentText())
        self.orient= str(self.window_ui_2.ortationdrop_1.currentText())
        length = self.window_ui_2.lng_temp_1.text()
        width = self.window_ui_2.wd_temp_1.text()
        if length=="" or width=="":
            self.window_ui_2.label_3.setText("Incomplete Data")
        else:

            area= float(length)*float(width)
            if (self.City =="Karachi" or self.City=="Dir" or self.City=="Chitral"):
                if self.floor=="Ground" and self.door_type=="Single Pane":
                    u= 4.60
                    sc= 0.5
                    cldt1 =52.8
                elif (self.floor=="First" and self.door_type=="Single Pane"):
                    u= 5.91
                    sc= 1.0
                    cldt1 =52.8
                elif (self.floor=="First" and self.door_type=="Double Pane"):
                    u= 4.60
                    sc= 0.5
                    cldt1 =52.8
                elif self.floor=="Ground" and self.door_type=="Double Pane":
                    u= 3.12
                    sc= 0.45
                    cldt1 =52.8
            
            if (self.City=="Karachi"):
                if self.orient =="North":
                    scl=52.8
                if self.orient =="South":
                    scl=2
                if self.orient =="East":
                    scl=62
                if self.orient =="West":
                    scl=4
                
            if (self.City =="Dir"):

                if self.orient =="North":
                    scl=5
                if self.orient =="South":
                    scl=4
                if self.orient =="East":
                    scl=3
                if self.orient =="West":
                    scl=2

            if (self.City =="Chitral"):
                if self.orient =="North":
                    scl=50
                if self.orient =="South":
                    scl=40
                if self.orient =="East":
                    scl=30
                if self.orient =="West":
                    scl=20

            load= u*area*cldt1
            self.window_ui_2.cl.setText(str(round(load,3)))
            load= sc*area*scl
            self.window_ui_2.rl.setText(str(round(load,3)))

    def nxt5_1(self):
        self.people= str(self.window_ui_2.people.text())
        if self.people == "":
            self.window_ui_2.incdata.setText("Incomplete Data!")
        else:
            qs= int(self.people)*75*0.96
            ql= int(self.people)*55
            self.window_ui_2.rl.setText(str(round(qs,3)))
            self.window_ui_2.rl_2.setText(str(round(ql,3)))

    def nxt5_2(self):
        self.watt= str(self.window_ui_2.watt.text())
        if self.watt == "":
            self.window_ui_2.incdata.setText("Incomplete Data!")
        else:
            q =3.41*(int(self.watt))*1*1.2*0.95
            self.window_ui_2.rl_3.setText(str(round(q,3)))

    def nxt5_3(self):
        qs =780
        self.window_ui_2.rl_5.setText(str(round(qs,3)))
        ql=520
        self.window_ui_2.rl_4.setText(str(round(ql,3)))
    
    def nxt5_4(self):
        qs =1340
        self.window_ui_2.rl_7.setText(str(round(qs,3)))
        ql=520
        self.window_ui_2.rl_6.setText(str(round(ql,3)))


    def nxt5_5(self):
        qs =187.2
        self.window_ui_2.rl_9.setText(str(round(qs,3)))







    def retranslateUi(self, fst_window):
        _translate = QtCore.QCoreApplication.translate
        fst_window.setWindowTitle(_translate("fst_window", "MainWindow"))
        self.next.setText(_translate("fst_window", "NEXT"))
        self.textcity.setText(_translate("fst_window", "Please Select your city"))
        self.Ambiebt_temp.setText(_translate("fst_window", "Ambient Temperature C"))
        self.title.setText(_translate("fst_window", "WEC CLTD"))
        self.Max_temp.setText(_translate("fst_window", "Max outdoor Temperature C"))
        self.city.setItemText(0, _translate("fst_window", "Karachi"))
        self.city.setItemText(1, _translate("fst_window", "Dir"))
        self.city.setItemText(2, _translate("fst_window", "Chitral"))
        self.Min_Temp.setText(_translate("fst_window", "Min outdoor Temperature C"))
        self.Min_Temp_2.setText(_translate("fst_window", "Latitude"))
        self.city_2.setItemText(0, _translate("fst_window", "24 degree North"))
        self.city_2.setItemText(1, _translate("fst_window", "36 degree North "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fst_window = QtWidgets.QMainWindow()
    ui = Ui_fst_window()
    ui.setupUi(fst_window)
    fst_window.show()
    sys.exit(app.exec_())
