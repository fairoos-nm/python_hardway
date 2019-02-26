"""list indexing"""

flowers = ["Rose", "Jasmin", "Lilly", "sun_flower"]

print(flowers[0]) #Rose

print(f"I love {flowers[0]} and I hate {flowers[3]}.")

for flower in flowers:
    if flower == "Lilly":
        print("I am Lilly.My index number is :", 2)
        print("Let's us test it.")
        if flowers[2] == "Lilly":
            print("You are correct, i am Lilly with index number 2")
        else:
            print("sorry")
