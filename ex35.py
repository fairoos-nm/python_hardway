from sys import exit
import time
from tqdm import tqdm
def gold_room():
    print("This room full of gold. How much do you take?.")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, You're not greedy, you win! ")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("How fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it now")

            bear_moved = True

        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
def key():
    print("take the key and open the 102 page of the red book")
    time.sleep(3)
    print("pag no : 102::: MANDRA:: HOM HOM GREEM HOOO HOOO HOOO")
    print("Read mandra loudly 3 times")
    time.sleep(4)
    for i in tqdm(range(10)):
        time.sleep(.5)
        pass
    print()
    for i in range(4):
        print("HA ha .... ", sep='', end=' ', flush = True)
        time.sleep(.5)
    print("PeTTu MooNee...!")
    help = True
    print("HI I AM kultuboom")
    print()
    print("Why you came here! Have you want any help")
    while True:
        choice = input("> ")
        if choice == "yes" and help:
            print("Take this coin and keep this mandra with you \n When you want my help Call Me using this mandra")
        elif "no" in choice:
            print("OK YOU CAN GO NOW:")
            print("drink this water and go")
            help = False
        elif choice == "ok" and help :
            dead("see You")
        elif choice != "ok" and help:
            dead("I will Kill YoU")               

def cthulhu_room():
    print("Here you see the great evil cthulhu.")
    print("He, It, wharever stares at you and you go insane.")
    print("Do you flee for your life or ear your life or eat your hear?")
    print("A locked box there Use your fingur print to open box")
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in  choice:
        dead("well that was tasty!")
    elif "fingur" in choice:
        key()
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until  you starve.")

start()
    
        
