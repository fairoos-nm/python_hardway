def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

what = iq/2*weight-height+age
something = (height - iq/2*weight)
print(age + something)
print(what)
