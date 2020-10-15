import string

# Function checks if input string
# has only digits or not

string1 = 'hello, this is a test 123'



def vowels_and_consonants(teststring):
    all_vowels = ''
    all_consonants = ''
    all_digits = ''
    for char in teststring:
        if char in string.ascii_letters:
            if (char == 'a') or (char == 'e')  or (char == 'i')  or (char == 'o') or (char == 'u') :
                all_vowels += char
            else:
                all_consonants += char
        if char in string.digits:
            all_digits += char

    digits = set(all_digits)
    vowels = set(all_vowels)
    consonants = set(all_consonants)

    print("All the vowels in the string: ", vowels)
    print("All the consonants in the string: ", consonants)
    print("All the digits in the string: ", digits)

vowels_and_consonants(string1)