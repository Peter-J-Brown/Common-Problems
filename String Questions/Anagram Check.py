
string1 = 'god'
string2 = 'dog'

string3 = 'yesterday'
string4 = 'tomorrow'


def anagram_check(string1, string2):
    # the sorted strings are checked
    if (sorted(string1) == sorted(string2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

print("String1:  {} , String 2:  {}".format(string1, string2))
anagram_check(string1, string2)

print("String1:  {} , String 2:  {}".format(string3, string4))
anagram_check(string3, string4)
