import sys
from PySide2 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

class God:
    def __init__(self):
        self.ui = ui

        self.help = {
            1:-5,
            2:-4,
            3:-4,
            4:-3,
            5:-3,
            6:-2,
            7:-2,
            8:-1,
            9:-1,
            10:0,
            11:0,
            12:1,
            13:1,
            14:2,
            15:2,
            16:3,
            17:3,
            18:4,
            19:4,
            20:5,
            21:5,
            22:6,
            23:6,
            24:7,
            25:7,
            26:8,
            27:8,
            28:9,
            29:9,
            30:10,
            31:10,
        }
        self.toolTip = {
            'str':lambda: self.ui.st_str_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.ui.st_str_origin.text()} + {self.ui.st_str_misc.text()} = {self.ui.st_str_all.text()}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
            'dex':lambda: self.ui.st_dex_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.ui.st_dex_origin.text()} + {self.ui.st_dex_misc.text()} = {self.ui.st_dex_all.text()}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
            'con':lambda: self.ui.st_con_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.ui.st_con_origin.text()} + {self.ui.st_con_misc.text()} = {self.ui.st_con_all.text()}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
            'int':lambda: self.ui.st_int_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.ui.st_int_origin.text()} + {self.ui.st_int_misc.text()} = {self.ui.st_int_all.text()}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
            'wis':lambda: self.ui.st_wis_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.ui.st_wis_origin.text()} + {self.ui.st_wis_misc.text()} = {self.ui.st_wis_all.text()}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
            'cha':lambda: self.ui.st_cha_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.ui.st_cha_origin.text()} + {self.ui.st_cha_misc.text()} = {self.ui.st_cha_all.text()}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
            }
        # --- Connect ---
        self.ui.st_str_origin.textChanged.connect(self.st_Str_Calc)
        self.ui.st_str_misc.textChanged.connect(self.st_Str_Calc)
        self.ui.st_dex_origin.textChanged.connect(self.st_Dex_Calc)
        self.ui.st_dex_misc.textChanged.connect(self.st_Dex_Calc)
        self.ui.st_con_origin.textChanged.connect(self.st_Con_Calc)
        self.ui.st_con_misc.textChanged.connect(self.st_Con_Calc)
        self.ui.st_int_origin.textChanged.connect(self.st_Int_Calc)
        self.ui.st_int_misc.textChanged.connect(self.st_Int_Calc)
        self.ui.st_wis_origin.textChanged.connect(self.st_Wis_Calc)
        self.ui.st_wis_misc.textChanged.connect(self.st_Wis_Calc)
        self.ui.st_cha_origin.textChanged.connect(self.st_Cha_Calc)
        self.ui.st_cha_misc.textChanged.connect(self.st_Cha_Calc)

    def st_Str_Calc(self):
        try:
            self.ui.st_str_all.setText(
                str(int(self.ui.st_str_origin.text()) + int(self.ui.st_str_misc.text()))
                )
            self.ui.st_str_mod.setText(str(self.help[int(self.ui.st_str_all.text())]))
            self.toolTip['str']()
        except BaseException:
            pass

    def st_Dex_Calc(self):
        try:
            self.ui.st_dex_all.setText(
                str(int(self.ui.st_dex_origin.text()) + int(self.ui.st_dex_misc.text()))
                )
            self.ui.st_dex_mod.setText(str(self.help[int(self.ui.st_dex_all.text())]))
            self.toolTip['dex']()
        except BaseException:
            pass
        pass

    def st_Con_Calc(self):
        try:
            self.ui.st_con_all.setText(
                str(int(self.ui.st_con_origin.text()) + int(self.ui.st_con_misc.text()))
                )
            self.ui.st_con_mod.setText(str(self.help[int(self.ui.st_con_all.text())]))
            self.toolTip['con']()
        except BaseException:
            pass
        pass

    def st_Int_Calc(self):
        try:
            self.ui.st_int_all.setText(
                str(int(self.ui.st_int_origin.text()) + int(self.ui.st_int_misc.text()))
                )
            self.ui.st_int_mod.setText(str(self.help[int(self.ui.st_sintall.text())]))
            self.toolTip['int']()
        except BaseException:
            pass
        pass

    def st_Wis_Calc(self):
        try:
            self.ui.st_wis_all.setText(
                str(int(self.ui.st_wis_origin.text()) + int(self.ui.wisstr_misc.text()))
                )
            self.ui.st_wis_mod.setText(str(self.help[int(self.ui.st_wis_all.text())]))
            self.toolTip['wis']()
        except BaseException:
            pass
        pass

    def st_Cha_Calc(self):
        try:
            self.ui.st_cha_all.setText(
                str(int(self.ui.st_cha_origin.text()) + int(self.ui.st_cha_misc.text()))
                )
            self.ui.st_cha_mod.setText(str(self.help[int(self.ui.st_cha_all.text())]))
            self.toolTip['cha']()
        except BaseException:
            pass
        pass
god = God()

MainWindow.show()
sys.exit(app.exec_())
