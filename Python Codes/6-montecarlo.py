from math import sqrt
import random, numpy as np
random.seed(2) #? optional

#incomplete code

x = 1
sigma = 1
u1 = random.random()
u2 = random.random()


V = lambda x: x #placeholder
V_delta = lambda x, a, b: a+(b*(x+sigma))

BM_x = lambda u1, u2: sqrt((-2) * (np.log(u1))) * (np.cos((2 * np.pi * u2))).real
BM_y = lambda u1, u2: sqrt((-2) * (np.log(u1))) * (np.sin((2 * np.pi * u2))).real #I should stop using lambdas like this, also BM means Box Mueller

print("x\t T")
while x < 200: # Ohms
    T1 = V(x, a, b)
    T2 = V_delta(x, a, b)
    V_random1 = sigma * BM_x(u1, u2) + T1 
    V_random2 = sigma * BM_y(u1, u2) + T2
    print(f"{x}\t{T_random1}\n{x+sigma}\t{T_random2}")
    x += 2*sigma