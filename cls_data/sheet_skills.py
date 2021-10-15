# --- Навыки ---

class Skill:
    def __init__(self, sheet):
        self.sheet = sheet
        self.sum = 0
        self.mod = 0
        self.ist = 0
        self.armor_penalty = 0
        self.misc = 0
        self.checker = None
        self.tooltip = 'noToolTip'

    def istrained(self):
        # Проверка владения
        pass

    def calc(self):
        pass

    def roll(self):
        pass

class Acrobatic(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        self.check = self.sheet.ui.sk_acr_istrained
        self.check.stateChanged.connect(self.istrained)

        self.sheet.ui.sk_acr_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_acr_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_dex.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_acr_misc.text())
        self.armor_penalty = int(self.sheet.ui.sk_acr_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_acr_mod.setText(str(self.mod))
        self.sheet.ui.sk_acr_sum.setText(str(self.sum))
