
odds = []
first_odd = 0

def oddNumbers(l,r):
    if l % 2 == 0:
        first_odd = l+1
        value = first_odd
        while value <= r:
            odds.append(value)
            value += 2

    if l % 2 != 0:
        first_odd == l
        value = first_odd
        while value <= r:
            odds.append(value)
            value += 2

    return odds

print(oddNumbers(0,1))