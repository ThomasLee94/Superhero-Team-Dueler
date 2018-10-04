# Name: Thomas J. Lee
# Project: Superheroes

import random
import math

class Hero:
    def __init__(self, name, health=100):
        self.abilities = []
        self.name = name
        self.armours = []
        self.start_health = health
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
        # This method should run the defend method on each piece of armor and calculate the total defence.
        # If the hero's health is 0, the hero is out of play and should return 0 defence points.
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
        if self.health > 0:
            self.health -= damage_amt
            print("take_damage method: {}".format(self.health))
            if self.health <= 0:
                self.deaths += 1
                return 1
            else:
                return 0
        else:
            return 0

    def add_kill(self, num_kills):

        # This method should add the number of kills # to self.kills
        self.kills += num_kills

class Ability:
    def __init__(self, name, attack_strength):
         # Set Ability name
         # Set attack strength
        self.name = name
        self.attack_strength = int(attack_strength)

    def attack(self):
        # Calculate lowest attack value as an integer.
        # Use random.randint(a, b) to select a random attack value.
        # Return attack value between 0 and the full attack.

        lowest_attack = math.floor(self.attack_strength/2)
        max_attack = self.attack_strength
        return random.randint(lowest_attack, max_attack)

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = int(attack_strength)


class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)

class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = []
        self.deaths = 0

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
        #Find total kills
        team_attack = 0
        for hero_obj in self.heroes:
            team_attack += hero_obj.attack() # <----- this in an Int 

        total_kills = other_team.defend(team_attack)
        print("team attack: {}".format(total_kills))
        for hero_obj in self.heroes:
            hero_obj.add_kill(total_kills)

        return total_kills

    def defend(self, damage_amt):
        # This method should calculate our team's total defence.
        # Any damage in excess of our team's total defence should be evenly distributed amongst all heroes with the deal_damage() method.
        # Return number of heroes killed in attack.
        defend_total = 0
        for hero_obj in self.heroes:
            defend_total += hero_obj.defend()

        if defend_total < damage_amt:
            excess_damage = damage_amt - defend_total
            num_dead_in_attack = self.deal_damage(excess_damage)
            self.deaths += num_dead_in_attack
            return num_dead_in_attack
        else:
            return 0

    def deal_damage(self, damage):
        # Divide the total damage amongst all heroes.
        # Return the number of heros that died in attack.
        hero_damage = damage//len(self.heroes)
        hero_deaths = 0
        print(hero_damage)
        print(hero_deaths)
        print(type(hero_damage))
        print(type(hero_deaths))
        for hero_obj in self.heroes:
            hero_deaths += hero_obj.take_damage(hero_damage)
        return hero_deaths

    def revive_heroes(self, health=100):
        # This method should reset all heroes health to their
        # original starting value.
        for hero_obj in self.heroes:
            hero_obj.health = hero_obj.start_health

    def stats(self):
        # This method should print the ratio of kills/deaths for each member of the team to the screen.
        # This data must be output to the terminal.
        for hero_obj in self.heroes:
            print("{} kills: {}".format(hero_obj.name, hero_obj.kills))
            print("{} deaths:{}".format(hero_obj.name, hero_obj.deaths))

    def update_kills(self):
        # This method should update each hero when there is a team kill.
        total_kills = 0
        for hero_obj in self.heroes:
            total_kills += hero_obj.kills
        return total_kills

class Armour:
    def __init__(self, name, defence):
        self.name = name
        self.defence = defence

    def defend(self):
        max_defence = self.defence
        random_defence = random.randint(0
        , max_defence)
        return random_defence

class Arena:
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two

    def not_letter(self, input):
        which_team = []
        build_team = ''
        string = str(input)
        for i in string:
            which_team.append(i)
        if len(which_team) == 8:
            if str(which_team) == "team_one":
                build_team = build_team_one()
            if str(which_team) == "team_two":
                build_team = build_team_two()
                

        if type(input) is not str:
            print("Sorry, letters only. Try again\n")
            arena.build_team_one()
    
    def not_num(self, input):
        which_team = []
        string = str(input)

        counter = 0

        for i in string:
            which_team.append(i)
        while len(which_team) == 8:
            if str(which_team) == "team_one":
                counter = 1

        if type(input) is not int:
            print("Sorry, numbers only. Try again\n")
            if counter == 1:
                arena.build_team_one()
            else:
                arena.build_team_two()

    def build_team_one(self):
        """
        This method should allow a user to build team one  by taking the team name from input.
        """
        print("BUILD TEAM ONE")
        team_one_name = input("What is the name of team one? ")
        self.not_letter(team_one_name)

        team_one_hero_name = input("what is the hero name? ")
        self.not_letter(team_one_hero_name)

        team_one_hero_ability_name = input("what is the ability name? ")
        self.not_letter(team_one_hero_ability_name)

        team_one_hero_ability_value = input("what is the attack damage of {}? ".format(team_one_hero_ability_name))
       

        team_one_hero_armour_name = input("What is the name for {}'s armour? ".format(team_one_hero_name))
        self.not_letter(team_one_hero_armour_name)

        team_one_hero_armour_value = input("what is the armour value of {}'s {}? ".format(team_one_hero_name, team_one_hero_armour_name))
       

        team_one_hero_one = Hero(team_one_hero_name)
        team_one_hero_one_ability= Ability(team_one_hero_ability_name, int(team_one_hero_ability_value))
        team_one_hero_one_armour = Armour(team_one_hero_armour_name, int(team_one_hero_armour_value))

        team_one_hero_one.add_ability(team_one_hero_one_ability)
        team_one_hero_one.add_armour(team_one_hero_one_armour)

        self.team_one.add_hero(team_one_hero_one)
        
    def build_team_two(self):
        """
        This method should allow user to build team two.
        """

        print("BUILD TEAM TWO")
        team_two_name = input("What is the name of team two? ")
        self.not_letter(team_two_name)

        team_two_hero_name = input("what is the hero name? ")
        self.not_letter(team_two_hero_name)

        team_two_hero_ability_name = input("what is the ability name? ")
        self.not_letter(team_two_hero_ability_name)

        team_two_hero_ability_value = input("what is the attack damage of {}? ".format(team_two_hero_ability_name))
        

        team_two_hero_armour_name = input("What is the name for {}'s armour? ".format(team_two_hero_name))
        self.not_letter(team_two_hero_armour_name)

        team_two_hero_armour_value = input("what is the armour value of {}'s {}? ".format(team_two_hero_name, team_two_hero_armour_name))
        

        team_two_hero_one = Hero(team_two_hero_name)
        team_two_hero_one_ability= Ability(team_two_hero_ability_name, int(team_two_hero_ability_value))
        team_two_hero_one_armour = Armour(team_two_hero_armour_name, int(team_two_hero_armour_value))

        team_two_hero_one.add_ability(team_two_hero_one_ability)
        team_two_hero_one.add_armour(team_two_hero_one_armour)

        self.team_two.add_hero(team_two_hero_one)

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        After battle, let user know who won
        """
        print("LOOK HERE")
        print(self.team_one.name)
        team_one_deaths = 0
        team_two_deaths = 0
        
        while (team_one_deaths < len(self.team_one.heroes) or team_two_deaths < len(self.team_two.heroes)):
            team_one_deaths += self.team_two.attack(self.team_one)
            team_two_deaths += self.team_one.attack(self.team_two)

        else:
            # print battle winner
            if team_one_deaths >= len(self.team_one.heroes):
                print("Team {} loses!".format(self.team_one.name))
                print("Team {} wins!".format(self.team_two.name))
            if team_two_deaths >= len(self.team_two.heroes):
                print("Team {} loses!".format(self.team_two.name))
                print("Team {} wins!".format(self.team_one.name))

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """
        self.team_one.stats()
        self.team_two.stats()

if __name__ == "__main__":

    # arena.build_team_one()
    # arena.build_team_two()

    # arena.team_battle()
    # arena.show_stats()

    game_is_running = True

    # Instantiate Game Arena
    team_A = Team("A")
    team_B = Team("B")
    arena = Arena(team_A, team_B)

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
    