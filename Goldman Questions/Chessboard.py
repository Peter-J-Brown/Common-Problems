# total squares on an n x n board

def countSquares(n):
    # better way to write
    # n*(n+1)*(2n+1)/6
    #return int(((n * (n + 1) / 2)* (2 * n + 1) / 3))
    return int(n*(n+1)*(2*n+1)/6)

# Driver code
n = 10
print("Count of squares is ", countSquares(n))
