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
        except BaseException:
            pass

    def st_Dex_Calc(self):
        pass

    def st_Con_Calc(self):
        pass

    def st_Int_Calc(self):
        pass

    def st_Wis_Calc(self):
        pass

    def st_Cha_Calc(self):
        pass
god = God()

MainWindow.show()
sys.exit(app.exec_())
