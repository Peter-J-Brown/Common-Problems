'''
def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

    # Function to left Rotate arr[] of size n by 1*/

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
'''

## rotates an array left by d places, for an array arr of size n
def leftRotate(arr, d, n):
    for i in range(d):
        temp = arr[0]
        for i in range(n - 1):
            arr[i] = arr[i + 1]
        arr[n - 1] = temp


# utility function to print an array */
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end =" ")
    # Driver program to test above functions */

arr = [1, 2, 3, 4, 5, 6, 7]
print("Array to be rotated: ", arr)
print("Left rotating by 2 places:")
leftRotate(arr, 2, len(arr))
printArray(arr, len(arr))