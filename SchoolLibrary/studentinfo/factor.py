import math

def factorial(n):

    if n == 0:
        n = 1
        return n

    else:
        #c = int(factorial(n-1))
        #d = c * n
        #return d
        return int(factorial(n-1)*n)

def compute_pi():
    a = 2*math.sqrt(2)/9801
    e = int(a)
    #print e
    k = 0
    total = 0
    while True:
        numerator = factorial(4*k) * (1103 + 26390*k)
        denominator = factorial(k)**4 * 396**(4*k)
        print numerator, "/", denominator
        c = float(numerator)
        d = float(denominator)
        b = c / d
        print b
        total += b    # Summation
        if abs(b) < 1e-15:
            break
        k += 1        # k from 0 => infinity
        print "see me"

    result = e*total
    resultint = float(result)
    print resultint
    return float(1/result)

    return compute_pi()

if __name__ == '__main__':
    factorial(4)
    print compute_pi()



#1/pi = 2(square root of 2)/9801 (k = 0, through infinity) (4k)!(1103+26390k)/(k!)+(396)^4k

#While true:
#   num = factorial(4k)x(1103....)
#   den = factorial(k)**4x(396)
#   b = num/den
#   total t = b
#   result = a.total
#   k +=1
#return 1/result
#
#def compute_pi():
#   a = 2/squarerootof(2)/9801
#   k = 0
#
#
#   result = a x total
#   k += 1
#   return 1/result
#
#