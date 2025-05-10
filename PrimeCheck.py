def PrimeCheck(number):
    a=1
    while ( (((number-1)/2)-a) / ((2*a)+1) ) >= 1:
        if (((number-1)/2)-a) % ((2*a)+1) == 0:
            return False
        a+=1
    return True
def f(mn, mx):
    return 2*((2 * mn * mx) + mn + mx)+1


def a(c):
    r = int(((c**0.5)-1)/2)
    if r<1:
        return 1
    return r
def PrimeCheck2(n):
    if n < 3:
        return

    if n%2 == 0:
        return False
    index= [1, a(n)] # (min, max)
    while True:

        k = f(index[0], index[1])
        if n == k :
            return False
        
        elif n > k:

            if index[0] == index [1] :
                index[0] , index[1] = 1 , index[1] + 1
            
            else:
                index[0] = index[0] + 1
        
        else:

            if index[0] == 1:
                return True
            
            else:
                index[0] , index[1] = 1 , index[1] + 1
