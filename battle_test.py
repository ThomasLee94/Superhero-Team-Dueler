import pytest
import superheroes
import random
import io
import sys

# Helper Functions


def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()


def create_armour():
    armours = [
        "Calculator",
        "Laser Shield",
        "Invisibility",
        "SFPD Strike Force",
        "Social Workers",
        "Face Paint",
        "Damaskus Shield",
        "Bamboo Wall",
        "Forced Projection",
        "Thick Fog",
        "Wall of Will",
        "Wall of Walls",
        "Obamacare",
        "Thick Goo"]
    name = armours[random.randint(0, len(armours) - 1)]
    power = random.randint(23, 700000)
    return superheroes.Armour(name, power)


def create_weapon():
    weapons = [
        "Antimatter Gun",
        "Star Cannon",
        "Black Hole Ram Jet",
        "Laser Sword",
        "Laser Cannon",
        "Ion Accellerated Disc Drive",
        "Superhuman Strength",
        "Blinding Lights",
        "Ferociousness",
        "Speed of Hermes",
        "Lightning Bolts"]
    name = weapons[random.randint(0, len(weapons) - 1)]
    power = random.randint(27, 700000)
    return superheroes.Weapon(name, power)


def create_ability():
    abilities = [
        "Alien Attack",
        "Science",
        "Star Power",
        "Immortality",
        "Grandmas Cookies",
        "Blinding Strength",
        "Cute Kittens",
        "Team Morale",
        "Luck",
        "Obsequious Destruction",
        "The Kraken",
        "The Fire of A Million Suns",
        "Team Spirit",
        "Canada"]
    name = abilities[random.randint(0, len(abilities) - 1)]
    power = random.randint(45, 700000)
    return superheroes.Ability(name, power)


def create_hero(weapons=False, armours=False, health=False):

    heroes = [
        "Athena",
        "Jodie Foster",
        "Christina Aguilera",
        "Gamora",
        "Supergirl",
        "Wonder Woman",
        "Batgirl",
        "Carmen Sandiego",
        "Okoye",
        "America Chavez",
        "Cat Woman",
        "White Canary",
        "Nakia",
        "Mera",
        "Iris West",
        "Quake",
        "Wasp",
        "Storm",
        "Black Widow",
        "San Luis Obispo",
        "Ted Kennedy",
        "San Francisco",
        "Bananas"]
    name = heroes[random.randint(0, len(heroes) - 1)]
    if health:
        power = health
    else:
        power = random.randint(3, 700000)
    hero = superheroes.Hero(name, power)
    if weapons and armours:
        for weapon in weapons:
            hero.add_ability(weapon)
        for armour in armours:
            hero.add_armour(armour)
    if armours and not weapons:
        for armour in armours:
            hero.add_armour(armour)

    return hero


def create_team(heroes=[]):
    teams = [
        "Orchids",
        "Red",
        "Blue",
        "Cheese Steaks",
        "Warriors",
        "49ers",
        "Marvel",
        "DC",
        "Rat Pack",
        "The Little Red Riding Hoods",
        "Team One",
        "Generic Team",
        "X-men",
        "Team Two",
        "Golden Champions",
        "Vegan Protectors",
        "The Cardinals",
        "Winky Bears",
        "Steelsmiths",
        "Boilermakers",
        "Nincompoops"]
    name = teams[random.randint(0, len(teams) - 1)]
    team = superheroes.Team(name)
    if len(heroes) > 0:
        for member in heroes:
            team.add_hero(member)

    return team


def create_set():
    armour_pieces = random.randint(1, 300)
    weapon_pieces = random.randint(1, 300)
    ability_ct = random.randint(1, 300)
    armours = []
    abilities = []
    for _ in range(0, armour_pieces):
        armours.append(create_armour())
    for _ in range(0, weapon_pieces):
        abilities.append(create_weapon())
    for _ in range(0, ability_ct):
        abilities.append(create_ability())

    hero_set = {'weapons': abilities, 'armours': armours}
    return hero_set


# Test Armour
def test_armour():
    armour = superheroes.Hero("The Ring", 200)
    for _ in range(0, 500):
        defence = armour.defend() <= 200
        assert (defence <= 200 and defence >= 0)


# Test Hero


def test_hero_default_health():
    jodie = superheroes.Hero("Jodie Foster")
    assert jodie.health == 100


def test_hero_init_new_health():
    hero = superheroes.Hero("Jodie Foster", 600)
    assert hero.health == 600


def test_hero_start_health():
    hero = superheroes.Hero("Jodie Foster", 300)
    assert hero.start_health == 300


def test_hero_defence():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armour("Gauntlets", 30)
    jodie.add_armour(gauntlets)
    defence = jodie.defend()
    assert defence >= 0 and defence <= 30


def test_dead_hero_defence():
    hero = superheroes.Hero("Vlaad", 0)
    garlic = superheroes.Armour("Garlic", 30000)
    hero.add_ability(garlic)
    assert hero.defend() == 0


def test_hero_equip_armour():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armour("Gauntlets", 30)
    jodie.add_armour(gauntlets)
    assert len(jodie.armours) == 1
    assert jodie.armours[0].name == "Gauntlets"


def test_hero_defend_multi_armour():
    jodie = superheroes.Hero("Jodie Foster")
    gauntlets = superheroes.Armour("Gauntlets", 4000)
    science = superheroes.Armour("Science", 9000)
    jodie.add_armour(gauntlets)
    jodie.add_armour(science)
    defend = jodie.defend()
    assert defend <= 13000 and defend >= 0


def test_hero_attack():
    flash = superheroes.Hero("The Flash")
    assert flash.attack() == 0
    pesto = superheroes.Ability("Pesto Sauce", 8000)
    flash.add_ability(pesto)
    attack = flash.attack()
    assert attack <= 8000 and attack >= 4000


# Test Team


def test_team_attack():
    team_one = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    aliens = superheroes.Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = superheroes.Team("Two")
    athena = superheroes.Hero("Athena")
    socks = superheroes.Armour("Socks", 10)
    athena.add_armour(socks)
    team_two.add_hero(athena)
    assert team_two.heroes[0].health == 100

    team_one.attack(team_two)

    assert team_two.heroes[0].health <= 0


def test_team_attack_kills():
    team_one = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    aliens = superheroes.Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = superheroes.Team("Two")
    athena = superheroes.Hero("Athena")
    socks = superheroes.Armour("Socks", 10)
    athena.add_armour(socks)
    team_two.add_hero(athena)
    assert team_one.heroes[0].kills == 0
    team_one.attack(team_two)
    assert team_one.heroes[0].kills == 1


def test_team_attack_deaths():
    team_one = superheroes.Team("One")
    jodie = superheroes.Hero("Jodie Foster")
    aliens = superheroes.Ability("Alien Friends", 10000)
    jodie.add_ability(aliens)
    team_one.add_hero(jodie)
    team_two = superheroes.Team("Two")
    athena = superheroes.Hero("Athena")
    socks = superheroes.Armour("Socks", 10)
    athena.add_armour(socks)
    team_two.add_hero(athena)
    assert team_two.heroes[0].deaths == 0
    team_one.attack(team_two)
    assert team_two.heroes[0].deaths == 1


def test_team_defend():
    heroes = []
    for _ in range(0, 20):
        heroes.append(create_hero(health=20))
        print(heroes[_].health)
    team_one = superheroes.Team("One")
    for hero in heroes:
        team_one.add_hero(hero)

    deaths = team_one.defend(100)
    for hero in team_one.heroes:
        assert hero.health == 15

    assert deaths == 0

    assert team_one.defend(400) == 20


def test_revive_heroes():
    heroes = []
    for _ in range(0, 20):
        heroes.append(create_hero(health=60))

    team_one = superheroes.Team("One")
    for hero in heroes:
        team_one.add_hero(hero)

    team_one.defend(300)
    for hero in team_one.heroes:
        assert hero.health == 45
    team_one.revive_heroes()
    for hero in team_one.heroes:
        assert hero.health == 60
