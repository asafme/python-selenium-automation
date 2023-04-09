#Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
def even_odd(arr):
    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1
    return arr

print(even_odd([1, 2, 3, 4, 5, 6]))


#Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
def AddOne(digits):
    index = len(digits) - 1

    while (index >= 0 and digits[index] == 9):
        digits[index] = 0
        index -= 1

    if (index < 0):

        digits.insert(0, 1)

    else:
        digits[index] += 1

digits = [1, 7, 8, 9]

AddOne(digits)

for digit in digits:
    print(digit, end=' ')



