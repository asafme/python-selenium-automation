# Our code generates a random three-digit number and has to sum all its digits.
# For example, if a number is 349, the code has to print the number 16, because 3 + 4 + 9 = 16.

def sum_of_three(n: int):
    result = 0
    original_n = n
    while n != 0:
        result = result + (n % 10)
        n = n // 10

    print(f"Sum of all digits {n} is {result}")


test = 125
sum_of_three(test)

