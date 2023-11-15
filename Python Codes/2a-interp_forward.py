from math import factorial as fact
import numpy as np

def fallfact(a, k): #this is to evaluate the r(r-1)(r-2)... sequence but could also be rewritten
    if k == 0:
        return 1
    else:
        return a * fallfact(a-1, k-1)

y_points = np.array([1.51295, 1.79024, 2.04887, 2.27976, 2.47567, 2.63142, 2.74432, 2.81448, 2.84532, 2.84409])

X = 0.55 #value where we are interpolating
r = (X - 0.5) / 0.15 #relative distance between closest point and interpolation value: could be automated but too lazy
max_order = 8
diff = [] #empty, will be filled with differences every time
alldiff = [y_points] #will be a list of arrays

for step in range(max_order + 1): # do this difference operation (order) times
    for i in range(len(y_points) - 1): #on the list of delta values, take the previous array and apply differences, append result to differences array
            diff.append(y_points[i+1] - y_points[i])

    alldiff.append(diff) # gotta have somewhere to save em
    y_points = diff #now my previous array is the one I do calculations on
    diff = [] # make space for the new box to store differences in

result = 0

for k in range(max_order):
    temp_res = result # needed for iterative error?
    result += (fallfact(r, k) * alldiff[k][0])/fact(k)
    print(f"Interpolation of order {k+1}: {round(result, 7)}\n\t Error term: {round((fallfact(r, k) * alldiff[k][0])/fact(k), 7)}\n\t Accuracy wrt analytical solution: {round(result-1.606830, 7)}\n\t Iterative error: {result - temp_res}\n")