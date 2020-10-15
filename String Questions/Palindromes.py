
string1 = 'ABCBA'
string2 = 'ABBA'
string3 = 'i am not a palindrome'

def palindrome_checker(teststring):

    if len(teststring) % 2 == 0:
        for i in range(0, int((len(teststring)/2) - 1)):
            if teststring[i] == teststring[len(teststring) -1 - i]:
                print("This string is a palindrome")
            else:
                print("This string is not a palindrome")
                return


    if len(teststring) % 2 != 0:
        for i in range(0, int((len(teststring) - 1)/2 - 1)):
            if teststring[i] == teststring[len(teststring) -1 - i]:
                print("This string is a palindrome")
            else:
                print("This string is not a palindrome")
                return


print("String 1 is: ", string1)
palindrome_checker(string1)
print("\n")

print("String 2 is: ", string2)
palindrome_checker(string2)
print("\n")

print("String 3 is: ", string3)
palindrome_checker(string3)