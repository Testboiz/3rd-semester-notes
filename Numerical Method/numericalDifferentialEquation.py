from decimal import *
def diffEq(x,y):
    return x+y

def eulerFunc(func,h,x,y):
    return y+h*(func(x,y))

def euler(func, h, startValue, functionValueAtStart,valueToApprox):
    steps = round(abs(valueToApprox-startValue)/h)
    x = startValue
    y_prev = functionValueAtStart
    y =eulerFunc(func,h,x,y_prev)
    print(y)
    for _ in range(1,steps):
        y_prev = y
        x+=h
        y =eulerFunc(func,h,x,y_prev)
        print(y)
    return y+functionValueAtStart
def heun(func, h, startValue, functionValueAtStart,valueToApprox):
    steps = round(abs(valueToApprox-startValue)/h)
    x = startValue
    y_prev = functionValueAtStart
    y = y_prev + (h/2)*(func(x,y_prev) + func(x+h,eulerFunc(func,h,x,y_prev)))
    print(y)
    for _ in range(1,steps):
        x+=h
        # euler invocation for the last term
        _ef = eulerFunc(func,h,x,y)
        y = y + (h/2)*(func(x,y) + func(x+h, _ef) )
        print(y)
    return y
def rungeKuttaFourthOrder(func,h,startValue,functionValueAtStart,valueToApprox):
    steps = round(abs(valueToApprox-startValue)/h)
    y_prev = functionValueAtStart
    x = startValue
    print(y_prev)
    for i in range(steps):
        if i != 0:
            x+=h
        k_1 = h*(func(x,y_prev))
        k_2 = h*(func(x+(h/2), y_prev + (k_1/2)))
        k_3 = h*(func(x+(h/2), y_prev + (k_2/2)))
        k_4 = h*(func(x+h ,y_prev + k_3))
        y_prev = (1/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
        print(y_prev)
    return y_prev

def rungeKuttaThirdOrder(func,h,startValue,functionValueAtStart,valueToApprox):
    steps = round(abs(valueToApprox-startValue)/h)
    y_prev = functionValueAtStart
    x = startValue
    print(y_prev)
    for i in range(steps):
        if i != 0:
            x+=h
        k_1 = h*(func(x,y_prev))
        k_2 = h*(func(x+(h/2), y_prev + (k_1/2)))
        k_3 = h*(func(x+h,y_prev-k_1+2*k_2 ))
        y_prev += (1/6)*(k_1+4*k_2+k_3) 
        print(y_prev)

ODE1 = lambda x,y : x+y
ODE2 = lambda x,y: 1+y**2
ODE3 = lambda x,y : 2*x+2*y



def test(h,toFind):
    steps = round(toFind/h)
    x_h = 0
    for _ in range(steps):
        x_h += h
        print(x_h)

print("euler")
euler(ODE1,0.02,0,1,0.1)
print("heun")
heun(ODE1,0.02,0,1,0.1)
print("RK")
rungeKuttaThirdOrder(ODE2,0.1,0,0,0.2)
print("soal euler")
euler(ODE3,Decimal(12)/Decimal(100),Decimal(0),Decimal(1),Decimal(6)/Decimal(100))
