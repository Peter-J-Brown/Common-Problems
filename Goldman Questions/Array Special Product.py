
testarray = [10,3,5,6,2]

def special_product(array, array_length):

    # Base case
    if (array_length == 1):
        print(0)
        return

    # Allocate memory for temporary arrays left[] and right[]
    left = [0] * array_length
    right = [0] * array_length

    # Allocate memory for the product array
    product = [0] * array_length

    # Left most element of left array is always 1
    left[0] = 1

    # Rightmost most element of right array is always 1
    right[array_length - 1] = 1

    # Construct the left array
    for i in range(1, array_length):
        left[i] = array[i - 1] * left[i - 1]

        # Construct the right array
    for j in range(array_length - 2, -1, -1):
        right[j] = array[j + 1] * right[j + 1]

        # Construct the product array using
    # left[] and right[]
    for i in range(array_length):
        product[i] = left[i] * right[i]

        # print the constructed prod array
    for i in range(array_length):
        print(product[i], end=' ')


special_product(testarray, len(testarray))