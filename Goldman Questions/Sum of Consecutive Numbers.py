
def consecutive_sum(target):

    num_of_solutions = 0 # tracks number of solution sets
    number_of_terms = 2 # minimum number of terms solution must contain
    a_values = []
    n_values = []

    while 2*target + number_of_terms - number_of_terms**2 > 0:
        a = (2*target + number_of_terms - number_of_terms**2) / (2*number_of_terms)
        if a % 1 == 0:
            a_values.append(int(a))
            n_values.append(int(number_of_terms))
            num_of_solutions += 1
        number_of_terms += 1

    print("There are", num_of_solutions, "unique solutions.")

    for i in range(0, len(a_values)):
        solutions = []
        for j in range(0, n_values[i]):
            solutions.append(a_values[i] + j)
        print("One set of solutions is: ", solutions, "which sums to: ", sum(solutions))

consecutive_sum(100)
