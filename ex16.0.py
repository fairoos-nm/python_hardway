from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("if you don't want it, hit crlto - c (^c).")
print("if you do want that, hit RETURN.")

input("?")

print("Opening the file ...")
target = open(filename,'w')

print("Truncating the file .Goodbay!")
target.truncate() #remove all things in current file

print("Now I'm going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("finely we are close it.")
target.close()
