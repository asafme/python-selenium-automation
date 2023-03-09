
n = int(input("Enter number"))
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)









def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5))



a = input ()

digits = "02468"

even = 0
odd = 0

for i in a:
    if i in digits:
        even += 1
    else:
        odd += 1

print ("Even:% d, odd:% d"% (even, odd))



def count_even_odd(n):
    even_count = 0
    odd_count = 0
    while (n > 0):
        rem = n % 10
        if (rem % 2 == 0):
            even_count += 1
        else:
            odd_count += 1

            n = int(n / 10)
        print ( "Even count : " , even_count)
        print ("/nOdd Count : ", odd_count)
        if (even_count % 2 == 0 and
                        odd_count % 2 != 0):
            return 1
        else:
            return 0

