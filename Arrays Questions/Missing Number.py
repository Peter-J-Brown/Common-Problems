
sorted_list10 = [1,2,3,4,5,7,8,9,10,11,13,15,16,17,18,19,20]

print(sorted_list10[-1])
def find_missing(array):
    return [x for x in range(array[0], array[-1]+1) if x not in array]

print("This missing number is:", find_missing(sorted_list10))
