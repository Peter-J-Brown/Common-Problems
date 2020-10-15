

# using factorial function
n = 4
factorial = 1
if int(n) >= 1:
    for i in range(1,int(n)+1):
        factorial = factorial * i
print(n,"! is:",factorial)


# using recursion
num = 4
def recur_factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("NA")
    else:
        return n*recur_factorial(n-1)

print (recur_factorial(int(num)))

#using math.factorial()

import math
num = 4
print("The factorial of ", num, " is : ")
print(math.factorial(int(num)))