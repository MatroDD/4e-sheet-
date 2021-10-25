class Defence:
    def __init__(self, sheet):
        self.sheet = sheet
        self.ten_and_halflevel = 0 # Бонус 10 + 0.5 уровня.
        self.ability = 0 # Бонус одного из двух атрибутов.
        self.clas = 0 # Бонус класса.
        # Имя class в программировании зарезервировано.
        # Его нельзя использовать - надо использовать что-то другое.
        self.feat = 0 # Бонус черт.
        self.enh = 0 # Бонус зачарования.
        self.misc = 0 # Временные модификаторы.
        self.sum = 0 # Общее значение.

    def calc(self):
        # Получаем
        pass

    def roll(self):
        pass

    def call(self):
        pass

class def_Fort(Defence):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Зависим от: Сила, Выносливость

        # Привязываем
        self.sheet.ui.def_fort_class.textChanged.connect(self.calc)
        self.sheet.ui.def_fort_feat.textChanged.connect(self.calc)
        self.sheet.ui.def_fort_enh.textChanged.connect(self.calc)
        self.sheet.ui.def_fort_misc.textChanged.connect(self.calc)

        self.calc()

    def calc(self):
        # Получаем
        self.ten_and_halflevel = 10 + self.sheet.lvl // 2
        # Узнаём, какой зависимый атрибут больше и добавляем наивысший.
        if self.sheet.st_str.mod > self.sheet.st_con.mod:
            self.ability = self.sheet.st_str.mod
        else:
            self.ability = self.sheet.st_con.mod
        self.clas = int(self.sheet.ui.def_fort_class.text())
        self.feat = int(self.sheet.ui.def_fort_feat.text())
        self.enh = int(self.sheet.ui.def_fort_enh.text())
        self.misc = int(self.sheet.ui.def_fort_misc.text())

        # Считаем
        # sum() позволяет узнать сумму всех объектов, поданных в него.
        # Подавать можно итерируемые объекты. Т.е. [списки] или (кортежи).
        # Зачем оно тут? Позволяет разбить длинную строку x = A + B + C + D + E
        # В более понятный и удобный для чтения вариант - построчно, через запятую.
        # Крайне удобно, когда суммировать нужно дохуя длинных строк.
        self.sum = sum([
            self.ten_and_halflevel,
            self.ability,
            self.clas,
            self.feat,
            self.enh,
            self.misc])

        # Записываем
        self.sheet.ui.def_fort_ability.setText(str(self.ability))
        self.sheet.ui.def_fort_ten_and_halflevel.setText(str(self.ten_and_halflevel))
        self.sheet.ui.def_fort_sum.setText(str(self.sum))
