from sys import argv

script, user_name = argv
def stars():
    
    count = 1
    for j in range(7):
        if j == 0:
            print("*")
        if j == 1:
            print("**")
        if j == 2:
            print("***")
            nm = input("****")

        if j == 4:
            print("***")
        if j == 5:
            print("**")
        if j == 6:
            print("*")
    return"Thanks for response.\n"
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few question.")
print(f"Do you like me {user_name}?.")
likes  = input(stars())

print(f"Where do you live {user_name}")
lives = input(stars()) 

print("What kind of computer do you have?")
computer = input(stars())

print(f"""
Alright, so you said {likes} about liking me.
you lives in {lives} . Not sure where there is.
And you have a {computer} computer. Nice.
"""
)
