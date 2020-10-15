
testarray = [5,1,2,3,4,5,1]

def findNumber(arr, k):
   i = 0
   while i <= len(arr)-1:
        if arr[i] == k:
            return str('YES')
        else:
            i += 1
   return str('NO')

## alternate solution

'''
def findNumber(arr, k):
   if k in arr:
        return str('YES')
    else:
        return str('NO')
'''

print(findNumber(testarray, 2))