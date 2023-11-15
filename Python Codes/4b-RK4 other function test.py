from numpy import sin as sin
import matplotlib.pyplot as plt
y_prime = lambda x, y: (x**2)/2 + sin(y)

x0, y0 = 0, 0 #looks better this way considering we deal with a function in 2 variables like f(x, y)?
yn = y0
x1 = 2
n = 16 #int(input("Intervalli: "))
h = (x1-x0)/n
xs1 = []
ys1 = []
for i in range(n):
    xs1.append(x0)
    ys1.append(yn)
    k0 = h * y_prime(x0, yn)
    k1 = h * y_prime(x0 + (h/2), yn + (k0/2))
    k2 = h * y_prime(x0 + (h/2), yn + (k1/2))
    k3 = h * y_prime(x0 + h, yn + k2)

    yn += (1/6)*(k0 + 2*k1 + 2*k2 + k3)
    x0 += h
    print(f"Valore al passo {i+1}: {round(yn, 7)}")

print(f"Valore della funzione nel punto {x1}: {yn}")
plt.plot(xs1, ys1)
plt.show()