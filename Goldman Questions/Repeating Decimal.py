
def repeating_decimal(numer, denom):

    negative = False

    if denom == 0:
        return 'Not defined'
    if numer == 0:
        return '0'

    if 0 > numer*denom:
        negative = True
    if numer % denom == 0:
        return str(numer / denom)

    numerator = abs(numer)
    denominator = abs(denom)

    if negative == True:
        output = '-' + str(numerator // denominator)
    if negative == False:
        output = str(numerator // denominator)

    output += '.'

    num_q = []
    while True:
        rem = numerator % denominator

        if rem == 0:
            for i in num_q:
                output += str(i[-1])
            break
        numerator = rem*10
        q = numerator // denominator

        if [numerator, q] not in num_q:
            num_q.append([numerator, q])

        elif [numerator, q] in num_q:
            ind = num_q.index([numerator, q])
            for i in num_q[:ind]:
                output += str(i[-1])

            output += "("
            for i in num_q[ind:]:
                output += str(i[-1])
            output += ")"
            break

    print(output)
    
repeating_decimal(-1,3)