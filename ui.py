# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui',
# licensing of 'untitled.ui' applies.
#
# Created: Thu Oct 14 04:38:23 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 241, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 50, 133, 144))
        self.groupBox_11.setObjectName("groupBox_11")
        self.st_str_origin = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_str_origin.setGeometry(QtCore.QRect(35, 14, 22, 20))
        self.st_str_origin.setMaxLength(2)
        self.st_str_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.st_str_origin.setObjectName("st_str_origin")
        self.st_str_mod = QtWidgets.QLabel(self.groupBox_11)
        self.st_str_mod.setGeometry(QtCore.QRect(107, 14, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_str_mod.setFont(font)
        self.st_str_mod.setFrameShape(QtWidgets.QFrame.Box)
        self.st_str_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.st_str_mod.setObjectName("st_str_mod")
        self.st_str_misc = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_str_misc.setGeometry(QtCore.QRect(59, 14, 22, 20))
        self.st_str_misc.setMaxLength(2)
        self.st_str_misc.setAlignment(QtCore.Qt.AlignCenter)
        self.st_str_misc.setObjectName("st_str_misc")
        self.st_str_all = QtWidgets.QLabel(self.groupBox_11)
        self.st_str_all.setGeometry(QtCore.QRect(83, 14, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_str_all.setFont(font)
        self.st_str_all.setFrameShape(QtWidgets.QFrame.Box)
        self.st_str_all.setAlignment(QtCore.Qt.AlignCenter)
        self.st_str_all.setObjectName("st_str_all")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_7.setGeometry(QtCore.QRect(2, 34, 32, 22))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_13.setGeometry(QtCore.QRect(2, 13, 32, 22))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_14.setGeometry(QtCore.QRect(2, 55, 32, 22))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_15.setGeometry(QtCore.QRect(2, 76, 32, 22))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_16.setGeometry(QtCore.QRect(2, 97, 32, 22))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_17.setGeometry(QtCore.QRect(2, 118, 32, 22))
        self.pushButton_17.setObjectName("pushButton_17")
        self.st_dex_misc = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_dex_misc.setGeometry(QtCore.QRect(59, 35, 22, 20))
        self.st_dex_misc.setMaxLength(2)
        self.st_dex_misc.setAlignment(QtCore.Qt.AlignCenter)
        self.st_dex_misc.setObjectName("st_dex_misc")
        self.st_dex_all = QtWidgets.QLabel(self.groupBox_11)
        self.st_dex_all.setGeometry(QtCore.QRect(83, 35, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_dex_all.setFont(font)
        self.st_dex_all.setFrameShape(QtWidgets.QFrame.Box)
        self.st_dex_all.setAlignment(QtCore.Qt.AlignCenter)
        self.st_dex_all.setObjectName("st_dex_all")
        self.st_dex_origin = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_dex_origin.setGeometry(QtCore.QRect(35, 35, 22, 20))
        self.st_dex_origin.setMaxLength(2)
        self.st_dex_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.st_dex_origin.setObjectName("st_dex_origin")
        self.st_dex_mod = QtWidgets.QLabel(self.groupBox_11)
        self.st_dex_mod.setGeometry(QtCore.QRect(107, 35, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_dex_mod.setFont(font)
        self.st_dex_mod.setFrameShape(QtWidgets.QFrame.Box)
        self.st_dex_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.st_dex_mod.setObjectName("st_dex_mod")
        self.st_con_misc = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_con_misc.setGeometry(QtCore.QRect(59, 56, 22, 20))
        self.st_con_misc.setMaxLength(2)
        self.st_con_misc.setAlignment(QtCore.Qt.AlignCenter)
        self.st_con_misc.setObjectName("st_con_misc")
        self.st_con_all = QtWidgets.QLabel(self.groupBox_11)
        self.st_con_all.setGeometry(QtCore.QRect(83, 56, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_con_all.setFont(font)
        self.st_con_all.setFrameShape(QtWidgets.QFrame.Box)
        self.st_con_all.setAlignment(QtCore.Qt.AlignCenter)
        self.st_con_all.setObjectName("st_con_all")
        self.st_con_origin = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_con_origin.setGeometry(QtCore.QRect(35, 56, 22, 20))
        self.st_con_origin.setMaxLength(2)
        self.st_con_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.st_con_origin.setObjectName("st_con_origin")
        self.st_con_mod = QtWidgets.QLabel(self.groupBox_11)
        self.st_con_mod.setGeometry(QtCore.QRect(107, 56, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_con_mod.setFont(font)
        self.st_con_mod.setFrameShape(QtWidgets.QFrame.Box)
        self.st_con_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.st_con_mod.setObjectName("st_con_mod")
        self.st_int_misc = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_int_misc.setGeometry(QtCore.QRect(59, 77, 22, 20))
        self.st_int_misc.setMaxLength(2)
        self.st_int_misc.setAlignment(QtCore.Qt.AlignCenter)
        self.st_int_misc.setObjectName("st_int_misc")
        self.st_int_all = QtWidgets.QLabel(self.groupBox_11)
        self.st_int_all.setGeometry(QtCore.QRect(83, 77, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_int_all.setFont(font)
        self.st_int_all.setFrameShape(QtWidgets.QFrame.Box)
        self.st_int_all.setAlignment(QtCore.Qt.AlignCenter)
        self.st_int_all.setObjectName("st_int_all")
        self.st_int_origin = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_int_origin.setGeometry(QtCore.QRect(35, 77, 22, 20))
        self.st_int_origin.setMaxLength(2)
        self.st_int_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.st_int_origin.setObjectName("st_int_origin")
        self.st_int_mod = QtWidgets.QLabel(self.groupBox_11)
        self.st_int_mod.setGeometry(QtCore.QRect(107, 77, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_int_mod.setFont(font)
        self.st_int_mod.setFrameShape(QtWidgets.QFrame.Box)
        self.st_int_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.st_int_mod.setObjectName("st_int_mod")
        self.st_wis_misc = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_wis_misc.setGeometry(QtCore.QRect(59, 98, 22, 20))
        self.st_wis_misc.setMaxLength(2)
        self.st_wis_misc.setAlignment(QtCore.Qt.AlignCenter)
        self.st_wis_misc.setObjectName("st_wis_misc")
        self.st_wis_all = QtWidgets.QLabel(self.groupBox_11)
        self.st_wis_all.setGeometry(QtCore.QRect(83, 98, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_wis_all.setFont(font)
        self.st_wis_all.setFrameShape(QtWidgets.QFrame.Box)
        self.st_wis_all.setAlignment(QtCore.Qt.AlignCenter)
        self.st_wis_all.setObjectName("st_wis_all")
        self.st_wis_origin = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_wis_origin.setGeometry(QtCore.QRect(35, 98, 22, 20))
        self.st_wis_origin.setMaxLength(2)
        self.st_wis_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.st_wis_origin.setObjectName("st_wis_origin")
        self.st_wis_mod = QtWidgets.QLabel(self.groupBox_11)
        self.st_wis_mod.setGeometry(QtCore.QRect(107, 98, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_wis_mod.setFont(font)
        self.st_wis_mod.setFrameShape(QtWidgets.QFrame.Box)
        self.st_wis_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.st_wis_mod.setObjectName("st_wis_mod")
        self.st_cha_misc = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_cha_misc.setGeometry(QtCore.QRect(59, 119, 22, 20))
        self.st_cha_misc.setMaxLength(2)
        self.st_cha_misc.setAlignment(QtCore.Qt.AlignCenter)
        self.st_cha_misc.setObjectName("st_cha_misc")
        self.st_cha_all = QtWidgets.QLabel(self.groupBox_11)
        self.st_cha_all.setGeometry(QtCore.QRect(83, 119, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_cha_all.setFont(font)
        self.st_cha_all.setFrameShape(QtWidgets.QFrame.Box)
        self.st_cha_all.setAlignment(QtCore.Qt.AlignCenter)
        self.st_cha_all.setObjectName("st_cha_all")
        self.st_cha_origin = QtWidgets.QLineEdit(self.groupBox_11)
        self.st_cha_origin.setGeometry(QtCore.QRect(35, 119, 22, 20))
        self.st_cha_origin.setMaxLength(2)
        self.st_cha_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.st_cha_origin.setObjectName("st_cha_origin")
        self.st_cha_mod = QtWidgets.QLabel(self.groupBox_11)
        self.st_cha_mod.setGeometry(QtCore.QRect(107, 119, 22, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(75)
        font.setBold(True)
        self.st_cha_mod.setFont(font)
        self.st_cha_mod.setFrameShape(QtWidgets.QFrame.Box)
        self.st_cha_mod.setAlignment(QtCore.Qt.AlignCenter)
        self.st_cha_mod.setObjectName("st_cha_mod")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 470, 401, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 181, 21))
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "Имя Персонажа", None, -1))
        self.groupBox_11.setTitle(QtWidgets.QApplication.translate("MainWindow", "Статы", None, -1))
        self.st_str_origin.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_str_mod.setText(QtWidgets.QApplication.translate("MainWindow", "-1", None, -1))
        self.st_str_misc.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.st_str_all.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Итоговый стат:</span> 8 + 0 = 8<br/><span style=\" font-weight:600;\">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>", None, -1))
        self.st_str_all.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.pushButton_7.setText(QtWidgets.QApplication.translate("MainWindow", "ЛОВ", None, -1))
        self.pushButton_13.setText(QtWidgets.QApplication.translate("MainWindow", "СИЛ", None, -1))
        self.pushButton_14.setText(QtWidgets.QApplication.translate("MainWindow", "ВЫН", None, -1))
        self.pushButton_15.setText(QtWidgets.QApplication.translate("MainWindow", "ИНТ", None, -1))
        self.pushButton_16.setText(QtWidgets.QApplication.translate("MainWindow", "МУД", None, -1))
        self.pushButton_17.setText(QtWidgets.QApplication.translate("MainWindow", "ХАР", None, -1))
        self.st_dex_misc.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.st_dex_all.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_dex_origin.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_dex_mod.setText(QtWidgets.QApplication.translate("MainWindow", "-1", None, -1))
        self.st_con_misc.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.st_con_all.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_con_origin.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_con_mod.setText(QtWidgets.QApplication.translate("MainWindow", "-1", None, -1))
        self.st_int_misc.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.st_int_all.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_int_origin.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_int_mod.setText(QtWidgets.QApplication.translate("MainWindow", "-1", None, -1))
        self.st_wis_misc.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.st_wis_all.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_wis_origin.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_wis_mod.setText(QtWidgets.QApplication.translate("MainWindow", "-1", None, -1))
        self.st_cha_misc.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.st_cha_all.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_cha_origin.setText(QtWidgets.QApplication.translate("MainWindow", "8", None, -1))
        self.st_cha_mod.setText(QtWidgets.QApplication.translate("MainWindow", "-1", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Панель с временным говном", None, -1))
        self.label_5.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Итоговый стат:</span> 8 + 0 = 8<br/><span style=\" font-weight:600;\">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Тест описаний.", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Файл", None, -1))
        self.action_2.setText(QtWidgets.QApplication.translate("MainWindow", "Открыть", None, -1))
        self.action_3.setText(QtWidgets.QApplication.translate("MainWindow", "Создать", None, -1))
        self.action_4.setText(QtWidgets.QApplication.translate("MainWindow", "Сохранить", None, -1))
        self.action_5.setText(QtWidgets.QApplication.translate("MainWindow", "Удалить", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

