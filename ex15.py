from sys import argv #imported argv from sys

script, file_name = argv 
text = open(file_name)  #open(), This is the preferred way to open a file.

print(f"hi , you are running {script}.")

print(f"Here is your file name {file_name}.")

print(text.read()) #Hey! text , Do your text read 
text.close()


print("\nenter your file name agin")
file_name_agin = input("> ")

text_agin = open(file_name_agin)
print(text_agin.read())
text_agin.close()


