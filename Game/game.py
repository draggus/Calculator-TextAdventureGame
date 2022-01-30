import random
from names import name_list
from low_level_monsters import low_level_monsters_list
from mid_level_monsters import mid_level_monsters_list
from high_level_monsters import high_level_monsters_list
name = input("Do you want to choose your OWN name or go with a RANDOM one?")
if name.lower() == "own":
    name = input('What do you want to be known as?')
elif name.lower() == "random":
    name = random.choice(name_list)
else:
    print("Invalid Choice")
##this here is the starting block
print(name, "begins their journey across the dark lands as a daemon of the netherworlds!")
print(name, ", Now it's time for you to choose your skill set!")
print(name, ", as a fledling daemon you have 3 skill points to allocate as you see fit")
stats = {'str': 1, 'dex': 1, 'con': 1}
print(stats)
#this is used to create easy attribute leveling up
def level_up():
    increase = input('Choose "str" or "dex" or con".')
    if increase == 'str':
        stats['str'] += 1
    elif increase == "dex":
        stats['dex'] += 1
    elif increase == "con":
        stats['con'] += 1
    else:
        print('You need to choose an attribute! Try again.')
        level_up()
   
level_up()
print(stats)
level_up()
print(stats)
level_up()
print(stats)

##these are used as an easy to way to throw in combats
def low_encounter():
    monster = random.choice(low_level_monsters_list)
    return print(monster)

def mid_encounter():
    monster = random.choice(mid_level_monsters_list)
    return print(monster)

def high_encounter():
    monster = random.choice(high_level_monsters_list)
    return print(monster)

experience = {'exp':0}
if experience['exp'] >= 2:
    level_up()
    print(stats)
    experience['exp'] = 0

def gain_experience():
    if ['health'] <= 0:
        experience['exp'] += ['experience']
