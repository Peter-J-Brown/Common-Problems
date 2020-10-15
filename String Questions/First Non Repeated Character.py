
string1 = 'lllllllnnnnnrrrrorrnhhhuuieee' # with a non repeating character
string2 = 'ppppppppoooooooiiiiiiiiuuuuuuu' # with no non repeating characters

def firstNonRepeatingChar(str1):
   char_order = []
   counts = {}
   for c in str1:
      if c in counts:
         counts[c] += 1
      else:
         counts[c] = 1
         char_order.append(c)
   for c in char_order:
      if counts[c] == 1:
        return c
   return None

print("First non repeating character in string 1: ", firstNonRepeatingChar(string1))
print("First non repeating character in string 2: ", firstNonRepeatingChar(string2))