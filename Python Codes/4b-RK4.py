dydx = lambda x, y: ((x**2)/2) + ((x*y)/2) - 1

x0, y0 = 0, 1 #looks better this way considering we deal with a function in 2 variables like f(x, y)?
current_y = y0
x1 = 2
intervals = 4 #int(input("Intervalli: "))
h = (x1-x0)/intervals

for i in range(intervals):
    k0 = h * dydx(x0, current_y)
    k1 = h * dydx(x0 + (h/2), current_y + (k0/2))
    k2 = h * dydx(x0 + (h/2), current_y + (k1/2))
    k3 = h * dydx(x0 + h, current_y + k2)

    current_y += (1/6)*(k0 + 2*k1 + 2*k2 + k3)
    x0 += h
    print(f"Valore al passo {i+1}: {round(current_y, 7)}")

print(f"Valore della funzione nel punto {x1}:", "%11.8f" % current_y)