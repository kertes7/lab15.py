#task 1 

class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"Ім'я: {self.name}, Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack}")

hero = Character("Герой", 3, 90, 18)
hero.info()

#task 2


class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"Ім'я: {self.name}, Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack}")

    def attack_enemy(self, enemy):
        print(f"{self.name} атакує {enemy.name} на {self.attack} одиниць!")
        enemy.health -= self.attack
        if enemy.health <= 0:
            print(f"{enemy.name} переможений!")
        else:
            print(f"У {enemy.name} залишилось {enemy.health} здоров'я")


hero1 = Character("Лицар", 5, 100, 20)
hero2 = Character("Орк", 4, 80, 15)
hero1.info()
hero2.info()
hero1.attack_enemy(hero2)
hero2.info()

#task 3

class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack

    def info(self):
        print(f"Ім'я: {self.name}, Рівень: {self.level}, Здоров'я: {self.health}, Атака: {self.attack}")

class Warrior(Character):
    def __init__(self, name, level, health, attack, armor):
        super().__init__(name, level, health, attack)
        self.armor = armor

    def heal(self):
        self.health += 20
        print(f"{self.name} відновив 20 здоров'я. Поточне здоров'я: {self.health}")

class Mage(Character):
    def __init__(self, name, level, health, attack, mana):
        super().__init__(name, level, health, attack)
        self.mana = mana

    def heal(self):
        self.health += 15
        print(f"{self.name} відновив 15 здоров'я. Поточне здоров'я: {self.health}")

class Archer(Character):
    def __init__(self, name, level, health, attack, arrows):
        super().__init__(name, level, health, attack)
        self.arrows = arrows

    def heal(self):
        self.health += 10
        print(f"{self.name} відновила 10 здоров'я. Поточне здоров'я: {self.health}")

w = Warrior("Роланд", 6, 120, 25, 50)
m = Mage("Елайна", 5, 70, 30, 100)
a = Archer("Ліанна", 4, 80, 22, 30)
w.info()
m.info()
a.info()
w.heal()
m.heal()
a.heal()
w.info()
m.info()
a.info()
