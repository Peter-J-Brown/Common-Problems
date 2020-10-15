
array = [1,2,3,4,5,6,7,8,9]
new_array2 =[]
i = 0

#using custom function
def ReverseArray(array):
    new_array1 = []
    i = 0
    while i <= len(array) - 1:
        new_array1.append(array[len(array) - i - 1])
        i = i+1
    return new_array1

# using reversed iterator
for item in reversed(array):
    new_array2.append(item)

print("Reversed using ReverseArray: ", ReverseArray(array))

print("Reversed using list slicing: ", array[::-1])

print("Reversed using reversed() function: ", new_array2)
