import os, time, sys, csv, time, json
from colorama import Fore, Style

hero_dipilih = []
monster_dipilih = []
daftar_hero = []
simpan = []
simpan_info = []

class Hero():
    
    def __init__(self, name, health, attack, armor, level, tipe, exp, gold, cash, monster):
        self.__name = str(name)
        self.__health = int(health)   
        self.__attack = int(attack)  
        self.__armor = int(armor)    
        self.__exp = int(exp)    
        self.exp_pool = [100, 200, 300]    
        self.__level = int(level)  
        self.__tipe = str(tipe)    
        self.__gold = int(gold)
        self.__cash = int(cash)
        self.monster_dikalahkan = int(monster)
        self.inven = []
        self.inven_nama = ""
        self.inven_power = 0
        self.serang = 0
        self.nyawa = 0
            
    def menu_game(self):
        while True:
            os.system("cls")
            print("1. Profile\t\tGold: {}\tCash: {}\n2. Dungeon\n3. inventory\n4. Shop\n5. Cheat\n0. Exit".format(self.__gold, self.__cash))
            tanya = input("Pilihanmu: ")
            if tanya == "1":
                Hero.profile(hero_dipilih[0])
            elif tanya == "2":
                Hero.lawan_monster(hero_dipilih[0])
            elif tanya == "3":
                Hero.inventory(hero_dipilih[0])
            elif tanya == "4":
                Hero.shop(hero_dipilih[0])
            elif tanya == "5":
                Hero.cheat(hero_dipilih[0])
            elif tanya == "0":
                hero_dipilih.clear()
                simpan.clear()
                if self.__name == "Sven":
                    simpan.append([self.__health, self.__attack, self.__armor, self.__level, self.__exp, self.__gold, self.__cash, self.monster_dikalahkan])
                    with open("savefile_str.csv", "w", newline="") as simpan_str:
                        tulis1 = csv.writer(simpan_str, delimiter=",")
                        for t1 in simpan:
                            tulis1.writerow(t1)
                elif self.__name == "Ursa":
                    simpan.append([self.__health, self.__attack, self.__armor, self.__level, self.__exp, self.__gold, self.__cash, self.monster_dikalahkan])
                    with open("savefile_agi.csv", "w", newline="") as simpan_agi:
                        tulis2 = csv.writer(simpan_agi, delimiter=",")
                        for t2 in simpan:
                            tulis2.writerow(t2)
                elif self.__name == "Invoker":
                    simpan.append([self.__health, self.__attack, self.__armor, self.__level, self.__exp, self.__gold, self.__cash, self.monster_dikalahkan])
                    with open("savefile_int.csv", "w", newline="") as simpan_int:
                        tulis3 = csv.writer(simpan_int, delimiter=",")
                        for t3 in simpan:
                            tulis3.writerow(t3)
                menu_awal()
            else:
                continue
        
    def profile(self):
        os.system("cls")
        print("❖  {} ({}) ❖\n✱ Level: {}\n✱ Exp: {}/{}\n✱ Health: {}\n✱ Attack: {}\n✱ Armor: {}".format(
            self.__name, 
            self.__tipe, 
            self.__level, 
            self.__exp, 
            self.__level*100,
            self.__health, 
            self.__attack,
            self.__armor 
            )
        )
        print()
        input("#Enter untuk kembali")
        self.menu_game()
        
    def lawan_monster(self):
        while True:
            os.system("cls")
            print("1. {}\n2. {}\n3. {}\n# Enter untuk kembali".format(
                orc1.name,       
                orc2.name,       
                boss1.name       
                )    
            )
            tanya_lawan = input("Pilih monster: ")
            if tanya_lawan == "1":
                monster_dipilih.append([orc1.name, orc1.health, orc1.attack, orc1.armor])
            elif tanya_lawan == "2":
                if self.monster_dikalahkan >= 1:
                    monster_dipilih.append([orc2.name, orc2.health, orc2.attack, orc2.armor])
                else:
                    input("Kalahkan monster 1 dahulu\nEnter untuk kembali")
                    continue
            elif tanya_lawan == "3":
                if self.monster_dikalahkan >= 2:
                    monster_dipilih.append([boss1.name, boss1.health, boss1.attack, boss1.armor])
                else:
                    input("Kalahkan monster 2 dahulu\nEnter untuk kembali")
                    continue
            else:
                self.menu_game()
            break
        self.battle()
    
    def battle(self):
        attack_diterima = 0
        name_lawan = monster_dipilih[0][0]
        health_lawan = monster_dipilih[0][1]
        attack_lawan = monster_dipilih[0][2]
        armor_lawan = monster_dipilih[0][3]
        while True:
            os.system("cls")
            print("❖  {} ❖\n✱ Health: {}\n✱ Attack: {}\n✱ Armor: {}".format(
                self.__name, 
                self.__health, 
                self.__attack,
                self.__armor 
                )
            )
            print()
            print("❖  {} ❖\n✱ Health: {}\n✱ Attack: {}\n✱ Armor: {}".format(
                name_lawan, 
                health_lawan, 
                attack_lawan, 
                armor_lawan
                )
            )
            input()
            health_lawan -= self.__attack
            self.__health -= attack_lawan
            attack_diterima += attack_lawan
            if self.__health <= 0 and health_lawan <= 0:
                input("DRAW\nEnter untuk kembali")
                break
            elif health_lawan <= 0:
                hero_dipilih[0].exp_up = 50
                self.__gold += 20
                self.__cash += 10
                if name_lawan == orc1.name:
                    if self.monster_dikalahkan == 0:
                        self.monster_dikalahkan += 1
                elif name_lawan == orc2.name:
                    if self.monster_dikalahkan == 1:
                        self.monster_dikalahkan += 1
                elif name_lawan == boss1.name:
                    if self.monster_dikalahkan == 2:
                        self.monster_dikalahkan += 1
                input("You WIN\nEnter untuk kembali")
                break
            elif self.__health <= 0:
                input("You LOSE\nEnter untuk kembali")
                break
        self.__health += attack_diterima
        monster_dipilih.pop([0][0])
        self.menu_game()
        
    def cheat(self):
        os.system("cls")
        tanya_cheat = input("Masukkan kode: ")
        if tanya_cheat == "mantap":
            self.__health += 1000
            self.__attack += 1000
            self.__armor += 1000
            self.__level += 100
            self.__gold += 1000
            self.__cash += 1000
            print("Kode diterima")
        else:
            print("Kode salah")
        input("Enter untuk kembali")
        
    def inventory(self):
        tampung_list_sword = list()
        tampung_dict_sword = dict()
        tampung_list_armor = list()
        tampung_dict_armor = dict()
        try:
            if self.tipe == "Stregth":
                with open("sword_str.json", "r") as eq:
                    baca1 = json.load(eq)
                    for bc in baca1:
                        tampung_list_sword.append(bc)
                with open("armor_str.json", "r") as eqq:
                    baca2 = json.load(eqq)
                    for bcc in baca2:
                        tampung_list_armor.append(bcc)
            elif self.tipe == "Agility":
                with open("sword_agi.json", "r") as eq:
                    baca1 = json.load(eq)
                    for bc in baca1:
                        tampung_list_sword.append(bc)
                with open("armor_agi.json", "r") as eqq:
                    baca2 = json.load(eqq)
                    for bcc in baca2:
                        tampung_list_armor.append(bcc)
            elif self.tipe == "Intelligent":
                with open("sword_int.json", "r") as eq:
                    baca1 = json.load(eq)
                    for bc in baca1:
                        tampung_list_sword.append(bc)
                with open("armor_int.json", "r") as eqq:
                    baca2 = json.load(eqq)
                    for bcc in baca2:
                        tampung_list_armor.append(bcc)                 
        except:
            pass
        while True:
            os.system("cls")
            tanya_equip = input("1. Sword\n2. Armor\n# Enter untuk kembali\nPilih: ")
            if tanya_equip == "1":
                os.system("cls")
                print(f"{'No':^6} {'Nama':^15} {'Power':^6}")
                index = 1
                for ls in tampung_list_sword:
                    print(f"{index:^6} {ls['Sword']:^15} {ls['Power']:^6}")
                    index += 1
                try:
                    tanya_inventory = int(input("Pilih: "))
                    if tanya_inventory == 1:
                        if self.serang != int(sword1.power):
                            self.serang = int(sword1.power)
                            self.__attack += self.serang
                            input("Senjata berhasil dipakai")
                        self.menu_game()
                    else:
                        input("Item tidak ada")
                except:
                    pass
            elif tanya_equip == "2":
                os.system("cls")
                print(f"{'No':^6} {'Nama':^15} {'Power':^6}")
                index = 1
                for ls in tampung_list_armor:
                    print(f"{index:^6} {ls['Armor']:^15} {ls['Power']:^6}")
                    index += 1
                try:    
                    tanya_inventory = int(input("Pilih: "))
                    if tanya_inventory == 1:
                        if self.nyawa != int(armor1.power):
                            self.nyawa = int(armor1.power)
                            self.__health += self.nyawa
                            input("Armor berhasil dipakai")
                        self.menu_game()
                    else:
                        input("Item tidak ada")
                except:
                    pass
            else:
                self.menu_game()
    
    def sword_str(self):
        tampung_list = list()
        tampung_dict = dict()
        try:
            with open("sword_str.json", "r") as k:
                baca1 = json.load(k)
                for b in baca1:
                    tampung_list.append(b)
        except:
            pass
        tampung_dict["Sword"] = self.inven_nama
        tampung_dict["Power"] = self.inven_power
        tampung_list.append(tampung_dict)
        with open("sword_str.json", "w") as eq:
            tulis1 = json.dump(tampung_list , eq, indent=2)
        
    def armor_str(self):
        tampung_list = list()
        tampung_dict = dict()
        try:
            with open("armor_str.json", "r") as k:
                baca1 = json.load(k)
                for b in baca1:
                    tampung_list.append(b)
        except:
            pass
        tampung_dict["Armor"] = self.inven_nama
        tampung_dict["Power"] = self.inven_power
        tampung_list.append(tampung_dict)
        with open("armor_str.json", "w") as eq:
            tulis1 = json.dump(tampung_list , eq, indent=2)
            
    def sword_agi(self):
        tampung_list = list()
        tampung_dict = dict()
        try:
            with open("sword_agi.json", "r") as k:
                baca1 = json.load(k)
                for b in baca1:
                    tampung_list.append(b)
        except:
            pass
        tampung_dict["Sword"] = self.inven_nama
        tampung_dict["Power"] = self.inven_power
        tampung_list.append(tampung_dict)
        with open("sword_agi.json", "w") as eq:
            tulis1 = json.dump(tampung_list , eq, indent=2)
        
    def armor_agi(self):
        tampung_list = list()
        tampung_dict = dict()
        try:
            with open("sword_agi.json", "r") as k:
                baca1 = json.load(k)
                for b in baca1:
                    tampung_list.append(b)
        except:
            pass
        tampung_dict["Armor"] = self.inven_nama
        tampung_dict["Power"] = self.inven_power
        tampung_list.append(tampung_dict)
        with open("armor_agi.json", "w") as eq:
            tulis1 = json.dump(tampung_list , eq, indent=2)
            
    def sword_int(self):
        tampung_list = list()
        tampung_dict = dict()
        try:
            with open("sword_int.json", "r") as k:
                baca1 = json.load(k)
                for b in baca1:
                    tampung_list.append(b)
        except:
            pass
        tampung_dict["Sword"] = self.inven_nama
        tampung_dict["Power"] = self.inven_power
        tampung_list.append(tampung_dict)
        with open("sword_int.json", "w") as eq:
            tulis1 = json.dump(tampung_list , eq, indent=2)
        
    def armor_int(self):
        tampung_list = list()
        tampung_dict = dict()
        try:
            with open("sword_int.json", "r") as k:
                baca1 = json.load(k)
                for b in baca1:
                    tampung_list.append(b)
        except:
            pass
        tampung_dict["Armor"] = self.inven_nama
        tampung_dict["Power"] = self.inven_power
        tampung_list.append(tampung_dict)
        with open("armor_int.json", "w") as eq:
            tulis1 = json.dump(tampung_list , eq, indent=2)
            
    def shop(self):
        os.system("cls")
        tanya_shop = input("1. Sword\n2. Armor\n# Enter untuk kembali\nPilih: ")
        if tanya_shop == "1":
            os.system("cls")
            print("1.", sword1.name)
            tanya_beli = input("Pilih: ")
            if tanya_beli == "1":
                if self.__cash >= int(sword1.price):
                    self.inven_nama = str(sword1.name)
                    self.inven_power = int(sword1.power)
                    self.__cash -= 100
                    if self.tipe == "Stregth":
                        self.sword_str()
                    elif self.tipe == "Agility":
                        self.sword_agi()
                    elif self.tipe == "Intelligent":
                        self.sword_int()
                else:
                    input("Cash tidak cukup")
        elif tanya_shop == "2":
            os.system("cls")
            print("1.", armor1.name)
            tanya_beli = input("Pilih: ")
            if tanya_beli == "1":
                if self.__cash >= int(sword1.price):
                    self.inven_nama = str(armor1.name)
                    self.inven_power = int(armor1.power)
                    self.__cash -= 100
                    if self.tipe == "Stregth":
                        self.armor_str()
                    elif self.tipe == "Agility":
                        self.armor_agi()
                    elif self.tipe == "Intelligent":
                        self.armor_int()
                else:
                    input("Cash tidak cukup")
        self.menu_game()         
        
    @property
    def name(self):
        return self.__name
        
    @property
    def health(self):
        return self.__health
    
    @property
    def attack(self):
        return self.__attack
    
    @property
    def armor(self):
        return self.__armor

    @property
    def tipe(self):
        return self.__tipe
    
    @property
    def level(self):
        return self.__level
    
    @property
    def exp(self):
        return self.__exp
    
    @property
    def exp_up(self):
        pass
    @exp_up.setter
    def exp_up(self, isi):
        self.__exp += isi
        if self.__level == 1:
            if self.__exp >= self.exp_pool[0]:
                self.level_up = self.__exp // self.exp_pool[0]
                self.__exp %= self.exp_pool[0]
        elif self.__level == 2:
            if self.__exp >= self.exp_pool[1]:
                self.level_up = self.__exp // self.exp_pool[1]
                self.__exp %= self.exp_pool[1]
        elif self.__level == 3:
            if self.__exp >= self.exp_pool[2]:
                self.level_up = self.__exp // self.exp_pool[2]
                self.__exp %= self.exp_pool[2]
    
    @property
    def level_up(self):
        pass
    @level_up.setter
    def level_up(self, isi):
        self.__level += isi
        if self.__level == 2:
            self.__health += self.health_pool[0]
            self.__attack += self.attack_pool[0]
            self.__armor += self.armor_pool[0]
        elif self.__level == 3:
            self.__health += self.health_pool[1]
            self.__attack += self.attack_pool[1]
            self.__armor += self.armor_pool[1]
        elif self.__level == 4:
            self.__health += self.health_pool[2]
            self.__attack += self.attack_pool[2]
            self.__armor += self.armor_pool[2]

class Hero_str(Hero):
    def __init__(self, name, health, attack, armor, level, tipe, exp, gold, cash, monster):
        super().__init__(name, health, attack, armor, level, tipe, exp, gold, cash, monster)
        self.health_pool = [100, 250, 350]
        self.attack_pool = [10, 25, 35]
        self.armor_pool = [10, 20, 30]

class Hero_agi(Hero):
    def __init__(self, name, health, attack, armor, level, tipe, exp, gold, cash, monster):
        super().__init__(name, health, attack, armor, level, tipe, exp, gold, cash, monster)
        self.health_pool = [100, 150, 200]
        self.attack_pool = [10, 40, 70]
        self.armor_pool = [10, 15, 20]

class Hero_int(Hero):
    def __init__(self, name, health, attack, armor, level, tipe, exp, gold, cash, monster):
        super().__init__(name, health, attack, armor, level, tipe, exp, gold, cash, monster)
        self.health_pool = [100, 200, 300]
        self.attack_pool = [10, 30, 50]
        self.armor_pool = [10, 15, 20]

class Monster(Hero):
    def __init__(self, name, health, attack, armor, level, tipe, exp, gold, cash, monster):
        super().__init__(name, health, attack, armor, level, tipe, exp, gold, cash, monster)

class Equip():
    def __init__(self, name, power, price):
        self.__name = name
        self.__power = power
        self.__price = price
        
    @property
    def name(self):
        return self.__name
    @property
    def power(self):
        return self.__power
    @property
    def price(self):
        return self.__price
    
#equip
sword1 = Equip("Sword of Heaven", 200, 100)
armor1 = Equip("Armor of Heaven", 600, 100)

#monster
orc1 = Monster("Orc 1", 100, 10, 5, 1, "None", 0, 0, 0, 0)
orc2 = Monster("Orc 2", 150, 15, 10, 1, "None", 0, 0, 0, 0)
boss1 = Monster("Boss 1", 350, 40, 25, 1, "None",0 ,0, 0, 0)

def menu_new():
    os.system("cls")
    print("1. Sven (Strength)\n2. Ursa (Agility)\n3. Invoker (Intelligent)\n# Enter untuk kembali")
    tanya_hero = input("Pilihanmu: ")
    if tanya_hero == "1":
        sven = Hero_str("Sven", 110, 10, 10, 1, "Stregth", 0, 0, 0, 0)
        daftar_hero.append(sven)
    elif tanya_hero == "2":
        ursa = Hero_agi("Ursa", 90, 15, 8, 1, "Agility", 0, 0, 0, 0)
        daftar_hero.append(ursa)
    elif tanya_hero == "3":
        invoker = Hero_int("Invoker", 100, 12, 6, 1, "Intelligent", 0, 0, 0, 0)
        daftar_hero.append(invoker)
    else:
        menu_awal()
    hero_dipilih.append(daftar_hero[0])
    daftar_hero.clear()
    Hero.menu_game(hero_dipilih[0])
                 
def menu_load():
    os.system("cls")
    simpan_info.clear()
    print("1. Sven (Strength)\n2. Ursa (Agility)\n3. Invoker (Intelligent)\n# Enter untuk kembali")
    tanya_hero = input("Pilihanmu: ")
    if tanya_hero == "1":
        try:
            with open("savefile_str.csv", "r") as hero_str:
                baca1 = csv.reader(hero_str, delimiter=",")
                for b1 in range(1):
                    for c1 in baca1:
                        simpan_info.append(c1)             
            sven = Hero_str("Sven", simpan_info[0][0], simpan_info[0][1], simpan_info[0][2], simpan_info[0][3], "Stregth", simpan_info[0][4], simpan_info[0][5], simpan_info[0][6], simpan_info[0][7])
            daftar_hero.append(sven)
            hero_dipilih.append(daftar_hero[0])
            daftar_hero.clear()
        except:
            input("Save data tidak ditemukan\nEnter untuk kembali")
            menu_awal()
    elif tanya_hero == "2":
        try:
            with open("savefile_agi.csv", "r") as hero_agi:
                baca2 = csv.reader(hero_agi, delimiter=",")
                for b2 in range(1):
                    for c2 in baca2:
                        simpan_info.append(c2)               
            ursa = Hero_agi("Ursa", simpan_info[0][0], simpan_info[0][1], simpan_info[0][2], simpan_info[0][3], "Agility", simpan_info[0][4], simpan_info[0][5], simpan_info[0][6], simpan_info[0][7])
            daftar_hero.append(ursa)
            hero_dipilih.append(daftar_hero[0])
            daftar_hero.clear()
        except:
            input("Save data tidak ditemukan\nEnter untuk kembali")
            menu_awal()
    elif tanya_hero == "3":
        try:            
            with open("savefile_int.csv", "r") as hero_int:
                baca3 = csv.reader(hero_int, delimiter=",")
                for b3 in range(1):
                    for c3 in baca3:
                        simpan_info.append(c3)            
            invoker = Hero_int("Invoker", simpan_info[0][0], simpan_info[0][1], simpan_info[0][2], simpan_info[0][3], "Intelligent", simpan_info[0][4], simpan_info[0][5], simpan_info[0][6], simpan_info[0][7])
            daftar_hero.append(invoker)
            hero_dipilih.append(daftar_hero[0])
            daftar_hero.clear()
        except:
            input("Save data tidak ditemukan\nEnter untuk kembali")
            menu_awal()
    else:
        menu_awal()
    Hero.menu_game(hero_dipilih[0])

os.system("cls")
print(Fore.YELLOW, Style.BRIGHT)
teks = ('''
            # # # #     # # # #     # # # #
           #       #   #       #  #             # # # #
          # # # # #   # # # # #  #      # # #       #
         #    #      #           #         #      # 
        #      #    #              # # # #     # # # #
''')
for t in teks:
    sys.stdout.write(t)
    sys.stdout.flush()
    time.sleep(0.01)
print(Style.RESET_ALL)
def menu_awal():
    while True:
        os.system("cls")
        print(Fore.YELLOW, Style.BRIGHT)
        print('''
            # # # #     # # # #     # # # #
           #       #   #       #  #             # # # #
          # # # # #   # # # # #  #      # # #       #
         #    #      #           #         #      # 
        #      #    #              # # # #     # # # #
        ''')
        print(Style.RESET_ALL)
        tanya = input("[1] New Game\n[2] Load Game\n[3] Exit\nPilih: ")
        if tanya == "1":
            menu_new()
        elif tanya == "2":
            menu_load()
        elif tanya == "3":
            exit()    
menu_awal()