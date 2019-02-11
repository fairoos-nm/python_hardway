name = input("enter your name")
print("Hi! {} are you ready to go.".format(name))
filename = input('enter your file name \n >>')
open_text = open(filename)
print(open_text.read())
open_text.close() #to close opned text
