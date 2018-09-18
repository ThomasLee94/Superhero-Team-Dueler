import random

class Ability:
    def __init__(self, name, attack_strength):
         # Set Ability name
         # Set attack strength
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        # Calculate lowest attack value as an integer.
        # Use random.randint(a, b) to select a random attack value.
        # Return attack value between 0 and the full attack.

        lowest_attack = self.attack_strength // 2
        max_attack = self.attack_strength
        return random.randint(lowest_attack, max_attack)

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack_strength

class Hero:
    def __init__(self, name):
        self.abilities = []
        self.name = name

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self):
        # Run attack() on every ability hero has
        # for ability in self.abilities:
        # return ability.attack()
        # Call the attack method on every ability
        # in our ability list
        # Add up and return the total of all attacks

        output = 0
        for value in self.abilities:
            output = output + value.attack()

        return output

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())


class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        hero_found = False
        for hero_obj in self.heroes:
            if name == hero_obj.name:
                hero_found = True
                self.heroes.remove(hero_obj)

        if hero_found == False:
            return 0

    def find_hero(self, name):
        hero_found = False
        for hero_obj in self.heroes:
            if hero_obj.name == name:
                hero_found = True
                return hero_obj
        if hero_found == False:
            return 0

    def view_all_heroes(self):
        for hero_obj in self.heroes:
            print(hero_obj.name)
