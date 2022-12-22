from math import sqrt
import random, numpy as np
random.seed(2) #? optional in the code, required by the test

#incomplete code

V = 1 #beginning value
step = 1 #new calcs every 2 volts
#uncertainty on voltage 3%
#uncertainty on current intensity 6%
R = 200

u1 = random.random()
u2 = random.random()

I = lambda v, r: v/r

BM_x = lambda u1, u2: sqrt((-2) * (np.log(u1))) * (np.cos((2 * np.pi * u2))).real
BM_y = lambda u1, u2: sqrt((-2) * (np.log(u1))) * (np.sin((2 * np.pi * u2))).real #I should stop using lambdas like this, also BM means Box Mueller

#code up to here is about the general thing

#start from 2V and obtain 10 measurements of voltage and current intensity (associating it to each resistance value)

print("V\t I")
while V < 10: # Ohms
    I1 = I(V, R) #analytical values
    I2 = I(V+step, R)
    #FORMULA IS I_RANDOM = UNCERTAINTY * BOXMUELLERVALUE + ANALYTICALVALUE
    I_random1 = (5*I1/100) * BM_x(u1, u2) + I1 
    I_random2 = (5*I2/100) * BM_y(u1, u2) + I2
    print(f"{V}\t{I_random1}\t\tAssociated resistance: {V/I_random1}\n{V+step}\t{I_random2}\t\tAssociated resistance: {(V+step)/I_random2}")
    V += 2*step