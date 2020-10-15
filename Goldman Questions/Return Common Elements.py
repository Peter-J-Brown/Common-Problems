list1 = [1,2,3,4,5,6,7,8,9]
list2 = [7,8,9,10,11,12,13]

def findCommon(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    common = set()
    for i in set1:
        if i in set2:
            common.add(i)
    return common

print("The common elements are: ", findCommon(list1,list2))