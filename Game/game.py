import random
import time
import sys
from time import sleep
from names import name_list
from low_level_monsters import low_level_monsters_list
from mid_level_monsters import mid_level_monsters_list
from high_level_monsters import high_level_monsters_list
#This is used to slow things down
def slow_typing():
    for w in sentence:
        sys.stdout.write(w)
        sys.stdout.flush()
        time.sleep(0.05)      
name = input("Do you want to choose your OWN name or go with a RANDOM one?")
if name.lower() == "own":
    name = input('What do you want to be known as?')
elif name.lower() == "random":
    name = random.choice(name_list)
else:
    print("Invalid Choice")
##this here is the starting block
sentence = f"{name} begins their journey across the dark lands as a daemon of the netherworlds!"
slow_typing()
sleep(1.5)
sentence = "\n",f"{name}, Now it's time for you to choose your skill set!"
slow_typing()
sleep(1.5)
sentence = "\n", f"{name}, as a fledling daemon you have 3 skill points to allocate as you see fit"
slow_typing()
stats = {'str': 1, 'dex': 1, 'con': 1}
print(stats)
#this is used to create easy attribute leveling up
def level_up():
    increase = input('Choose "str" or "dex" or con".')
    if increase == 'str':
        stats['str'] += 1
        print(stats)
    elif increase == "dex":
        stats['dex'] += 1
        print(stats)
    elif increase == "con":
        stats['con'] += 1
        print(stats)
    else:
        print('You need to choose an attribute! Try again.')
        level_up()
   
level_up()
level_up()
level_up()

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
#going to make a block for combat
#something like dexterity + random number above a certain threshold to score a hit and otherwise a miss
#something similar for damage of strength + dX

sentence = "You awaken from your slumber and find yourself staring at a dark empty cave."
slow_typing()  
sleep(1.5)
sentence = "\nOn your right you see what appears to be a small silhoutte flickering in what seems to be torchlight."
slow_typing()
sleep(1.5)
sentence ="\nOn your left you see a small opening in the distance leading to possibly the upper layers?"
slow_typing()
sleep(1)
choice = input("\nDo you want to head RIGHT towards the silhoutte or LEFT towards the small opening?")
if choice.lower() == "right":
    low_encounter()
elif choice.lower() == "left":
    sentence = "\nAs you get closer to the opening you have a distinct feeling that someones watching you from the shadows!"
    slow_typing()
    low_encounter()
else:
    print('You need to choose left or right.')

