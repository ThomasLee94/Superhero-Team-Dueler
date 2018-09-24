import random

class Hero:
    def __init__(self, name, health=100):
        self.abilities = []
        self.name = name
        self.armours = []
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def add_armour(self, armour):
        self.armours.append(armour)

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

    def defend(self):
        # This method should run the defend method on each piece of armor and calculate the total defense.
        # If the hero's health is 0, the hero is out of play and should return 0 defense points.
        count = 0
        if len(self.armours) > 0:
            for armour_obj in self.armours:
                    count = count + armour_obj.defend()

            if self.health == 0:
                count = 0
                return count
            else:
                return count
        else:
            return 0

        def take_damage(self, damage_amt):
            # This method should subtract the damage amount from the hero's health.
            # If the hero dies update number of deaths.
            self.health -= damage_amt
            if self.health == 0:
                self.death += 1

        def add_kill(self, num_kills):

            # This method should add the number of kills # to self.kills
            return self.kills + num_kills



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

    def attack(self, other_team):
        # This method should total our teams attack strength and call the defend() method on the rival team that is passed in.
        # It should call add_kill() on each hero with the number of kills made.
        team_kills = 0
        for hero_obj in self.heroes:
            team_kills += add_kill(hero_obj)
        return team_kills

    def defend(self, damage_amt):
        # This method should calculate our team's total defense.
        # Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        # Return number of heroes killed in attack.
        defend_total = 0
        for hero_obj in self.heroes:
            defend_total += defend(hero_obj)

        if defend_total < damage_amt:
            excess_damage = damage_amt - defend_total
            for hero_obj in self.heroes:
                hero_obj.deal_damage(excess_damage)
        else:
            return 0

    def deal_damage(self, damage):

        # Divide the total damage amongst all heroes.
        # Return the number of heros that died in attack.
        hero_damage = damage//len(self.heroes)
        hero_deaths = 0
        for hero_obj in self.heroes:
            hero_deaths = hero_obj.take_damage(hero_damage)
        return hero_deaths

    def revive_heroes(self, health=100):

        # This method should reset all heroes health to their
        # original starting value.
        self.health = health

    def stats(self):

        # This method should print the ratio of kills/deaths for each member of the team to the screen.
        # This data must be output to the terminal.
        for hero_obj in self.heroes:
            print("{} kills: ".format(hero_obj.name) + hero_obj.kills)
            print("{} deaths: ".format(hero_obj.name) + hero_obj.deaths)

    def update_kills(self):

        # This method should update each hero when there is a team kill.
        


class Armour:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense


    def defend(self):
        self.defense = max_defense
        random_defense = randint(0, max_defense)
        return random_defense


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
