print("""You enter a dark room with two doors.)
Do you go through door #1 or door #2 or door #3?""")
door = input(">")

if door == "1":
    print("There's a gaint bear here eating a chees cake.")
    print("What do you do?")
    print("1.Take the cake.")
    print("2.Screme at the bear")

    bear = input(">")

    if bear == "1":
        print("The bear eats your facw off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is porbablly better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1.Blueberries.")
    print("2.Yellow jacket clothespins.")
    print("3.Understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity  == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job")

elif door == "3":
    print("Here You can see two boxs, Golden\u261f and Silver\u261e. open any one.")
    selected_box = input("> ")
    if selected_box == "Golden":
        print("Here is two keys and two shelfs, Select any key ,key1 \u0fc8 or key2 \u0fc5")
        selected_key = input("> ")
        if selected_key == "key1":
            print("Here is two butons white  \u25a1 and black  \u25a0 , press any one \u23fa ")
            pressed_button = input("> ")
            if pressed_button == "white":
                print("Open the secrect door under your leg and go to paradies  \u2665")
            elif pressed_button == "black":
                print("The bomb is ready to blast \u231a after you red this! get ready for deth \u2620")
            else:
                print("Good by")
        elif selected_key == "key2":
            print("Sorry! You lost this game, It is like lottery challenge!")
            print("Take little gift under the table.")
    elif selected_box == "Silver":
        print("why you did't select the golden one?.")
        print("There are lot of chance in golden, but you lost")
        print("Sorry! it is only a Rahmath biriyani tickket for you! \u26df")
        print("\u06de Don't worry ! it is very tasty \101db")
