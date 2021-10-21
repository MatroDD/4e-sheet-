# --- Шесть Базовых Атрибутов ---

class Atribute:
    # Родительский класс для атрибутов
    def __init__(self, sheet): # Функция, ВСЕГДА вызываемся один раз при создании класса.
        self.sheet = sheet
        self.origin = 10
        self.misc = 0
        self.all = 0
        self.mod = 0
        self.tooltip = 'noToolTip'

    def calc(self):
        # Функция рассчёта
        pass

    def roll(self):
        # Функция броска
        pass

    def call(self):
        # Функция вызова calc() для тех, кто зависим от этого атрибута.
        pass

class Str(Atribute): # Наследуем класс: Класс(Родитель)
    def __init__(self, sheet):
        super().__init__(sheet) # Эта строка означает, что мы ОБНОВЛЯЕМ функцию
        # Т.е. всё, что было в классе родителя остаётся неизменным, если мы это не изменили здесь
        # Это значит, что мы не обязаны писать self.mod = 0 каждый раз, ибо это делает родитель
        # Что сильно укорачивает код от повторного написания.

        # Привязываем поля интерфейса к классу, чтобы обновлять данные по мере их изменения.
        self.sheet.ui.st_str_origin.textChanged.connect(self.calc)
        self.sheet.ui.st_str_misc.textChanged.connect(self.calc)
        self.sheet.ui.st_str_origin.setText(str(self.origin))
        # Вызываем первичный Calc, чтобы сгенерировать описания для ячеек.
        self.calc()

    def call(self):
        super().call()
        try:
            # Атлетика
            self.sheet.sk_athl.calc()
            pass
        except BaseException:
            pass

    def calc(self):
        super().calc()
        # Получаем
        try: # Вход в блок отлова исключений.
            self.origin = int(self.sheet.ui.st_str_origin.text())
            self.misc = int(self.sheet.ui.st_str_misc.text())
        except BaseException:
            pass
        # Считаем
        self.all = self.origin + self.misc
        self.mod = self.sheet.help[self.all]
        # Записываем
        self.sheet.ui.st_str_all.setText(str(self.all))
        self.sheet.ui.st_str_mod.setText(str(self.mod))
        # Обновляем всплывающие подсказки-описания
        self.sheet.ui.st_str_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.origin} + {self.misc} = {self.all}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
        # Вызываем пересчёт зависимых объектов
        self.call()

class Dex(Atribute): # Наследуем класс: Класс(Родитель)
    def __init__(self, sheet):
        super().__init__(sheet) # Эта строка означает, что мы ОБНОВЛЯЕМ функцию
        # Т.е. всё, что было в классе родителя остаётся неизменным, если мы это не изменили здесь
        # Это значит, что мы не обязаны писать self.mod = 0 каждый раз, ибо это делает родитель
        # Что сильно укорачивает код от повторного написания.

        # Привязываем поля интерфейса к классу, чтобы обновлять данные по мере их изменения.
        self.sheet.ui.st_dex_origin.textChanged.connect(self.calc)
        self.sheet.ui.st_dex_misc.textChanged.connect(self.calc)
        self.sheet.ui.st_dex_origin.setText(str(self.origin))
        # Вызываем первичный Calc, чтобы сгенерировать описания для ячеек.
        self.calc()

    def call(self):
        super().call()
        try:
            # Акробатика, Воровство, Скрытность
            self.sheet.sk_acr.calc()
            self.sheet.sk_thief.calc()
            self.sheet.sk_stealth.calc()
        except BaseException:
            pass

    def calc(self):
        super().calc()
        # Получаем
        try: # Вход в блок отлова исключений.
            self.origin = int(self.sheet.ui.st_dex_origin.text())
            self.misc = int(self.sheet.ui.st_dex_misc.text())
        except BaseException: # Блок действий на отловленное исключение. В нашем случае - ничего.
            pass
        # Считаем
        self.all = self.origin + self.misc
        self.mod = self.sheet.help[self.all]
        # Записываем
        self.sheet.ui.st_dex_all.setText(str(self.all))
        self.sheet.ui.st_dex_mod.setText(str(self.mod))
        # Обновляем всплывающие подсказки-описания
        self.sheet.ui.st_dex_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.origin} + {self.misc} = {self.all}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
        self.call()

class Con(Atribute): # Наследуем класс: Класс(Родитель)
    def __init__(self, sheet):
        super().__init__(sheet) # Эта строка означает, что мы ОБНОВЛЯЕМ функцию
        # Т.е. всё, что было в классе родителя остаётся неизменным, если мы это не изменили здесь
        # Это значит, что мы не обязаны писать self.mod = 0 каждый раз, ибо это делает родитель
        # Что сильно укорачивает код от повторного написания.

        # Привязываем поля интерфейса к классу, чтобы обновлять данные по мере их изменения.
        self.sheet.ui.st_con_origin.textChanged.connect(self.calc)
        self.sheet.ui.st_con_misc.textChanged.connect(self.calc)
        self.sheet.ui.st_con_origin.setText(str(self.origin))
        # Вызываем первичный Calc, чтобы сгенерировать описания для ячеек.
        self.calc()

    def call(self):
        super().call()
        try:
            # Выносливость
            self.sheet.sk_end.calc()
            pass
        except BaseException:
            pass

    def calc(self):
        super().calc()
        # Получаем
        try: # Вход в блок отлова исключений.
            self.origin = int(self.sheet.ui.st_con_origin.text())
            self.misc = int(self.sheet.ui.st_con_misc.text())
        except BaseException:
            pass
        # Считаем
        self.all = self.origin + self.misc
        self.mod = self.sheet.help[self.all]
        # Записываем
        self.sheet.ui.st_con_all.setText(str(self.all))
        self.sheet.ui.st_con_mod.setText(str(self.mod))
        # Обновляем всплывающие подсказки-описания
        self.sheet.ui.st_con_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.origin} + {self.misc} = {self.all}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
        self.call()

class Int(Atribute): # Наследуем класс: Класс(Родитель)
    def __init__(self, sheet):
        super().__init__(sheet) # Эта строка означает, что мы ОБНОВЛЯЕМ функцию
        # Т.е. всё, что было в классе родителя остаётся неизменным, если мы это не изменили здесь
        # Это значит, что мы не обязаны писать self.mod = 0 каждый раз, ибо это делает родитель
        # Что сильно укорачивает код от повторного написания.

        # Привязываем поля интерфейса к классу, чтобы обновлять данные по мере их изменения.
        self.sheet.ui.st_int_origin.textChanged.connect(self.calc)
        self.sheet.ui.st_int_misc.textChanged.connect(self.calc)
        self.sheet.ui.st_int_origin.setText(str(self.origin))
        # Вызываем первичный Calc, чтобы сгенерировать описания для ячеек.
        self.calc()

    def call(self):
        super().call()
        try:
            # Магия, История, Религия
            self.sheet.sk_arc.calc()
            self.sheet.sk_hist.calc()
            self.sheet.sk_rel.calc()
            pass
        except BaseException:
            pass

    def calc(self):
        super().calc()
        # Получаем
        try: # Вход в блок отлова исключений.
            self.origin = int(self.sheet.ui.st_int_origin.text())
            self.misc = int(self.sheet.ui.st_int_misc.text())
        except BaseException:
            pass
        # Считаем
        self.all = self.origin + self.misc
        self.mod = self.sheet.help[self.all]
        # Записываем
        self.sheet.ui.st_int_all.setText(str(self.all))
        self.sheet.ui.st_int_mod.setText(str(self.mod))
        # Обновляем всплывающие подсказки-описания
        self.sheet.ui.st_int_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.origin} + {self.misc} = {self.all}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
        self.call()

class Wis(Atribute): # Наследуем класс: Класс(Родитель)
    def __init__(self, sheet):
        super().__init__(sheet) # Эта строка означает, что мы ОБНОВЛЯЕМ функцию
        # Т.е. всё, что было в классе родителя остаётся неизменным, если мы это не изменили здесь
        # Это значит, что мы не обязаны писать self.mod = 0 каждый раз, ибо это делает родитель
        # Что сильно укорачивает код от повторного написания.

        # Привязываем поля интерфейса к классу, чтобы обновлять данные по мере их изменения.
        self.sheet.ui.st_wis_origin.textChanged.connect(self.calc)
        self.sheet.ui.st_wis_misc.textChanged.connect(self.calc)
        self.sheet.ui.st_wis_origin.setText(str(self.origin))
        # Вызываем первичный Calc, чтобы сгенерировать описания для ячеек.
        self.calc()

    def call(self):
        super().call()
        try:
            # Подземелье, Природа, Проницательность, Целительство, Восприятие
            self.sheet.sk_dung.calc()
            self.sheet.sk_nat.calc()
            self.sheet.sk_heal.calc()
            self.sheet.sk_ins.calc()
            self.sheet.sk_perc.calc()
            pass
        except BaseException:
            pass

    def calc(self):
        super().calc()
        # Получаем
        try: # Вход в блок отлова исключений.
            self.origin = int(self.sheet.ui.st_wis_origin.text())
            self.misc = int(self.sheet.ui.st_wis_misc.text())
        except BaseException:
            pass
        # Считаем
        self.all = self.origin + self.misc
        self.mod = self.sheet.help[self.all]
        # Записываем
        self.sheet.ui.st_wis_all.setText(str(self.all))
        self.sheet.ui.st_wis_mod.setText(str(self.mod))
        # Обновляем всплывающие подсказки-описания
        self.sheet.ui.st_wis_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.origin} + {self.misc} = {self.all}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
        self.call()

class Cha(Atribute): # Наследуем класс: Класс(Родитель)
    def __init__(self, sheet):
        super().__init__(sheet) # Эта строка означает, что мы ОБНОВЛЯЕМ функцию
        # Т.е. всё, что было в классе родителя остаётся неизменным, если мы это не изменили здесь
        # Это значит, что мы не обязаны писать self.mod = 0 каждый раз, ибо это делает родитель
        # Что сильно укорачивает код от повторного написания.

        # Привязываем поля интерфейса к классу, чтобы обновлять данные по мере их изменения.
        self.sheet.ui.st_cha_origin.textChanged.connect(self.calc)
        self.sheet.ui.st_cha_misc.textChanged.connect(self.calc)
        self.sheet.ui.st_cha_origin.setText(str(self.origin))
        # Вызываем первичный Calc, чтобы сгенерировать описания для ячеек.
        self.calc()

    def call(self):
        super().call()
        try:
            # Запугивание, Знание Улиц, Обман, Дипломатия
            self.sheet.sk_bluff.calc()
            self.sheet.sk_dipl.calc()
            self.sheet.sk_street.calc()
            self.sheet.sk_int.calc()
            pass
        except BaseException:
            pass

    def calc(self):
        super().calc()
        # Получаем
        try: # Вход в блок отлова исключений.
            self.origin = int(self.sheet.ui.st_cha_origin.text())
            self.misc = int(self.sheet.ui.st_cha_misc.text())
        except BaseException:
            pass
        # Считаем
        self.all = self.origin + self.misc
        self.mod = self.sheet.help[self.all]
        # Записываем
        self.sheet.ui.st_cha_all.setText(str(self.all))
        self.sheet.ui.st_cha_mod.setText(str(self.mod))
        # Обновляем всплывающие подсказки-описания
        self.sheet.ui.st_cha_all.setToolTip(f'<html><head/><body><p><span style=" font-weight:600;">Итоговый стат:</span> {self.origin} + {self.misc} = {self.all}<br/><span style=" font-weight:600;">Формула:</span> &lt;БазовыйСтат&gt; + &lt;ВременныйМод&gt; = &lt;ИтоговыйСтат&gt;</p></body></html>'),
        self.call()
