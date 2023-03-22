# Given a string. Split it into 2 equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.

string_one = "aaabbb"
print(string_one)
res_first, res_second = string_one[:len(string_one)//2], string_one[len(string_one)//2:]

print(res_second, res_first)

# Given a string, determine if it consists of all unique characters.

def check_unique_chars(string):
    if string is None:
        return False
    for char in string:
        if string.count(char) > 1:
            return False
    return True


print(check_unique_chars("abcde"))
print(check_unique_chars("aabcde"))
