import math

def riemannSum(func, boxAmnount, leftInterval, rightInterval):
    boxSize = abs(leftInterval-rightInterval)/boxAmnount
    func_eval = 0
    for i in range(int(round(boxSize))+1):
        step = i * abs(leftInterval-rightInterval)/boxSize
        func_eval+= func(leftInterval + step)
        print(f'|x{i}|{round(leftInterval + step,3)} | {func(leftInterval + step)}')
    return boxAmnount *  func_eval

def trapezoidalRule(func, boxAmnount, leftInterval, rightInterval):
    boxSize = abs(leftInterval-rightInterval)/boxAmnount
    func_eval = 0
    for i in range(int(round(boxSize))+1):
        step = i * abs(leftInterval-rightInterval)/boxSize
        func_eval+= 2* func(leftInterval + step)
        print(f'|x{i}|{round(leftInterval + step,3)} | {  func(leftInterval + step)}')
    func_eval -= func(leftInterval) + func(rightInterval)
    return  (boxAmnount/2) *  func_eval

def midpointRule(func, boxAmnount, leftInterval, rightInterval):
    boxSize = abs(leftInterval-rightInterval)/boxAmnount
    func_eval = 0
    for i in range(boxAmnount):
        midPoint = i + 0.5
        input = boxSize * midPoint
        func_eval+= func(input)
        print(f'|x{i}|{round(leftInterval + midPoint,3)} | {  func(leftInterval + midPoint)}')
    return boxAmnount * func_eval

def simpsonOneThird(func,boxAmnount,leftInterval,rightInterval):
    boxSize = abs(leftInterval-rightInterval)/boxAmnount
    func_eval = 0
    for i in range(0,boxAmnount+1):
        x_r = 0
        if i == 0:
            func_eval+=func(leftInterval)
        elif i == boxAmnount:
            func_eval+=func(rightInterval)
        else:
            x_r = (i/boxAmnount)*(leftInterval-rightInterval)
            if i%2 == 0:
                func_eval+=2*func(x_r)
            else:
                func_eval+=4*func(x_r)
        print(f'|x{i}|{round(leftInterval + x_r,3)} | {  func(leftInterval + x_r)}')
    return func_eval * boxSize/3
def simpsonThreeEights(func,boxAmnount,leftInterval,rightInterval):
    boxSize = abs(leftInterval-rightInterval)/boxAmnount
    func_eval = 0
    for i in range(0,boxAmnount+1):
        x_r = 0
        if i == 0 :
            func_eval+=func(leftInterval)
        elif i == boxAmnount:
            func_eval+=func(rightInterval)
        else:
            x_r = (i/boxAmnount)*(leftInterval-rightInterval) 
            if i%3 == 0:
                func_eval+=2*func(x_r)
            else:
                func_eval+=3*func(x_r)
        print(f'|x{i}|{round(leftInterval + x_r,3)} | {  func(leftInterval + x_r)}')

    return func_eval * (3*boxSize)/8

soal1 = lambda x : x**2 * math.cos(x**2)
soal2 = lambda x : math.exp(x)/(1+x)
soal3 = lambda x : x**2 * math.sin(x**2)
soal4 = lambda x : math.exp(x)
contoh1 = lambda x : 1/(1+x) 
tugas = lambda x : 2*x*math.exp(3*x)
print(riemannSum(soal1,0.2,1.5,2.5))
print(riemannSum(soal2, 0.2,1.7,3.3))
print(trapezoidalRule(soal3,0.3,0.5,2))
print(trapezoidalRule(soal4,0.2,1.7,3.3))
print(simpsonOneThird(contoh1,8,1,0))
print("tugas")
print(trapezoidalRule(tugas,0.5,3,6))
print(simpsonOneThird(tugas,6,3,6))
