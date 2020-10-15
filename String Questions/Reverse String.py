
testString = 'hello this is a test'
reversed_string = ''

## method using list slicing
def reverse_String_Slice(string):
    reversedString = string[::-1]
    print(reversedString)


# method using custom function
def reverse_String_Custom(string):
    list = []
    new_string = ''
    i = 0
    while i <= len(string) - 1:
        list.append(string[len(string) - i - 1])
        i = i+1
    for element in list:
        new_string += element

    print("The reversed string is: ", new_string)


# using custom function
reverse_String_Custom(testString)

## using list slicing
reverse_String_Slice(testString)

# using reversed iterator
for char in reversed(testString):
    reversed_string += char
print("Reversed iterator: ", reversed_string)