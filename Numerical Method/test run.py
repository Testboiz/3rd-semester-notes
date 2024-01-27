import math 
func = lambda x : x**2 * math.sin(x**2)

sum = func(0.5) +  func(0.8) + func(1.1) + func(1.4) + func(1.7) + func(2)

print(sum * (2-0.5)/2*5)