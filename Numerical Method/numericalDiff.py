import math
import enum

class Method (enum):
    foward = 0
    middle = 1
    backward = 2

def choose(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


def numericalDifferentiation(func : function, input : float,  h : float, order : int, method : Method):
    nominator = 0
    denominator = h**order
    match(method):
        case Method.foward:
            for i in range(order + 1):
                nominator += (-1)**(order-i) * choose(order,i) * func(input + i * h)
        case Method.middle:
            for i in range(order + 1):
                nominator += (-1)**i * choose(order,i) * func(input + i * h)
        case Method.backward:
            for i in range(order + 1):
                nominator += (-1)**i * choose(order,i) * func(input - (order/2 - i) * h)
    return nominator/denominator
