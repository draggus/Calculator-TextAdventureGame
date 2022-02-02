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

player_stats = {'str': 1, 'dex': 1, 'con': 1,}
print(player_stats)
player_stats['health'] = player_stats['con'] * random.randint(3,5) 
#this is used to create easy attribute leveling up
def level_up():
    increase = input('Choose "str" or "dex" or con".')
    if increase == 'str':
        player_stats['str'] += 1
        print(player_stats)
    elif increase == "dex":
        player_stats['dex'] += 1
        print(player_stats)
    elif increase == "con":
        player_stats['con'] += 1
        player_stats['health'] = player_stats['con'] * random.randint(3,5)
        print(player_stats)
    else:
        print('You need to choose an attribute! Try again.')
        level_up()
   
level_up()
level_up()
level_up()

##these are used as an easy to way to throw in combats
##needs some work to get the health bars to function as intended, will learn it in due time :)
def low_encounter():
    
    monster = random.choice(low_level_monsters_list)
    while player_stats['health'] > 0:
        if monster('health') > 0:
            player_cth()
            monster_cth()
        elif monster[0] <=0:
            gain_experience()
        elif player_stats['health'] <= 0:
            print("Unfortunately you have died!")

def mid_encounter():
    monster = random.choice(mid_level_monsters_list)
    while player_stats['health'] > 0:
        if monster[0] > 0:
            player_cth()
            monster_cth()
        elif monster[0] <=0:
            gain_experience()
        elif player_stats['health'] <= 0:
            print("Unfortunately you have died!")

def high_encounter():
    monster = random.choice(high_level_monsters_list)
    while player_stats['health'] > 0:
        if monster[0] > 0:
            player_cth()
            monster_cth()
        elif monster[0] <=0:
            gain_experience()
        elif player_stats['health'] <= 0:
            print("Unfortunately you have died!")


experience = {'exp':0}
if experience['exp'] >= 2:
    level_up()
    print(player_stats)
    experience['exp'] = 0

def gain_experience():
    experience['exp'] += ['experience']
#going to make a block for combat
#something like dexterity + random number above a certain threshold to score a hit and otherwise a miss
#something similar for damage of strength + dX
def player_damage():
    player_stats['health'] = player_stats['health'] - (player_stats['str'] + random.randomint(1,3))

def player_cth():
    to_hit = random.randomint(1,100) + (player_stats['dex'] * 10)
    if to_hit >= 60:
        monster_damage()
    else:
        print("You miss having rolled,", to_hit, ".")

monster = high_encounter or mid_encounter or low_encounter

def monster_damage():
    monster[0] = monster[0] - (monster[1] + random.randomint(1,2))

def monster_cth():
    to_hit = random.randomint(1,100) + (monster[2] *10)
    if to_hit >=65:
        player_damage()
    else:
        print("The", monster, "has missed you rolling,", to_hit, ".")

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

