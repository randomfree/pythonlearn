def powersum(power,*args):
    '''return the sum of each argument raised to the specified prwer .'''
    total = 0
    for i in args:
        total +=pow(i,power)
    print(total)
    return total


powersum(2,3,4)
powersum(2,10)
