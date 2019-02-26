people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decided.")

if trucks > cars:
    pirnt("That's too many trucks.")
elif trucks < cars:
    print("May be we could take the trucks")
else:
    print("We still can't decide")


if people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, let's stay home then.")

if cars > trucks and trucks < people:
    print("Truck is best")
elif cars == truck or people == trucks:
    print("Let's make a fun!")
else:
    print("What we do mahaan")
