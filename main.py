import math
import random

class Armor:
    def __init__(self, AC, type, name):
        self.AC = AC
        self.name = name
        self.type = type

class Weapon:
    def __init__(self, name, bonus, damage_min, damage_max):
        self.name = name
        self.bonus = bonus
        self.damage_min = damage_min
        self.damage_max = damage_max

class Class_type:

    def __init__(self, name, start_HP, ability):
        self.name = name
        self.start_HP = start_HP
        self.ability = ability

class Hero:

    def __init__(self, name, STR, DEX, CON, INT, CHA, WIN, Class_type):
        self.LVL = 1
        self.STR = math.ceil((STR - 10) / 2)
        self.DEX = math.ceil((DEX - 10) / 2)
        self.CON = math.ceil((CON - 10) / 2)
        self.INT = math.ceil((INT - 10) / 2)
        self.CHA = math.ceil((CHA - 10) / 2)
        self.PROF = 2
        self.class_type = Class_type
        self.WIN = math.ceil((WIN - 10) / 2)
        self.equipment = ''
        self.inventory = ''
        self.name = name
        self.Health(Class_type)

    def lvl_up(self):
        MAX_LVL = 20
        if self.LVL < MAX_LVL:
            self.LVL += 1
            self.Health(Class_type)
            if self.LVL == 5:
                self.PROF = 3
            if self.LVL == 9:
                self.PROF = 4
            if self.LVL == 13:
                self.PROF = 5
            if self.LVL == 17:
                self.PROF = 6

    def Health(self, Class_type):
        self.HP = self.class_type.start_HP + self.CON + (self.class_type.start_HP/2 + self.CON) * (self.LVL - 1)

    def wear(self, Armor):
        self.equipment = {'Armor': Armor.name}
        if Armor.type == 'Heavy':
            self.AC = Armor.AC
        if Armor.type == 'Middle':
            if self.DEX < 2:
                self.AC = Armor.AC + self.DEX
            else:
                self.AC = Armor.AC + 2
        if Armor.type == 'Light':
            self.AC = Armor.AC + self.DEX

    def barbarian_naked_armor(self):
        if self.class_type == Barbarian:
            self.AC = 10 + self.DEX + self.CON

    def arm(self, Weapon):
        self.equipment = {'Armor': Weapon.name}
        self.damage_min = Weapon.damage_min + self.STR
        self.damage_max = Weapon.damage_max + self.STR
        self.hit_min = 1 + Weapon.bonus + self.STR + self.PROF
        self.hit_max = 20 + Weapon.bonus + self.STR + self.PROF

    def attacked(self, hit, damage):
        print(f'{self.name} attacked')
        if self.AC < hit:
            self.HP = self.HP - damage
            print(f'secssecful attack takes {damage} damege, {self.name} has {self.HP} HP')
        else:
            print('miss')

    def attack(self):
        hit = random.randint(self.hit_min, self.hit_max)
        if hit == self.hit_max:
            damage = random.randint(self.damage_min, self.damage_max) + random.randint(self.damage_min, self.damage_max)
        else:
            damage = random.randint(self.damage_min, self.damage_max)
        print(f'{self.name}, attack {hit}, damage {damage}')
        return hit, damage

Chainmail = Armor(16, 'Heavy', 'Chainmail')
Half_Plate = Armor(16, 'Middle', 'Half_Plate')
Plate = Armor(16, 'Heavy', 'Plate')

Warhammer = Weapon('Warhammer', 0, 1, 10)
Maul = Weapon('Maul', 0, 2, 12)
Greataxe = Weapon('Greataxe', 0, 1, 12)

Fighter = Class_type('Fighter', 10, '')
Barbarian = Class_type('Barbarian', 12, '')

Tor = Hero('Tor',24, 12, 18, 10, 12, 14, Fighter)
Grackle = Hero('Grackle', 20, 14, 20, 10, 10, 14, Barbarian)

while Tor.LVL < 10:
    Tor.lvl_up()
Tor.wear(Half_Plate)
Tor.arm(Warhammer)

while Grackle.LVL < 10:
    Grackle.lvl_up()
Grackle.barbarian_naked_armor()
Grackle.arm(Maul)

while Tor.HP > 0 and Grackle.HP > 0:
    Grackle.attacked(*Tor.attack())
    Tor.attacked(*Grackle.attack())

if Tor.HP < 0:
    print('Grackle win')
if Grackle.HP < 0:
    print('Tor win')

