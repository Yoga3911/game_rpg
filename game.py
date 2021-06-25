import os, sys, time, random
import animasi_stickman as an
from colorama import Fore, Style
from alive_progress import alive_bar, config_handler; 

os.system("cls")
class Hero:
    
    def __init__(self, name, health, power):
        self.__name = name
        self.__health = health
        self.__power = power
        
    @property
    def name(self):
        return self.__name
    
    @property
    def health(self):
        return self.__health
    
    @property
    def power(self):
        return self.__power

    def monster1(self):
        global nama_lawan
        global nyawa_lawan
        global serang_lawan
        nama_lawan = monster1.name
        nyawa_lawan = monster1.health
        serang_lawan = monster1.power
        
    def monster2(self):
        global nama_lawan
        global nyawa_lawan
        global serang_lawan
        nama_lawan = monster2.name
        nyawa_lawan = monster2.health
        serang_lawan = monster2.power
        
    def bos1(self):
        global nama_lawan
        global nyawa_lawan
        global serang_lawan
        nama_lawan = bos1.name
        nyawa_lawan = bos1.health
        serang_lawan = bos1.power

class Item:
    
    def __init__(self, name, power):
        self.__name = name
        self.__power = power
    @property
    def name(self):
        return self.__name
    @property
    def power(self):
        return self.__power
    

#Hero#
monster1 = Hero("Monster 1", 50, 5)
monster2 = Hero("Monster 2", 100, 10)
bos1 = Hero("Bringas", 400, 40)
masuk = input("Masukkan nama hero: ")
karakter = Hero("{}".format(masuk), 100, 10)
nama = karakter.name
nyawa = karakter.health
serang = karakter.power
daftar = []
gold = 0
cash = 0
biaya_nyawa = 7
biaya_serang = 9
energy = 0
level = 0
exp = 0
exp1 = 50
exp2 = 150
##

#item#
senjata1 = Item("Pedang 1", 10)
senjata1X = Item("Pedang 1X", 15)
senjata2 = Item("Pedang 2", 20)
senjata2X = Item("Pedang 2X", 25)
senjata3 = Item("Pedang 3", 40)
senjata3X = Item("Pedang 3X", 60)
senjata1_shop = Item("Pedang kematian", 100)
senjata2_shop = Item("Pedang dewa", 300)

baju1 = Item("Baju 1", 30)
baju1X = Item("Baju 1X", 40)
baju2 = Item("Baju 2", 50)
baju2X = Item("Baju 2X", 60)
baju3 = Item("Baju 3", 80)
baju3X = Item("Baju 3X", 100)
baju1_shop = Item("Baju kematian", 300)
baju2_shop = Item("Baju dewa", 500)

inven = []
inven_senjata_nama = []
inven_senjata_power = []
inven_baju_nama = []
inven_baju_power = []
senjata = 0
baju = 0
##

ucapan = "Alice: Hai {} selamat datang ...".format(masuk)
ucapan1 = "> Hai Alice"
ucapan2 = "Alice: Tolong bantu desa ini pahlawan !"
ucapan3 = "> Baiklah ..."
for x in ucapan:
    sys.stdout.write(x)
    sys.stdout.flush()
    if x == "A" or x == "l" or x == "i" or x == "c" or x == "e":
        time.sleep(0)
    elif x == ":":
        time.sleep(1.5)
    else:
        time.sleep(0.1)
print()
for ucap1 in ucapan1:
    sys.stdout.write(ucap1)
    sys.stdout.flush()
    if ucap1 == ">":
        time.sleep(1.5)
    else:
        time.sleep(0.1)
print()
for ucap2 in ucapan2:
    sys.stdout.write(ucap2)
    sys.stdout.flush()
    if ucap2 == "A" or ucap2 == "l" or ucap2 == "i" or ucap2 == "c" or ucap2 == "e":
        time.sleep(0)
    elif ucap2 == ":":
        time.sleep(1.5)
    else:
        time.sleep(0.1)
print()
for ucap3 in ucapan3:
    sys.stdout.write(ucap3)
    sys.stdout.flush()
    if ucap3 == ">":    
        time.sleep(1.5)
    else:
        time.sleep(0.1)
print()
input("\nTekan enter untuk memulai game")

os.system("cls")
print(Fore.YELLOW)
print(Style.DIM)
config_handler.set_global(theme='ascii')
with alive_bar(100, length=40) as bar:                                                                 
    for i in range(100):                                                                               
        time.sleep(.05)                                                                                
        bar() 
print(Style.RESET_ALL)

while True:
    os.system("cls")
    print(55*"=")
    print(Fore.CYAN, Style.BRIGHT,">>> Hidden Leaf <<<".center(55, " "), Style.RESET_ALL)
    print(55*"=")
    print("1. Profile\t",Fore.YELLOW, Style.DIM,"Gold:", gold, Style.RESET_ALL, Fore.GREEN, "\tCash:", cash, Style.RESET_ALL,"\n2. Dungeon\n3. Inventory\n4. Upgrade\n5. Shop\n6. Battle record\n7. Cheat\n8. Exit")
    pilih = input("[1, 2, 3, 4, 5, 6, 7, 8]: ")
    if pilih == "1":
        os.system("cls")
        print(55*"=")
        print(Fore.YELLOW,">>> Profile <<<".center(55, " "), Style.RESET_ALL)
        print(55*"=")
        print(Fore.MAGENTA, end = "")
        print("Hero:\t", nama)
        print(Fore.BLUE, end = "")
        print(Style.BRIGHT, end = "")
        print("Level:\t", level)
        print(Fore.CYAN, end = "")
        print(Style.BRIGHT, end = "")
        if level == 0:
            print("Exp:\t", exp, "||", exp1 - exp, "xp, level 0 > level 1")
        elif level == 1:
            print("Exp:\t", exp, "||", exp2 - exp, "xp, level 1 > level 2")
        else:
            print("Exp:\t", exp)
            
        print(Fore.GREEN, end = "")
        print(Style.DIM, end = "")
        print("Health:\t", nyawa)
        print(Fore.RED, end = "")
        print(Style.DIM, end = "")
        print("Power:\t", serang)
        print(Style.RESET_ALL, end = "")
        input("Tekan enter untuk kembali")
    elif pilih == "2":
        os.system("cls")
        print(55*"=")
        print(Fore.YELLOW,">>> Dungeon <<<".center(55, " "), Style.RESET_ALL)
        print(55*"=")
        print("1. Monster 1\n2. Monster 2\n3. Bringas\n#Tekan enter untuk kembali")
        musuh = input("Pilih lawan [1, 2, 3]: ")
        print(55*"=")
        if musuh == "1":
            print("Nama:", monster1.name,"\nHealth:", monster1.health, "\nPower:", monster1.power)
            yakin = input("Ingin melawan musuh ini? [y/t]: ")
            if yakin == "y":
                Hero.monster1(monster1)
            else:
                pass
        elif musuh == "2":
            print("Nama:", monster2.name,"\nHealth:", monster2.health, "\nPower:", monster2.power)
            yakin = input("Ingin melawan musuh ini? [y/t]: ")
            if yakin == "y":
                if monster1.name in daftar:
                    Hero.monster2(monster2)
                else:
                    print("Kalahkan Monster 1 dulu")
                    print(55*"=")
                    input("Tekan enter untuk kembali")
            else:
                pass
        elif musuh == "3":
            print("Nama:", bos1.name,"\nHealth:", bos1.health, "\nPower:", monster2.power)
            yakin = input("Ingin melawan musuh ini? [y/t]: ")
            if yakin == "y":
                if monster2.name in daftar:
                    Hero.bos1(bos1)
                else:
                    print("Kalahkan Monster 2 dulu")
                    print(55*"=")
                    input("Tekan enter untuk kembali")
            else:
                pass
        else:
            pass
    elif pilih == "3":
        os.system("cls")
        print(55*"=")
        print(Fore.YELLOW,">>> Inventory <<<".center(55, " "), Style.RESET_ALL)
        print(55*"=")
        print("1. Senjata\n2. Baju\n#Tekan enter untuk kembali")
        item = input("Pilihanmu [1, 2]: ")
        if item == "1":
            angka1 = 1
            if inven_senjata_nama != []:
                for ada_senjata in inven_senjata_nama:
                    print("{}. {}".format(angka1, ada_senjata))
                    angka1 += 1
                tanya_senjata = input("Pilih senjata: ")
                if tanya_senjata == "1":
                    if senjata != inven_senjata_power[0]:
                        serang -= senjata
                        senjata = inven_senjata_power[0]
                        serang += senjata
                        print("Senjata berhasil dipakai")
                    else:
                        pass
                elif tanya_senjata == "2":
                    if len(inven_senjata_power) == 2:
                        if senjata != inven_senjata_power[1]:
                            serang -= senjata
                            senjata = inven_senjata_power[1]
                            serang += senjata
                            print("Senjata berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_senjata == "3":
                    if len(inven_senjata_power) == 3:
                        if senjata != inven_senjata_power[2]:
                            serang -= senjata
                            senjata = inven_senjata_power[2]
                            serang += senjata
                            print("Senjata berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_senjata == "4":
                    if len(inven_senjata_power) == 4:
                        if senjata != inven_senjata_power[3]:
                            serang -= senjata
                            senjata = inven_senjata_power[3]
                            serang += senjata
                            print("Senjata berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_senjata == "5":
                    if len(inven_senjata_power) == 5:
                        if senjata != inven_senjata_power[4]:
                            serang -= senjata
                            senjata = inven_senjata_power[4]
                            serang += senjata
                            print("Senjata berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_senjata == "6":
                    if len(inven_senjata_power) == 6:
                        if senjata != inven_senjata_power[5]:
                            serang -= senjata
                            senjata = inven_senjata_power[5]
                            serang += senjata
                            print("Senjata berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_senjata == "7":
                    if len(inven_senjata_power) == 7:
                        if senjata != inven_senjata_power[6]:
                            serang -= senjata
                            senjata = inven_senjata_power[6]
                            serang += senjata
                            print("Senjata berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_senjata == "8":
                    if len(inven_senjata_power) == 8:
                        if senjata != inven_senjata_power[7]:
                            serang -= senjata
                            senjata = inven_senjata_power[7]
                            serang += senjata
                            print("Senjata berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_senjata == "":
                    pass
                else:
                    pass
            elif inven_senjata_nama == []:
                print("Tidak ada item")    
            input("Tekan enter untuk kembali")
        elif item == "2":
            angka2 = 1
            if inven_baju_nama != []:
                for ada_baju in inven_baju_nama:
                    print("{}. {}".format(angka2, ada_baju))
                    angka2 += 1
                tanya_baju = input("Pilih baju: ")
                if tanya_baju == "1":
                    if baju != inven_baju_power[0]:
                        nyawa -= baju
                        baju = inven_baju_power[0]
                        nyawa += baju
                        print("Baju berhasil dipakai")
                    else:
                        pass
                elif tanya_baju == "2":
                    if len(inven_baju_power) == 2:
                        if baju != inven_baju_power[1]:
                            nyawa -= baju
                            baju = inven_baju_power[1]
                            nyawa += baju
                            print("Baju berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_baju == "3":
                    if len(inven_baju_power) == 3:
                        if baju != inven_baju_power[2]:
                            nyawa -= baju
                            baju = inven_baju_power[2]
                            nyawa += baju
                            print("Baju berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_baju == "4":
                    if len(inven_baju_power) == 4:
                        if baju != inven_baju_power[3]:
                            nyawa -= baju
                            baju = inven_baju_power[3]
                            nyawa += baju
                            print("Baju berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_baju == "5":
                    if len(inven_baju_power) == 5:
                        if baju != inven_baju_power[4]:
                            nyawa -= baju
                            baju = inven_baju_power[4]
                            nyawa += baju
                            print("Baju berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_baju == "6":
                    if len(inven_baju_power) == 6:
                        if baju != inven_baju_power[5]:
                            nyawa -= baju
                            baju = inven_baju_power[5]
                            nyawa += baju
                            print("Baju berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_baju == "7":
                    if len(inven_baju_power) == 7:
                        if baju != inven_baju_power[6]:
                            nyawa -= baju
                            baju = inven_baju_power[6]
                            nyawa += baju
                            print("Baju berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_baju == "8":
                    if len(inven_baju_power) == 8:
                        if baju != inven_baju_power[7]:
                            nyawa -= baju
                            baju = inven_baju_power[7]
                            nyawa += baju
                            print("Baju berhasil dipakai")
                        else:
                            pass
                    else:
                        pass
                elif tanya_baju == "":
                    pass
                else:
                    pass
            elif inven_baju_nama == []:
                print("Tidak ada item")
            input("Tekan enter untuk kembali")
        else:
            pass    
    
    elif pilih == "4":
        os.system("cls")
        print(55*"=")
        print(Fore.YELLOW,">>> Upgrade <<<".center(55, " "), Style.RESET_ALL)
        print(55*"=")
        print("1. Health\n2. Power\n#Tekan enter untuk kembali")
        atribut = input("Upgrade [1, 2]: ")
        if atribut == "1":
            print("Biaya upgrade", biaya_nyawa)
            if gold < biaya_nyawa:
                print("Gold tidak cukup")
            elif gold >= biaya_nyawa:
                print("Health ditingkatkan:", nyawa, ">>", nyawa + 30)
                nyawa += 30
                gold -= biaya_nyawa
                biaya_nyawa += 4
            print(55*"=")
            input("Tekan enter untuk kembali")
        elif atribut == "2":
            print("Biaya upgrade", biaya_serang)
            if gold < biaya_serang:
                print("Gold tidak cukup")
            elif gold >= biaya_serang:
                print("Power ditingkatkan:", serang, ">>", serang + 10)
                serang += 10
                gold -= biaya_serang
                biaya_serang += 4
            print(55*"=")
            input("Tekan enter untuk kembali")
        else:
            pass
    elif pilih == "5":
        os.system("cls")
        print(55*"=")
        print(Fore.YELLOW,">>> Shop <<<".center(55, " "), Style.RESET_ALL)
        print(55*"=")
        print("1. Pedang kematian\n2. Pedang dewa\n3. Baju kematian\n4. Baju dewa\n#Tekan enter untuk kembali")
        tanya_belanja = input("[1, 2, 3, 4]: ")
        if tanya_belanja == "1":
            print(senjata1_shop.name, "Attack +",senjata1_shop.power, "\nHarga 100 cash")
            tanya_beli = input("Apakah anda ingin membeli senjata ini? [y/t] ")
            if tanya_beli == "y":
                if cash >= 100:
                    if senjata1_shop not in inven:
                        cash -= 100
                        inven.append(senjata1_shop)
                        inven_senjata_nama.append(senjata1_shop.name)
                        inven_senjata_power.append(senjata1_shop.power)
                    else:
                        print("Anda sudah punya senjata ini")
                else:
                    print("Cash tidak cukup")
            else:
                pass
            print(55*"=")
            input("Tekan enter untuk kembali")
        elif tanya_belanja == "2":
            print(senjata2_shop.name, "Attack +",senjata2_shop.power, "\nHarga 300 cash")
            tanya_beli = input("Apakah anda ingin membeli senjata ini? [y/t] ")
            if tanya_beli == "y":
                if cash >= 300:
                    if senjata2_shop not in inven:
                        cash -= 300
                        inven.append(senjata2_shop)
                        inven_senjata_nama.append(senjata2_shop.name)
                        inven_senjata_power.append(senjata2_shop.power)
                    else:
                        print("Anda sudah punya senjata ini")
                else:
                    print("Cash tidak cukup")
            else:
                pass
            print(55*"=")
            input("Tekan enter untuk kembali")
        elif tanya_belanja == "3":
            print(baju1_shop.name, "Attack +",baju1_shop.power, "\nHarga 100 cash")
            tanya_beli = input("Apakah anda ingin membeli senjata ini? [y/t] ")
            if tanya_beli == "y":
                if cash >= 100:
                    if baju1_shop not in inven:
                        cash -= 100
                        inven.append(baju1_shop)
                        inven_baju_nama.append(baju1_shop.name)
                        inven_baju_power.append(baju1_shop.power)
                    else:
                        print("Anda sudah punya senjata ini")
                else:
                    print("Cash tidak cukup")
            else:
                pass
            print(55*"=")
            input("Tekan enter untuk kembali")
        elif tanya_belanja == "4":
            print(baju2_shop.name, "Attack +",baju2_shop.power, "\nHarga 300 cash")
            tanya_beli = input("Apakah anda ingin membeli senjata ini? [y/t] ")
            if tanya_beli == "y":
                if cash >= 300:
                    if baju2_shop not in inven:
                        cash -= 300
                        inven.append(baju2_shop)
                        inven_baju_nama.append(baju2_shop.name)
                        inven_baju_power.append(baju2_shop.power)
                    else:
                        print("Anda sudah punya senjata ini")
                else:
                    print("Cash tidak cukup")
            else:
                pass
            print(55*"=")
            input("Tekan enter untuk kembali")
        else:
            pass
    elif pilih == "6":
        os.system("cls")
        print(55*"=")
        print(Fore.YELLOW,">>> Battle record <<<".center(55, " "), Style.RESET_ALL)
        print(55*"=")
        index = 1
        for i in daftar:
            print("{}. {}".format(index, i))
            index += 1
        print(55*"=")
        input("Tekan enter untuk kembali")
        os.system("cls")
    elif pilih == "7":
        os.system("cls")
        print(55*"=")
        print(Fore.YELLOW,">>> Cheat <<<".center(55, " "), Style.RESET_ALL)
        print(55*"=")
        curang = input("Masukkan kode: ")
        if curang == "mantap":
            nyawa += 99999
            serang += 99999
            cash += 99999
            gold += 99999
            print("Kode diterima")
        else:
            print("Kode salah")
        input("Tekan enter untuk kembali")
    elif pilih == "8":
        print(55*"=")
        pergi = "> Sampai jumpa kembali {} :)".format(masuk)
        for s in pergi:
            if s == ">":
                sys.stdout.write(s)
                sys.stdout.flush()
                time.sleep(0.8)
            else:
                sys.stdout.write(s)
                sys.stdout.flush()
                time.sleep(0.1)
        exit()
    else:
        pass
    
    try:
        nyawa_player = nyawa        
        while nyawa_player > 0 and nyawa_lawan > 0:
            os.system("cls")
            print(55*"=")
            print("Nama:\t", nama, "\nHP:\t", nyawa_player, "\nPower:\t", serang)
            print(Fore.CYAN, end = "")
            print(Style.BRIGHT, end = "")
            print("Energy:\t", energy)
            print(Style.RESET_ALL, end = "")
            print(55*"=")
            print("Nama:\t", nama_lawan, "\nHP:\t", nyawa_lawan, "\nPower:\t", serang_lawan)
            print(55*"=")
            tanya = input("1. Attack\n2. Ultimate (3 Energy)\nPilihanmu [1, 2]: ")
            if tanya == "1":
                nyawa_lawan -= serang
                nyawa_player -= serang_lawan
                energy += 1
                print(55*"=")
                input("Tekan enter untuk lanjut")
            elif tanya == "2":
                if energy > 2:
                    nyawa_lawan -= (serang + 30) 
                    nyawa_player -= serang_lawan
                    energy -= 3
                else:
                    print("Energy tidak cukup!")
                print(55*"=")
                input("Tekan enter untuk lanjut")
            else:
                print("Perintah tidak ada")
                print(55*"=")  
                input("Tekan enter untuk lanjut")
                
            if nyawa_player < 1 and nyawa_lawan < 1:
                energy -= energy
                print("Draw")
                print(55*"=")
                input("Tekan enter untuk kembali")
            elif nyawa_player < 1:
                energy -= energy
                print("Lose")
                print(55*"=")
                input("Tekan enter untuk kembali")
            elif nyawa_lawan < 1:
                an.anim()
                if musuh == "1":
                    gold += 9
                    cash += 10
                    exp += 30
                    acak1 = random.randint(1, 10)
                    if acak1 == 1:
                        if senjata1X not in inven:
                            inven.append(senjata1X)
                            print("\nAnda mendapatkan", senjata1X.name, end = "")
                        else:
                            pass
                    elif acak1 == 2:
                        if baju1X not in inven:
                            inven.append(baju1X)
                            print("\nAnda mendapatkan", baju1X.name, end = "")
                        else:
                            pass
                    elif acak1 > 2 and acak1 <= 6:
                        if senjata1 not in inven:
                            inven.append(senjata1)
                            print("\nAnda mendapatkan", senjata1.name, end = "")
                        else:
                            pass
                    elif acak1 > 6 and acak1 <= 10:
                        if baju1 not in inven:
                            inven.append(baju1)
                            print("\nAnda mendapatkan", baju1.name, end = "")
                        else:
                            pass
                    if senjata1 in inven:
                        if senjata1.power not in inven_senjata_power:
                            inven_senjata_nama.append(senjata1.name)
                            inven_senjata_power.append(senjata1.power)
                        else:
                            pass
                    if senjata1X in inven:
                        if senjata1X.power not in inven_senjata_power:
                            inven_senjata_nama.append(senjata1X.name)
                            inven_senjata_power.append(senjata1X.power)
                        else:
                            pass
                    if baju1 in inven:
                        if baju1.power not in inven_baju_power:
                            inven_baju_nama.append(baju1.name)
                            inven_baju_power.append(baju1.power)
                        else:
                            pass
                    if baju1X in inven:
                        if baju1X.power not in inven_baju_power:
                            inven_baju_nama.append(baju1X.name)
                            inven_baju_power.append(baju1X.power)
                        else:
                            pass
                    if monster1.name in daftar:
                        pass
                    elif monster1.name not in daftar:
                        daftar.append(monster1.name)
                elif musuh == "2":
                    gold += 11
                    cash += 15
                    exp += 60
                    acak1 = random.randint(1, 10)
                    if acak1 == 1:
                        if senjata2X not in inven:
                            inven.append(senjata2X)
                            print("\nAnda mendapatkan", senjata2X.name, end = "")
                        else:
                            pass
                    elif acak1 == 2:
                        if baju2X not in inven:
                            inven.append(baju2X)
                            print("\nAnda mendapatkan", baju2X.name, end = "")
                        else:
                            pass
                    elif acak1 > 2 and acak1 <= 6:
                        if senjata2 not in inven:
                            inven.append(senjata2)
                            print("\nAnda mendapatkan", senjata2.name, end = "")
                        else:
                            pass
                    elif acak1 > 6 and acak1 <= 10:
                        if baju2 not in inven:
                            inven.append(baju2)
                            print("\nAnda mendapatkan", baju2.name, end = "")
                        else:
                            pass
                    if senjata2 in inven:
                        if senjata2.power not in inven_senjata_power:
                            inven_senjata_nama.append(senjata2.name)
                            inven_senjata_power.append(senjata2.power)
                        else:
                            pass
                    if senjata2X in inven:
                        if senjata2X.power not in inven_senjata_power:
                            inven_senjata_nama.append(senjata2X.name)
                            inven_senjata_power.append(senjata2X.power)
                        else:
                            pass
                    if baju2 in inven:
                        if baju2.power not in inven_baju_power:
                            inven_baju_nama.append(baju2.name)
                            inven_baju_power.append(baju2.power)
                        else:
                            pass
                    if baju2X in inven:
                        if baju2X.power not in inven_baju_power:
                            inven_baju_nama.append(baju2X.name)
                            inven_baju_power.append(baju2X.power)
                        else:
                            pass
                    if monster2.name in daftar:
                        pass
                    elif monster2.name not in daftar:
                        daftar.append(monster2.name)
                elif musuh == "3":
                    gold += 20
                    cash += 30
                    exp += 120
                    acak1 = random.randint(1, 10)
                    if acak1 == 1:
                        if senjata3X not in inven:
                            inven.append(senjata3X)
                            print("\nAnda mendapatkan", senjata3X.name, end = "")
                        else:
                            pass
                    elif acak1 == 2:
                        if baju3X not in inven:
                            inven.append(baju3X)
                            print("\nAnda mendapatkan", baju3X.name, end = "")
                        else:
                            pass
                    elif acak1 > 2 and acak1 <= 6:
                        if senjata3 not in inven:
                            inven.append(senjata3)
                            print("\nAnda mendapatkan", senjata3.name, end = "")
                        else:
                            pass
                    elif acak1 > 6 and acak1 <= 10:
                        if baju3 not in inven:
                            inven.append(baju3)
                            print("\nAnda mendapatkan", baju3.name, end = "")
                        else:
                            pass
                    if senjata3 in inven:
                        if senjata3.power not in inven_senjata_power:
                            inven_senjata_nama.append(senjata3.name)
                            inven_senjata_power.append(senjata3.power)
                        else:
                            pass
                    if senjata3X in inven:
                        if senjata3X.power not in inven_senjata_power:
                            inven_senjata_nama.append(senjata3X.name)
                            inven_senjata_power.append(senjata3X.power)
                        else:
                            pass
                    if baju3 in inven:
                        if baju3.power not in inven_baju_power:
                            inven_baju_nama.append(baju3.name)
                            inven_baju_power.append(baju3.power)
                        else:
                            pass
                    if baju3X in inven:
                        if baju3X.power not in inven_baju_power:
                            inven_baju_nama.append(baju3X.name)
                            inven_baju_power.append(baju3X.power)
                        else:
                            pass
                    if bos1.name in daftar:
                        pass
                    elif bos1.name not in daftar:
                        daftar.append(bos1.name)
                energy -= energy
                print("\n==============================")
                if level == 0:
                    if exp >= exp1:
                        level += 1
                        nyawa += 20
                        serang += 5
                        exp -= exp1
                        print("Naik ke level 1")
                elif level == 1:
                    if exp >= exp2:
                        nyawa += 30
                        serang += 10
                        level += 1
                        exp -= exp2
                        print("Naik ke level 2")
                else:
                    pass
                input("Tekan enter untuk kembali")
            os.system("cls")
    except:
        pass
