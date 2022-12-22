from math import sqrt
import random, numpy as np
random.seed(2) #? optional in the code, required by the test

#incomplete code

V0 = 2 #beginning value
step = 2 #new calcs every 2 volts
#uncertainty on voltage 3%
#uncertainty on current intensity 6%

u1 = random.random()
u2 = random.random()

#choosing which
V = lambda i, r: i*r #placeholder for the function
V_delta = lambda x, a, b: a+(b*(x+step))

BM_x = lambda u1, u2: sqrt((-2) * (np.log(u1))) * (np.cos((2 * np.pi * u2))).real
BM_y = lambda u1, u2: sqrt((-2) * (np.log(u1))) * (np.sin((2 * np.pi * u2))).real #I should stop using lambdas like this, also BM means Box Mueller

#code up to here is about the general thing

#start from 2V and obtain 10 measurements of voltage and current intensity (associating it to each resistance value)

print("V\t I")
while R < 200: # Ohms
    T1 = V(x, a, b) #analytical values
    T2 = V_delta(x, a, b)

    V_random1 = sigma * BM_x(u1, u2) + T1 
    V_random2 = sigma * BM_y(u1, u2) + T2
    print(f"{x}\t{T_random1}\n{x+sigma}\t{T_random2}")
    x += 2*step