import random
import time
import sys
from time import sleep
from names import name_list

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

sentence = f"{name} begins their journey across the dark lands as a daemon of the netherworlds!"
slow_typing()
sleep(1)

sentence = "\n",f"{name}, Now it's time for you to choose your skill set!"
slow_typing()
sleep(1)

sentence = "\n", f"{name}, as a fledling daemon you have 3 skill points to allocate as you see fit"
slow_typing()

player_stats = {'str': 1, 'dex': 1, 'con': 1, 'health': random.randint(3,5), 'exp': 0}
print(player_stats)

def level_up():
    increase = input('Choose "str" or "dex" or con".')
    if increase.lower() == 'str':
        player_stats['str'] += 1
        print(player_stats)
    elif increase.lower() == "dex":
        player_stats['dex'] += 1
        print(player_stats)
    elif increase.lower() == "con":
        player_stats['con'] += 1
        player_stats['health'] += random.randint(3,5)
        print(player_stats)
    else:
        print('You need to choose an attribute! Try again.')
        level_up()
   
level_up()
level_up()
level_up()

bat = {"name": "bat", "health": 2, 'str': 1, 'dex': 1, 'experience': 1}
wyvern ={"name": "wyvern", "health": 10, 'str': 3, 'dex': 3, 'experience': 5}
monster = bat

def gain_experience():
    player_stats['exp'] += monster['experience']
    print("You have defeated the", monster['name'], "!!")
    print(player_stats['exp'], "is the amount of experience you have gained!")
    if player_stats['exp'] >= 5:
        level_up()
        player_stats['exp'] = 0

def monster_damage_to_player():
    damage = (monster['str'] + random.randint(1,2))
    player_stats["health"] = player_stats["health"] - damage
    print("The", monster['name'], "has hit you for,", damage, "points of damage")
    if player_stats['health'] <= 0:
        game_over()

def game_over():
    print("\nYou have been slain by", monster['name'], "it's game over!")
    input("\nPress any button to exit the game.")
    sys.exit

def player_chance_to_hit():
    to_hit = random.randint(1,100) + (player_stats['dex'] * 10)
    if to_hit >= 60:
        player_damage_to_monster()
    else:
        print("You miss the", monster['name'], ".")

def player_damage_to_monster():
    damage = (player_stats['str'] + random.randint(1,3))     
    monster["health"] = monster["health"] - damage
    print("You hit the", monster['name'], "for,", damage, "points of damage")


def monster_chance_to_hit():
    to_hit = random.randint(1,100) + (monster['dex'] *10)
    if to_hit >=65:
        monster_damage_to_player()
    else:
        print("The", monster['name'], "has missed you.")

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
    sentence = ("You spot a bat flying towards you from the ceiling!!")
    slow_typing()
    while monster['health'] > 0:
        player_chance_to_hit()
        sleep(0.5)
        monster_chance_to_hit()
        sleep(0.5)

elif choice.lower() == "left":
    sentence = "\nAs you get closer to the opening you have a distinct feeling that someones watching you from the shadows!"
    slow_typing()
    while monster['health'] > 0:
        player_chance_to_hit()
        sleep(0.5)
        monster_chance_to_hit()
        sleep(0.5)

else:
    print('You need to choose left or right.')

gain_experience()

sentence = "\nHaving defeated the fearsome bloodthirsty bat, you continue on your journey upwards to stairway you found hidden in the shadows..."
slow_typing()

sentence = "\nWalking up the stairway, you notice there's a greenish glow to the cavern lighting, it reminds you of something, but you can't quite figure out what.."
slow_typing()

sentence = "\nAs you reach the floor above you, you notice that the floor appears to have small puddles of liquid in it, you think to yourself 'not slimes please' "
slow_typing()

sentence = "\nWalking onwards from the path infront of you, the tunnel comes to a crossroads, having to choose left or right."
slow_typing()

sentence = "\nWhile contemplating this big decision a group of bats swoops through the skies from the left side!"
slow_typing()

monster = wyvern

choice = input("\nDo you take the quieter side on the Right, or go with whatever scared off those bats on the Left?")
if choice.lower() == "right":
    sentence = "\nNothing else seems to be here other than the eerie feeling of dread."
    slow_typing()

elif choice.lower() == "left":
    sentence = "\nThe bats seemed to be flying away from something quite dreadful indeed, its a baby wyvern, and it seems to think your it's lunch"
    slow_typing()
    while monster['health'] > 0:
        player_chance_to_hit()
        sleep(0.5)
        monster_chance_to_hit()
        sleep(0.5)