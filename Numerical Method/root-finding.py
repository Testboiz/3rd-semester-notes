import sympy
import math
import tabulate

table = []
table_regula_falsi = []

class tableHeader:
    def __init__(self, iter, a, c, b, func, interval):
        self.iter = iter
        self.a = a
        self.c = c
        self.b = b
        self.f_a = func(a)
        self.f_c = func(c)
        self.f_b = func(b)
        self.interval = interval
        self.length = math.fabs(a-c)

x = sympy.symbols("x")

class Modes:
    BISECTION = 0
    REGULA_FALSI = 1

def polynomialMaker(*coefficients, symbol=x):
    equation = 0
    coefficientList = list(coefficients)
    coefficientList.reverse()
    for power,coef in enumerate(coefficientList):
        equation += coef * symbol ** power
    return equation

print(polynomialMaker(1,2,3))
def interpolator(left, right,func, mode):
    match mode:
        case Modes.BISECTION:
            return (left+right)/2
        case Modes.REGULA_FALSI:
            return right - (((func(right))*(right-left))/(func(right) - func(left)))
        case _:
            return None
def bisectionIterative(func, leftGuess, rightGuess, errorTreshold):
    it = 1
    mid = interpolator(leftGuess,rightGuess,func, Modes.BISECTION)
    leftBound = func(leftGuess)
    rightBound = func(rightGuess)
    if leftBound > 0 and rightBound > 0 \
    or leftBound < 0 and rightBound < 0 :
        return 
    else:
        while math.fabs(func(mid)) > errorTreshold:
            interval = ""
            mid = interpolator(leftGuess,rightGuess,func, Modes.BISECTION)
            if func(mid) * func(leftGuess) < 0:
               rightGuess = mid
               interval = "[a-c]"
            else:
               leftGuess = mid
               interval = "[c-b]"
            table.append([it,leftGuess,mid,rightGuess,func(leftGuess),func(mid),func(rightGuess),interval,math.fabs(leftGuess-rightGuess)])
            it+=1
        return mid
    
def regulaFalsi(func, leftGuess, rightGuess, errorTreshold):
    mid = interpolator(leftGuess,rightGuess,func, Modes.REGULA_FALSI)
    leftBound = func(leftGuess)
    rightBound = func(rightGuess)
    if leftBound > 0 and rightBound > 0 \
    or leftBound < 0 and rightBound < 0 :
        return 
    else:
        while math.fabs(func(mid)) > errorTreshold:
            interval = ""
            mid = interpolator(leftGuess,rightGuess,func, Modes.REGULA_FALSI)
            if func(mid) * func(leftGuess) < 0:
                rightGuess = mid
                interval = "[a-c]"
            else:
                leftGuess = mid
                interval = "[c-b]"
            table_regula_falsi.append([leftGuess,mid,rightGuess,func(leftGuess),func(mid),func(rightGuess),interval,math.fabs(leftGuess-rightGuess)])
        return mid
func = lambda x : 2*x**2 - 3*x - 5 
func2 = lambda x : (2.71828**x)-5*x**2
print(func2(0))
# bisectionIterative(func, -7,0,0.0001)
# regulaFalsi(func, -7,0,0.0001)
print(bisectionIterative(func2,2,3.1457,0.001))
print(tabulate.tabulate(table,headers=["NO",'a','c','b','f(a)','f(c)','f(b),','Interval','Lebar']))
# print(tabulate.tabulate(table_regula_falsi,headers=['a','c','b','f(a)','f(c)','f(b),','Interval','Lebar']))