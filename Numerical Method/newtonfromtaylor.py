import sympy as sp
x = sp.symbols("x")
def newtonfromtaylor(x):
    return x - (4*x*x-2*x-1)/(8*x-4)
symbollicNewtonFromTaylor = x - (4*x**2-2*x-1)/(8*x-4)
iter = 0
print(iter)
for i in range(10):
    iter = newtonfromtaylor(iter)
    print(iter)
# print(symbollicNewtonFromTaylor.subs(0))