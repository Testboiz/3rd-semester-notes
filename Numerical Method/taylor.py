import sympy
import math

x = sympy.Symbol("x")
PYTHON_PRECISION = 15
sympy.init_printing(order='rev-lex',use_unicode=False)

# def factorial(x):
#     result = 1
#     if x > 0:
#         for i in range(1,x+1):
#             result*= i
#         return result
#     elif x == 0:
#         return result
#     else:
#         return 0

def taylorEq(f,x0,upperBound,symbol=x):
    taylorSeries = 0
    for i in range(0,upperBound+1):
        fdiff = sympy.diff(f,symbol,i).subs(symbol,x0)
        print('&',sympy.latex(sympy.diff(f,symbol,i)) + r" \\")
        taylorFrac = (symbol-x0)**i/sympy.factorial(i)
        taylorSeries += fdiff*taylorFrac
    return taylorSeries

def errorAbs(spyfunc,pyfunc, value):
    return math.abs(spyfunc.subs(value) - pyfunc(value))
def error(spyfunc,pyfunc, value):
    return spyfunc.subs(value) - pyfunc(value)
def relativeError(spyfunc,pyfunc, value):
    return error(spyfunc,pyfunc,value)/pyfunc(value)
def relativeApproximationError(spyfunc,pyfunc, value):
    return error(spyfunc,pyfunc,value)/pyfunc(value)
def relativaApproximationErrorIterative(newFunc,oldFunc,value):
    return (newFunc.subs(value)-oldFunc.subs(value))/newFunc.subs(value)
def truncationError(func,value,bound,offset = 0):
    return (func(value)*(value-offset)**bound+1)/sympy.factorial(value+1)
def roundingError():
    #this one is probably just around 1e-16 by default
    return 1e-16    
def errorAnalysisFunction(func,x0,e_ra):
    err = (func(x0) - x0)/func(x0)
    if err > e_ra:
        errorAnalysisFunction(func,err,e_ra)
    else:
        return err
#TODO iterative version

f =  2 - sympy.exp(-x)
g = sympy.exp(2*x) -1
h = sympy.ln(1-x)

print(sympy.latex(taylorEq(g,0,3).subs(x,0.0001)))