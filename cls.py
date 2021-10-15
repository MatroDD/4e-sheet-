class Hero:
    def __init__(self, god):
        self.god = god
        self.name = god.ui.char_name.text()
        self.vlv = 1
        self.class_level = {}
        self.armor_type = 'light'
        self.armor_class = 10

        self.str = 10
        self.str_misc = 0
        self.str_mod = 0
        self.str_all = 10
        self.dex = 10
        self.dex_misc = 0
        self.dex_mod = 0
        self.dex_all = 10
        self.con = 10
        self.con_misc = 0
        self.con_mod = 0
        self.con_all = 10
        self.int = 10
        self.int_misc = 0
        self.int_mod = 0
        self.int_all = 10
        self.wis = 10
        self.wis_misc = 0
        self.wis_mod = 0
        self.wis_all = 10
        self.cha = 10
        self.cha_misc = 0
        self.cha_mod = 0
        self.cha_all = 10

    def setArmorClass(self):
        ac = self.armor_type
        if ac == 'light':
            self.armor_class = self.dex_mod + 10 # Базовая формула, другие будут позже

    def setStr(self,):
                # org=int(self.god.ui.st_str_all.text()),
                # misc=int(self.god.ui.st_str_misc.text()),
                # mod=int(self.god.ui.st_str_mod.text()),
                # all=int(self.god.ui.st_str_all.text())):
        self.str = org
        self.str_misc = misc
        self.str_mod = mod
        self.str_all = all

    def setDex(self):
        self.dex = int(self.god.ui.st_dex_all.text())
        self.dex_misc = int(self.god.ui.st_dex_misc.text())
        self.dex_mod = int(self.god.ui.st_dex_mod.text())
        self.dex_all = int(self.god.ui.st_dex_all.text())

    def setCon(self):
        self.con = int(self.god.ui.st_con_all.text())
        self.con_misc = int(self.god.ui.st_con_misc.text())
        self.con_mod = int(self.god.ui.st_con_mod.text())
        self.con_all = int(self.god.ui.st_con_all.text())

    def setInt(self):
        self.int = int(self.god.ui.st_int_all.text())
        self.int_misc = int(self.god.ui.st_int_misc.text())
        self.int_mod = int(self.god.ui.st_int_mod.text())
        self.int_all = int(self.god.ui.st_int_all.text())

    def setWis(self):
        self.wis = int(self.god.ui.st_wis_all.text())
        self.wis_misc = int(self.god.ui.st_wis_misc.text())
        self.wis_mod = int(self.god.ui.st_wis_mod.text())
        self.wis_all = int(self.god.ui.st_wis_all.text())

    def setCha(self):
        self.cha = int(self.god.ui.st_cha_all.text())
        self.cha_misc = int(self.god.ui.st_cha_misc.text())
        self.cha_mod = int(self.god.ui.st_cha_mod.text())
        self.cha_all = int(self.god.ui.st_cha_all.text())

class Skill:
    def __init__(self, god):
        self.god = god
        self.name = 'name'
        self.all = 0
        self.mod = 0
        self.inst = 0
        self.armor_penalty = 0
        self.misc = 0
class Acrobatic(Skill):
    def __init__(self, god):
        super().__init__(god)
        self.name = 'Акробатика'
        self.calc()

    def calc(self):
        self.mod = int(self.god.ui.st_dex_mod.text()) + int(self.god.ui.LvL.text())//2 # CALC
        if self.god.ui.istrained.isChecked():
            self.inst = 5
        self.armor_penalty = int(self.god.ui.armorpenalty.text())
        self.misc = int(self.god.ui.sk_misc.text())
        self.all = self.mod + self.inst + self.armor_penalty + self.misc
        try:
            self.god.ui.dex_mod_here.setText(str(self.mod))
            self.god.ui.sk_acr_sum.setText(str(self.all))
        except BaseException:
            pass
