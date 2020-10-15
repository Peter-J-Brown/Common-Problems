
from collections import *

testarray1 = [1,2,3,4,5,6,7,7,7,7,7,7]

testarray2 = [1,2,3,4,5,6,7,8,9,9,9,9]

testarray3 = [1,1,1,1,1,1,2,2,2,2,2,2]

def find_majority(array):

   c = Counter(array)
   value1, count1 = c.most_common()[0]
   value2, count2 = c.most_common()[1]

   if count1 > len(array)/2:
       print(value1, "is the most common element with", count2, " instances and it is the majority element.")

   if count1 == len(array) / 2:
       if count1 != count2:
           print(value1, "is the most common element with", count1, "instances out of", len(array), "values, and it is the majority element.")
       if count1 == count2:
           print(value1, "and", value2, "appear equal numbers of times with", count1, "instances each out of ", len(array), "values, but there is no majority element.")

   if count1 < len(array)/2:
       print(value1, "is the most common element with", count1, " instances out of", len(array), "values, but there is no majority element.")


print(testarray1)
find_majority(testarray1)
print("\n")

print(testarray2)
find_majority(testarray2)
print("\n")

print(testarray3)
find_majority(testarray3)