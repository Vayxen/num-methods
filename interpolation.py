from typing import List
import numpy as np
# from math import prod

x_points = np.linspace(0.5, 1.85, 10, endpoint = True)
y_points = np.array([1.51295, 1.79024, 2.04887, 2.27976, 2.47567, 2.63142, 2.74432, 2.81448, 2.84532, 2.84409])

X = 0.55
r = (X - 0.5) / 0.15
order = 8

def ffd(xset: List[float], iteration = 0) -> List[List[float]]: 
    if iteration >= order:
        return []

    current_iteration_diff = []

    for i in range(len(xset) - 1):

        delta = round(xset[i+1] - xset[i], 4)
        current_iteration_diff.append(delta)
        
    return [current_iteration_diff] + ffd(current_iteration_diff, iteration + 1)

res = [y_points] + ffd(y_points)

print(f"\n===================\nObtained differences, from order 0 to 8:\n{res}\n")

file = open("fwddifferences.txt", "w")
file.write(str(res))
file.close

#evaluating finite differences from order 1 to 8

# imagine this is latex... sum_0^8 r(r-1)...(r-n+1) * res[i][0]/n!

#interpolate and evaluate x = 0.55 on the interpolated polynomial
