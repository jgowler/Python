import random

class Character:
    def __init__(self, name, hp, str, defence, speed):
        self.name = name
        self.hp = hp
        self.str = str
        self.defence = defence
        self.speed = speed

    def attack(self):
        print(f"{self.name} attacks for {self.str}!")
    
    def defend(self):
        print(f"{self.name} defends. The attack is reduced by {self.defence}.")

class Ninja(Character):
    def __init__(self, name, hp, str, defence, speed):
        super().__init__(name, hp, str, defence, speed)

    def evade(self):
        if self.speed > 45:
            print(f"{self.name} the Ninja evaded the attack!")
        else:
            print(f"{self.name} tried to evade but was not quick enough.")

class Warrior(Character):
    def __init__(self, name, hp, str, defence, speed, weapon=None):
        super().__init__(name, hp, str, defence, speed)
        self.weapon = weapon

    def grapple(self):
        if self.str > 45:
            print(f"{self.name} was able to wrestle the enemy to the ground!")
        else:
            print(f"{self.name} tried to wrestle the enemy but was overpowered.")

    def weapon_attack(self):
        if self.weapon == True:
            damage = self.str * 2
            print(f"{self.name} used their weapon to attack for {damage} damage!")
            print(f"{self.name}'s weapon broke from the attack.")
            self.weapon == False
        else:
            print(f"{self.name} does not have a weapon, the attack failed.")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=30, str=20, defence=20, speed=40)
        self.mana = 100

    def magic_blast(self):
        if self.mana > 40:
            damage = self.mana * 1.5
            print(f"{self.name} used a magic blast. It did {damage} damage")
            self.mana -= 20
            print(f"20 of {self.name}'s mana was depleted in the attack")
        else:
            print(f"{self.name} does not have enough mana for this attack.")

    def recover_mana(self):
        mana_recovery = self.mana * 0.6
        print(f"{self.name} meditated and recovered {mana_recovery} mana")
        self.mana += mana_recovery
        print(f"{self.name} now has {self.mana} mana")

class Enemy:
    Enemy_names = [
    "Sir Reginald Puddlewick",
    "Lady Petunia Snogworthy",
    "Boris Tiddlebottom",
    "Daphne Crumpetshire",
    "Lord Nigel Bumblefluff",
    "Miss Beatrice Wobbleton",
    "Percival Twinkletoes",
    "Mabel Scone-Flinger",
    "Eustace Picklepop",
    "Gertrude Fizzlebang"
    ]
    
    def __init__(self, hp, str, defence, speed):
        if Enemy.Enemy_names:
            self.name = random.choice(Enemy.Enemy_names)
            Enemy.Enemy_names.remove(self.name)
        else:
            self.name = "Unknown"
        self.hp = hp
        self.str = str
        self.defence = defence
        self.speed = speed

    def attack(self):
        print(f"{self.name} attacks you for {self.str}!")

    def defend(self):
        print(f"{self.name} defends your attack.")

    def enemy_info(self):
        print(f"Name: {self.name}")
        print(f"HP: {self.hp}")
        print(f"Strength: {self.str}")
        print(f"Defence: {self.defence}")
        print(f"Speed: {self.speed}")

class Goblin(Enemy):
    def __init__(self, hp, str, defence, speed, weapon=None):
        super().__init__(hp, str, defence, speed)
        self.weapon = weapon

    def weapon_attack(self):
        if self.weapon == True:
            damage = self.str * 1.5
            print(f"{self.name} attacks you with its weapon. It did {damage} damage!")
            self.weapon = False
            print(f"{self.name}'s weapon has broken.")
        else:
            print(f"The Goblin {self.name} tried to attack you but did not have a weapon.")

class Dragon(Enemy):
    def __init__(self, hp, str, defence, speed):
        super().__init__(hp=200, str=60, defence=60, speed=30)

    def fireblast(self):
        if self.hp > 50:
            fireblast = self.str + self.defence - self.speed
            print(f"{self.name} released a fireblast! This did {fireblast} damage!")
            self.hp -= 30
        elif self.hp <= 50:
            print(f"{self.name} is too weak and could not release the fireball.")
