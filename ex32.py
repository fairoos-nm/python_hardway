the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'ornages', 'pears', 'apricots']
change = [1, 'pennies', 2,'dimes', 3, 'quarters']

#this first of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type{fruit}")

#also we can go through mixed list too
#notice we have to use {} since we don't know what's in it
for i in change :
    print(f"I got {i}")

#We can also build lists, first start with an empty one

elements = []

#then use the range function to do 0 to 5 counts

for i in range(0, 6):
    print(f"Adding {i} to the list")
    #append is a function that lists understand
    elements.append(i)
print (elements)

for i in elements:
    print(f"Element was:{i}")
