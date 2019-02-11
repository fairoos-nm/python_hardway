
from_ = input("Enter the name of files: ")
to = input("Enter the name of file you want to copy: ")




open_file = open(from_)
read_file = open_file.read()

to_file =open(to, 'w')
to_file.write(read_file)
