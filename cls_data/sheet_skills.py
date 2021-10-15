# --- Навыки ---

class Skill:
    def __init__(self, sheet):
        self.sheet = sheet
        self.name = 'name'
        self.all = 0
        self.mod = 0
        self.inst = 0
        self.armor_penalty = 0
        self.misc = 0
class Acrobatic(Skill):
    def __init__(self, sheet):
        super().__init__(sheet)
        self.name = 'Акробатика'
        self.calc()

    def calc(self):
        self.mod = int(self.sheet.ui.st_dex_mod.text()) + int(self.sheet.ui.LvL.text())//2 # CALC
        if self.sheet.ui.istrained.isChecked():
            self.inst = 5
        self.armor_penalty = int(self.sheet.ui.armorpenalty.text())
        self.misc = int(self.sheet.ui.sk_misc.text())
        self.all = self.mod + self.inst + self.armor_penalty + self.misc
        try:
            self.sheet.ui.dex_mod_here.setText(str(self.mod))
            self.sheet.ui.sk_acr_sum.setText(str(self.all))
        except BaseException:
            pass
