# When user enters a number, its factorial is displayed.

def factorial(number: int):
    result = 1
    for i in range(2, number + 1):
        result = result * i # result *=i

    print(f"Factorial of {number} is {result}")


test_number = 5 # 1 * 2 * 3 * 4* 5 = 120
factorial(test_number)


