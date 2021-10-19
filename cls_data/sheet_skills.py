# --- Навыки ---

class Skill:
    def __init__(self, sheet):
        self.sheet = sheet
        self.sum = 0 # Итоговое значение.
        self.mod = 0 # Модификатор (Мод.стата + уровень // 2)
        self.ist = 0 # Владение 0 / +5
        self.armor_penalty = 0 # Штраф от брони. Всегда приводится к отрицательному перед проверкой.
        self.misc = 0 # Прочие временные модификаторв.
        self.checker = None # Галочка на владении True / False
        self.tooltip = 'noToolTip' # Всплывающая подсказка.

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
        # Зависим от: Ловкость
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
        self.calc()

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

class sk_Arc(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Интеллект
        self.check = self.sheet.ui.sk_arc_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_arc_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_arc_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_int.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_arc_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_arc_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_arc_mod.setText(str(self.mod))
        self.sheet.ui.sk_arc_sum.setText(str(self.sum))

class sk_Athl(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Сила
        self.check = self.sheet.ui.sk_athl_istrained
        self.check.stateChanged.connect(self.istrained)

        self.sheet.ui.sk_athl_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_athl_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_str.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_athl_misc.text())
        self.armor_penalty = int(self.sheet.ui.sk_athl_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_athl_mod.setText(str(self.mod))
        self.sheet.ui.sk_athl_sum.setText(str(self.sum))

class sk_Bluff(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Харизма
        self.check = self.sheet.ui.sk_bluff_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_bluff_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_bluff_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_cha.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_bluff_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_bluff_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_bluff_mod.setText(str(self.mod))
        self.sheet.ui.sk_bluff_sum.setText(str(self.sum))

class sk_Dipl(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Харизма
        self.check = self.sheet.ui.sk_dipl_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_dipl_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_dipl_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_cha.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_dipl_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_dipl_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_dipl_mod.setText(str(self.mod))
        self.sheet.ui.sk_dipl_sum.setText(str(self.sum))

class sk_Dung(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Мудрость
        self.check = self.sheet.ui.sk_dung_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_dung_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_dung_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_wis.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_dung_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_dung_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_dung_mod.setText(str(self.mod))
        self.sheet.ui.sk_dung_sum.setText(str(self.sum))

class sk_End(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Выносливость
        self.check = self.sheet.ui.sk_end_istrained
        self.check.stateChanged.connect(self.istrained)

        self.sheet.ui.sk_end_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_end_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_con.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_end_misc.text())
        self.armor_penalty = int(self.sheet.ui.sk_end_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_end_mod.setText(str(self.mod))
        self.sheet.ui.sk_end_sum.setText(str(self.sum))

class sk_Heal(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Мудрость
        self.check = self.sheet.ui.sk_heal_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_heal_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_heal_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_wis.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_heal_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_heal_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_heal_mod.setText(str(self.mod))
        self.sheet.ui.sk_heal_sum.setText(str(self.sum))

class sk_Hist(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Интеллект
        self.check = self.sheet.ui.sk_hist_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_hist_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_hist_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_int.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_hist_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_hist_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_hist_mod.setText(str(self.mod))
        self.sheet.ui.sk_hist_sum.setText(str(self.sum))

class sk_Ins(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Мудрость
        self.check = self.sheet.ui.sk_ins_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_ins_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_ins_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_wis.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_ins_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_ins_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_ins_mod.setText(str(self.mod))
        self.sheet.ui.sk_ins_sum.setText(str(self.sum))

class sk_Int(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Харизма
        self.check = self.sheet.ui.sk_int_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_int_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_int_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_cha.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_int_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_int_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_int_mod.setText(str(self.mod))
        self.sheet.ui.sk_int_sum.setText(str(self.sum))

class sk_Nat(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Мудрость
        self.check = self.sheet.ui.sk_nat_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_nat_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_nat_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_wis.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_nat_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_nat_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_nat_mod.setText(str(self.mod))
        self.sheet.ui.sk_nat_sum.setText(str(self.sum))

class sk_Perc(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Мудрость
        self.check = self.sheet.ui.sk_perc_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_perc_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_perc_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_wis.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_perc_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_perc_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_perc_mod.setText(str(self.mod))
        self.sheet.ui.sk_perc_sum.setText(str(self.sum))

class sk_Rel(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Интеллект
        self.check = self.sheet.ui.sk_rel_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_rel_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_rel_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_int.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_rel_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_rel_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_rel_mod.setText(str(self.mod))
        self.sheet.ui.sk_rel_sum.setText(str(self.sum))

class sk_Stealth(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Ловкость
        self.check = self.sheet.ui.sk_stealth_istrained
        self.check.stateChanged.connect(self.istrained)

        self.sheet.ui.sk_stealth_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_stealth_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_dex.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_stealth_misc.text())
        self.armor_penalty = int(self.sheet.ui.sk_stealth_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_stealth_mod.setText(str(self.mod))
        self.sheet.ui.sk_stealth_sum.setText(str(self.sum))

class sk_Street(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Харизма
        self.check = self.sheet.ui.sk_street_istrained
        self.check.stateChanged.connect(self.istrained)

        # self.sheet.ui.sk_street_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_street_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_cha.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_street_misc.text())
        # self.armor_penalty = int(self.sheet.ui.sk_street_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist # + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_street_mod.setText(str(self.mod))
        self.sheet.ui.sk_street_sum.setText(str(self.sum))

class sk_Thief(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        # Привязываем галку владения
        # Зависим от: Ловкость
        self.check = self.sheet.ui.sk_thief_istrained
        self.check.stateChanged.connect(self.istrained)

        self.sheet.ui.sk_thief_armorpenalty.textChanged.connect(self.calc)
        self.sheet.ui.sk_thief_misc.textChanged.connect(self.calc)
        self.calc()

    def istrained(self):
        super().istrained()
        if self.check.isChecked():
            self.ist += 5
        else:
            self.ist -= 5
        self.calc()

    def calc(self):
        super().calc()
        # Получаем
        self.mod = self.sheet.st_dex.mod + self.sheet.lvl // 2
        self.misc = int(self.sheet.ui.sk_thief_misc.text())
        self.armor_penalty = int(self.sheet.ui.sk_thief_armorpenalty.text())
        self.sum = self.mod + self.misc + self.ist + -abs(self.armor_penalty)

        # Пишем
        self.sheet.ui.sk_thief_mod.setText(str(self.mod))
        self.sheet.ui.sk_thief_sum.setText(str(self.sum))
