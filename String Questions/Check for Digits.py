import string

# Function checks if input string
# has only digits or not

string1 = 'i contain digits 12345'
string2 = 'i do not contain digits'

def check_for_digits(teststring):
    for char in teststring:

        # If anything other than digit
        # letter is present, then return
        # False, else return True

        if char in string.digits:
            return True

    return False

# returns the digits within the string fed as input
def print_digits(teststring):
    digits = ''
    for char in teststring:
        if char in string.digits:
            digits += char
    return digits


print(string1)
print("Does this string contain digits? ", check_for_digits(string1))
print("What digits does", "\'", string1 ,"\'", "contain?", print_digits(string1))
print("\n")
print(string2)
print("Does this string contain digits? ", check_for_digits(string2))
