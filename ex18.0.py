# This one is like your script with argv

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} , arg2: {arg2}")

def print_two_agin(arg1, arg2):
    print(f"arg1: {arg1} , arg2: {arg2}")

def print_one_arg(arg):
    print(f"arg : {arg}")


def print_none():
    print("I got nothing!")




print_two("nm", "fairoos")
print_two_agin("Zed", "shaw")
print_one_arg("First")
print_none()
