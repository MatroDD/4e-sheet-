# --- Шесть Базовых Атрибутов ---
from random import randint

class Atribute:
    # Родительский класс для атрибутов
    def __init__(self, sheet): # Функция, ВСЕГДА вызываемся один раз при создании класса.
        self.sheet = sheet
        self.origin = 10 # Изначальное значение.
        self.misc = 0 # Временные модификаторы.
        self.all = 0 # Общее/итоговое значение.
        self.mod = 0 # Модификатор.
        self.tooltip = 'noToolTip' # Всплывающая подсказка.
        self.rolltip = {} # Используется для генерации текста бросков.

    def calc(self):
        # Функция рассчёта
        pass

    def roll(self):
        # Функция броска
        self.rolltip['randint'] = randint(1, 20) # Кидаем 1d20
        if self.rolltip['randint'] == 1: # Если выпало 1
            self.rolltip['color'] = '#aa0000' # Красный
        elif self.rolltip['randint'] == 20: # Если выпало 20
            self.rolltip['color'] = '#00aa00' # Зелёный
        else: # Иначе
            self.rolltip['color'] = '#000000' # Чёрный
        self.rolltip['result'] = self.rolltip['randint'] + self.mod

        # Написать результаты броска в чат.
        self.sheet.ui.chat.append(f'''<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600; font-style:italic;">бросок </span><span style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600;">{self.rolltip['what']}:</span><span style=" font-family:'MS Shell Dlg 2'; font-size:8pt;"> 1d20</span><span style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600;">[</span><span style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600; color:{self.rolltip['color']};">{self.rolltip['randint']}</span><span style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600;">]</span><span style=" font-family:'MS Shell Dlg 2'; font-size:8pt;"> +{self.rolltip['what']}.Мод</span><span style=" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600;">[{self.mod}]</span><span style=" font-family:'MS Shell Dlg 2'; font-size:8pt;"> = {self.rolltip['result']}</span></p>''')
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

        self.rolltip['what'] = 'СИЛ' # Текст для бросков
        # Привязываем кнопку с текстом навыка к функции броска
        self.sheet.ui.st_str_button.clicked.connect(self.roll)

    def call(self):
        super().call()
        try:
            # Атлетика, Стойкость
            self.sheet.sk_athl.calc()
            self.sheet.def_fort.calc()
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

        self.rolltip['what'] = 'ЛОВ' # Текст для бросков
        # Привязываем кнопку с текстом навыка к функции броска
        self.sheet.ui.st_dex_button.clicked.connect(self.roll)

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

        self.rolltip['what'] = 'ВЫН' # Текст для бросков
        # Привязываем кнопку с текстом навыка к функции броска
        self.sheet.ui.st_con_button.clicked.connect(self.roll)

    def call(self):
        super().call()
        try:
            # Выносливость, Стойкость
            self.sheet.sk_end.calc()
            self.sheet.def_fort.calc()
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

        self.rolltip['what'] = 'ИНТ' # Текст для бросков
        # Привязываем кнопку с текстом навыка к функции броска
        self.sheet.ui.st_int_button.clicked.connect(self.roll)

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

        self.rolltip['what'] = 'МУД' # Текст для бросков
        # Привязываем кнопку с текстом навыка к функции броска
        self.sheet.ui.st_wis_button.clicked.connect(self.roll)

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

        self.rolltip['what'] = 'ХАР' # Текст для бросков
        # Привязываем кнопку с текстом навыка к функции броска
        self.sheet.ui.st_cha_button.clicked.connect(self.roll)

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
