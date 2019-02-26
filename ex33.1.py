
def test():
    i = 0
    numbers = []
    limit = int(input("Enter your limit: "))
    incri_value = int(input("Enter your incriment value: "))
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + incri_value
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        
    print("The numbers")
    
    for num in numbers:
        print(num)
test()
