from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Here we copying contonts of {from_file} to {to_file}.")

in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} byte long")

print(f"Dose the output file exist? {exists(to_file)}")

print("Ready, hit RETURN to continue, CRLT-C to abort.")

input()

out_file = open(to_file, 'w')
out_file.write(in_data)
print("Allright, all done.")

out_file.close
in_file.close
