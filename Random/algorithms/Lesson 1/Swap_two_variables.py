# User inputs two numbers. one number is assigned to a variable, the other number is assigned to another variable.
# The task is to invert the variables, so that the first variable contains the second number, while the first number
# is in the second variable.

def swap_variables(a: int, b: int):
    print(f"Before swap: a = {a}, b = {b}") # a = 5, b = 10
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}") # a = 10, b = 5


test_a = 5
test_b = 10
swap_variables(test_a, test_b)







# OR

def swap_variables(a: int, b: int):
    print(f"Before swap: a = {a}, b = {b}") # a = 5, b = 10
    temp = a
    a = b
    b = temp
    print(f"After swap: a = {a}, b = {b}") # a = 10, b = 5


test_a = 5
test_b = 10
swap_variables(test_a, test_b)

# OR

def swap_variables(a: int, b: int):
    print(f"Before swap: a = {a}, b = {b}") # a = 5, b = 10
    a = a + b
    b = a - b
    a = a - b
    print(f"After swap: a = {a}, b = {b}") # a = 10, b = 5


test_a = 5
test_b = 10
swap_variables(test_a, test_b)
