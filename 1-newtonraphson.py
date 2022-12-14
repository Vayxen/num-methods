import numpy as np

x0 = float(input("Starting value: ")) #set starting value for iterative function
eps = 1.E-1 #set precision

f = lambda x : np.cos(x) - x**3 #function
fp = lambda x : -np.sin(x) - 3*(x**2) #its derivative

y = f(x0)
yp = fp(x0) #I only need these two variables to check the conditions below

if y == 0: #good fucking job
    print("Root accidentally found.")
    exit(0)
elif yp == 0: #aren't you a lucky one
    print("Stationary point: algorithm will not work.")
    exit(0)


def nr(x): #i-th step
    t = x - f(x)/fp(x)
    return t

xi = nr(x0)
steps = 0 #just a check in a scenario where starting value causes NR to run indefinitely

file_with_steps = open("file_with_steps.txt", "w")

while abs(xi - x0) > eps:
    x0 = xi
    xi = nr(x0)
    steps += 1
    if steps > 200:
        print("Algorithm may have entered a cycle or is progressively overshooting. Interrupting.")
        exit(0)
    iteration = f"Step {steps} - current x = {xi}\n"
    file_with_steps.write(iteration)

file_with_steps.close()



print(f"Approximate root found after {steps} iterations: {xi} \n {f(xi)})")
