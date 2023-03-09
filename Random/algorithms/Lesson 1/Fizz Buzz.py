# Write a program that prints the numbers from 1 to 100.
# But for multiples of 3 print "Fizz" instead of the number.
# and for the multiples of five print "Buzz".
# For numbers which are multiples fo both three and five print "FizzBuzz"
def fizzbuzz(n: int):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)



fizzbuzz(100) # can't forget this!!


