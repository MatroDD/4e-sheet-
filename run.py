# --- Импорты ---
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
import cls

# --- Инициализация графического окна ---
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

# --- Создания базовых классов ---
class Sheet:
    def __init__(self):
        self.ui = ui # Файл интерфейса

        # Словарь с костылём для подсчёта модификатора статов
        self.help = {
            1:-5, 2:-4, 3:-4, 4:-3, 5:-3, 6:-2, 7:-2, 8:-1, 9:-1, 10:0,
            11:0, 12:1, 13:1, 14:2, 15:2, 16:3, 17:3, 18:4, 19:4, 20:5,
            21:5, 22:6, 23:6, 24:7, 25:7, 26:8, 27:8, 28:9, 29:9, 30:10, 31:10}

        self.lvl = int(self.ui.lvl.text())
        # Создаём классы атрибутов
        self.st_str = cls.Str(self)
        self.st_dex = cls.Dex(self)
        self.st_con = cls.Con(self)
        self.st_int = cls.Int(self)
        self.st_wis = cls.Wis(self)
        self.st_cha = cls.Cha(self)

        # Создаём классы навыков
        self.sk_acr = cls.sk_Acr(self)
        self.sk_arc = cls.sk_Arc(self)
        self.sk_athl = cls.sk_Athl(self)
        self.sk_bluff = cls.sk_Bluff(self)
        self.sk_dipl = cls.sk_Dipl(self)
        self.sk_dung = cls.sk_Dung(self)
        self.sk_end = cls.sk_End(self)
        self.sk_heal = cls.sk_Heal(self)
        self.sk_hist = cls.sk_Hist(self)
        self.sk_ins = cls.sk_Ins(self)
        self.sk_int = cls.sk_Int(self)
        self.sk_nat = cls.sk_Nat(self)
        self.sk_perc = cls.sk_Perc(self)
        self.sk_rel = cls.sk_Rel(self)
        self.sk_stealth = cls.sk_Stealth(self)
        self.sk_street = cls.sk_Street(self)
        self.sk_thief = cls.sk_Thief(self)

        # --- Connect ---
        # Добавляем к полям ввода статов и модификаторов событие "если изменён текст"
        # Тут же привязываем это событие к функции

        self.ui.max_HP.textChanged.connect(self.misc_HP_Calc)
        self.ui.current_HP.textChanged.connect(self.misc_HP_Calc)
        # --- Костыле-инициализация ---

        self.ui.max_HP.setText('0')
        self.misc_HP_Calc()

# Попытка в подсчёт показателей здоровья
    def misc_HP_Calc(self):
        try:
            self.ui.bloodied.setText(
                str(int(self.max_HP.text()) / int(2))
                )
        except BaseException:
            pass
        pass


# Созадём основной класс для взаимосвязи приложения
sheet = Sheet()

# Показыаем окно и запускаем цикл.
# После sys.exit(app.exec_()) никакой код писать нельзя
# он выполнится ТОЛЬКО когда мы ЗАКРОЕМ окно
MainWindow.show()
sys.exit(app.exec_())
