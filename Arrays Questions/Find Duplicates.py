
list = [1,2,4,6,7,8,6,5,4,3,2,1,6,8,11,16,11]
dupl = set()

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(list) == len(set(list)):
        return False
    else:
        return True


result = checkIfDuplicates_1(list)
if result is True:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')


set = set(list)

def find_duplicates(list):
    for i in list:
        if list.count(i) > 1:
            dupl.add(i)
    print("The original list: ", list)
    print("The duplicates are: ", dupl)

find_duplicates(list)