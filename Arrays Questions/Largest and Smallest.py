list = [3,55,66,12,3,106,52,2,95,43,21,157,66,15,135]

def smallest_and_largest(list):
    list.sort()
    print("Smallest element is: ", list[0])
    print("Largest element is: ", list[-1])

print("The original list: ", list)
smallest_and_largest(list)
