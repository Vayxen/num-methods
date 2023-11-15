import numpy as np

f = lambda x: (np.e)**(x**2)
fp = lambda x: 2* f(x) * (1 + 2*(x**2))

h = 0.2 #step
result = f(0) + f(0.8) #implied: a = 0, b= 0.8
error = ((h**2)/12) * 0.8 * fp(0.8)
arg = np.linspace(h, 0.8 - h, int(0.8/h)) #this could use more numbers but works in a general case as b-a/h is the num of intervals, whereas the sum needs to stop at the n-th term, which is the second to last step (ergo b - h)

for i in arg:
    result += f(i)

result = (h/2)*result

print(result, "+-", error)