


def fibIterative(terms):
    sequence = [0, 1]
    if terms == 1:
        sequence = [0]
        return sequence
    if terms == 2:
        sequence = [0,1]
        return sequence

    for i in range(2, terms):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def fibRecursive(terms):
    if terms <= 1:
        return terms
    else:
        return (fibRecursive(terms - 1) + fibRecursive(terms - 2))




print("Using iterative method:")
print("The fibbonaci sequence with ", len(fibIterative(25)), "terms is:", fibIterative(25))
print("\n")

nterms = 10

print("Using recursive method:")
if nterms <= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(fibRecursive(i))


