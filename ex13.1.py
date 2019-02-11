from sys import argv

one, two, three, four, five = argv
#here we combime both argv and input
name = input("hi what is your name.")

print("name of script you are given:", one)
print("first variable you are given:", two)
print("second variable you are given:", three)
print("last second variable you are given:", four)
print("sorry i am the final one variable you are given:", five)
print ("hi {} welcome.".format(name))
