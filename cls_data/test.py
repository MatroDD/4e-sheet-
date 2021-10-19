class HP_tracking:
    def __init__(self, sheet):
        self.sheet = sheet
        self.max_HP = 0
        self.bloodied = 0
        self.surge_value = 0
        self.surges_per_day = 0
        self.current_HP = 0
        self.max_HP_2 = self.max_HP
        self.tooltip = 'noToolTip'

    def calc(self):
        # Функция рассчёта
        pass

    def roll(self):
        # Функция броска
        pass

    def call(self):
        # Функция вызова calc() для тех, кто зависим от этого атрибута.
        # ВСЕГДА вызывайте зависимые объекты внутри блока try
        # Иначе словите Error404: "Зависимый объект ещё не существует"
        pass

class max_HP(HP_tracking): # Наследуем класс: Класс(Родитель)
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
