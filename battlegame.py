import random

class Character:
    def __init__(self, name):
        self.name = name
        self.HP = 100
        self.max_HP = 100
        self.ATK = 10
        self.SPATK = 15
        self.MANA = 100
        self.max_MANA = 100
        self.SP_COST = 30
        self.DEF = 5
        self.ATK_LUCK = 80
        self.SPATK_LUCK = 70

    def __str__(self):
        return f"\n{self.name}, ready for battle!"

    def is_alive(self):
        return self.HP > 0

    def display_stats(self):
        print(f"\n{self.name}'s stats are:")
        print(f"Health: {self.HP}/{self.max_HP}")
        print(f"ATK: {self.ATK}")
        print(f"SPATK: {self.SPATK}")
        print(f"Mana: {self.MANA}/{self.max_MANA}")
        print(f"Defense: {self.DEF}")
        print(f"ATK Luck: {self.ATK_LUCK}")
        print(f"SPATK Luck: {self.SPATK_LUCK}\n")

    def attack(self):
        chance = random.randint(0, 100)
        if chance < self.ATK_LUCK:
            print(f"{self.name}'s attack hits!")
            return self.ATK
        print(f"{self.name}'s attack missed!")
        return 0

    def special_attack(self):
        if self.MANA < self.SP_COST:
            print(f"{self.name} doesn't have enough mana!")
            return 0
        self.MANA -= self.SP_COST
        if random.randint(0, 100) < self.SPATK_LUCK:
            print(f"{self.name}'s special attack hits for {self.SPATK}!")
            return self.SPATK
        print(f"{self.name}'s special attack missed!")
        return 0

    def take_damage(self, incoming):
        damage_received = max(incoming - self.DEF, 0)
        self.HP = max(self.HP - damage_received, 0)
        print(f"{self.name} took {damage_received} damage! HP: {self.HP}/{self.max_HP}\n")

class Hero(Character):
    """Base class for every player character."""

    def __init__(self, name):
        super().__init__(name)
        self.inventory = {'health_potion': 3, 'mana_potion': 3}
        self.HP = random.randint(95, 105)
        self.max_HP = self.HP
        self.ATK = random.randint(10, 12)
        self.SPATK = random.randint(24, 26)
        self.MANA = 120
        self.max_MANA = 120
        self.SP_COST = 30
        self.DEF = random.randint(5, 7)
        self.ATK_LUCK = 88
        self.SPATK_LUCK = 78

    def use_potion(self):
        choice = input("Use health or mana potion? (health/mana): ").lower()
        if choice == "health":
            if self.inventory['health_potion'] > 0:
                self.HP = min(self.HP + 30, self.max_HP)
                self.inventory['health_potion'] -= 1
                print(f"{self.name} used a health potion! Current health: {self.HP}/{self.max_HP}")
            else:
                print("No health potions left!")
        elif choice == "mana":
            if self.inventory['mana_potion'] > 0:
                self.MANA = min(self.MANA + 50, self.max_MANA)
                self.inventory['mana_potion'] -= 1
                print(f"{self.name} used a mana potion! Current mana: {self.MANA}/{self.max_MANA}")
            else:
                print("No mana potions left!")
        else:
            print("Invalid choice.")

class Wizard(Hero):
    """Reliable special-attack accuracy, thin mana pool."""

    def __init__(self, name):
        super().__init__(name)
        self.HP = random.randint(100, 110)
        self.max_HP = self.HP
        self.ATK = random.randint(11, 13)
        self.SPATK = random.randint(25, 28)
        self.MANA = 90
        self.max_MANA = 90
        self.SP_COST = 20
        self.DEF = random.randint(6, 8)
        self.ATK_LUCK = 90
        self.SPATK_LUCK = 75

class Avatar(Hero):
    """High-mana glass cannon built around Fireballs."""

    def __init__(self, name):
        super().__init__(name)
        self.HP = random.randint(85, 95)
        self.max_HP = self.HP
        self.ATK = random.randint(11, 13)
        self.SPATK = random.randint(30, 34)
        self.MANA = 160
        self.max_MANA = 160
        self.SP_COST = 35
        self.DEF = random.randint(3, 5)
        self.ATK_LUCK = 85
        self.SPATK_LUCK = 80

    def special_attack(self):
        if self.MANA < self.SP_COST:
            print(f"{self.name} tried to throw a Fireball, but not enough mana!")
            return 0
        self.MANA -= self.SP_COST
        if random.randint(0, 100) < self.SPATK_LUCK:
            print(f"{self.name} casts a Fireball! It deals {self.SPATK} damage!")
            return self.SPATK
        print(f"{self.name}'s Fireball fizzled!")
        return 0

class Warrior(Hero):
    """Highest HP and DEF, blunt Power Strike."""

    def __init__(self, name):
        super().__init__(name)
        self.HP = random.randint(120, 130)
        self.max_HP = self.HP
        self.ATK = random.randint(14, 16)
        self.SPATK = random.randint(18, 20)
        self.MANA = 70
        self.max_MANA = 70
        self.SP_COST = 25
        self.DEF = random.randint(10, 12)
        self.ATK_LUCK = 92
        self.SPATK_LUCK = 65

    def special_attack(self):
        if self.MANA < self.SP_COST:
            print(f"{self.name} tried a Power Strike, but is too winded!")
            return 0
        self.MANA -= self.SP_COST
        if random.randint(0, 100) < self.SPATK_LUCK:
            print(f"{self.name} unleashes a Power Strike for {self.SPATK}!")
            return self.SPATK
        print(f"{self.name}'s Power Strike missed!")
        return 0

class Rogue(Hero):
    """Lowest HP and DEF, highest luck on everything."""

    def __init__(self, name):
        super().__init__(name)
        self.HP = random.randint(75, 85)
        self.max_HP = self.HP
        self.ATK = random.randint(13, 15)
        self.SPATK = random.randint(22, 25)
        self.MANA = 100
        self.max_MANA = 100
        self.SP_COST = 25
        self.DEF = random.randint(2, 4)
        self.ATK_LUCK = 95
        self.SPATK_LUCK = 85

    def special_attack(self):
        if self.MANA < self.SP_COST:
            print(f"{self.name} tried a Shadowstrike, but is out of energy!")
            return 0
        self.MANA -= self.SP_COST
        if random.randint(0, 100) < self.SPATK_LUCK:
            print(f"{self.name} lands a Shadowstrike for {self.SPATK}!")
            return self.SPATK
        print(f"{self.name}'s Shadowstrike missed!")
        return 0

HERO_CLASSES = {
    "1": ("Wizard", Wizard),
    "2": ("Avatar", Avatar),
    "3": ("Warrior", Warrior),
    "4": ("Rogue", Rogue),
}

ENEMY_TYPES = {
    "Goblin": dict(hp=(60, 70), atk=(9, 11), spatk=(12, 15), mana=50,
                   sp_cost=15, deff=(2, 4), atk_luck=75, spatk_luck=60),
    "Troll": dict(hp=(115, 130), atk=(13, 16), spatk=(10, 13), mana=40,
                  sp_cost=20, deff=(8, 10), atk_luck=68, spatk_luck=50),
    "Dark Sorcerer": dict(hp=(80, 90), atk=(9, 11), spatk=(28, 32), mana=120,
                           sp_cost=30, deff=(4, 6), atk_luck=70, spatk_luck=80),
}

class Enemy(Character):
    """Picks a random type unless one is given."""

    def __init__(self, kind=None):
        kind = kind or random.choice(list(ENEMY_TYPES.keys()))
        stats = ENEMY_TYPES[kind]
        super().__init__(kind)
        self.HP = random.randint(*stats['hp'])
        self.max_HP = self.HP
        self.ATK = random.randint(*stats['atk'])
        self.SPATK = random.randint(*stats['spatk'])
        self.MANA = stats['mana']
        self.max_MANA = stats['mana']
        self.SP_COST = stats['sp_cost']
        self.DEF = random.randint(*stats['deff'])
        self.ATK_LUCK = stats['atk_luck']
        self.SPATK_LUCK = stats['spatk_luck']

    def take_turn(self):
        print(f"\n{self.name}'s turn — HP: {self.HP}/{self.max_HP}")
        if self.MANA >= self.SP_COST and random.random() < 0.5:
            return self.special_attack()
        return self.attack()


def choose_hero(label):
    print(f"\n-- {label}: choose your hero --")
    print("1. Wizard  🧙 - Accurate specials, thin mana pool")
    print("2. Avatar  🔥 - Devastating Fireballs, fragile defense")
    print("3. Warrior 🛡️ - Tanky, reliable Power Strikes")
    print("4. Rogue   🗡️ - Fast, high-luck Shadowstrikes, low HP")
    choice = input("Enter a number (1-4): ")
    class_name, cls = HERO_CLASSES.get(choice, ("Hero", Hero))
    name = input(f"Enter this {class_name}'s name: ")
    return cls(name)


def player_turn(character):
    print(f"\n{character.name}'s turn — HP: {character.HP}/{character.max_HP}  "
          f"MANA: {character.MANA}/{character.max_MANA}")
    print("1. Attack  2. Special Attack  3. Use Potion  4. Display Stats")
    choice = input("Choose: ")

    if choice == "1":
        return character.attack()
    if choice == "2":
        return character.special_attack()
    if choice == "3":
        character.use_potion()
        return 0
    if choice == "4":
        character.display_stats()
        return player_turn(character)
    print("Invalid choice, you hesitate and lose your turn.")
    return 0


def battle(fighter_a, fighter_b, a_is_ai=False, b_is_ai=False):
    print(f"\n=== {fighter_a.name} vs {fighter_b.name}! ===")

    while fighter_a.is_alive() and fighter_b.is_alive():
        damage = fighter_a.take_turn() if a_is_ai else player_turn(fighter_a)
        fighter_b.take_damage(damage)
        if not fighter_b.is_alive():
            print(f"{fighter_b.name} has fallen! {fighter_a.name} wins!")
            return

        damage = fighter_b.take_turn() if b_is_ai else player_turn(fighter_b)
        fighter_a.take_damage(damage)
        if not fighter_a.is_alive():
            print(f"{fighter_a.name} has fallen! {fighter_b.name} wins!")
            return


def main():
    print("=== Welcome to the Battle Arena! ===")
    print("1. Fight an Enemy (solo)")
    print("2. Two-Player Battle")
    mode = input("Choose a mode (1/2): ")

    if mode == "2":
        hero1 = choose_hero("Player 1")
        hero2 = choose_hero("Player 2")
        battle(hero1, hero2)
    else:
        hero = choose_hero("Player 1")
        enemy = Enemy()
        print(f"\nA wild {enemy.name} appears!")
        battle(hero, enemy, b_is_ai=True)

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()