#a function that returns true if the input number is prime and false if its not, using a self created algorithm
def PrimeCheck(number):
    a=1
    while ( (((number-1)/2)-a) / ((2*a)+1) ) >= 1:
        if ( (((number-1)/2)-a) / ((2*a)+1) ) % 1 == 0:
            return False
        a+=1
    return True