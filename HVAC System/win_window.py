# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_win_window(object):
    def setupUi(self, win_window):
        win_window.setObjectName("win_window")
        win_window.resize(663, 440)
        self.centralwidget = QtWidgets.QWidget(win_window)
        self.centralwidget.setObjectName("centralwidget")
        win_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(win_window)
        QtCore.QMetaObject.connectSlotsByName(win_window)

    def retranslateUi(self, win_window):
        _translate = QtCore.QCoreApplication.translate
        win_window.setWindowTitle(_translate("win_window", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win_window = QtWidgets.QMainWindow()
    ui = Ui_win_window()
    ui.setupUi(win_window)
    win_window.show()
    sys.exit(app.exec_())