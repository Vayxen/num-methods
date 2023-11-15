# ABM1 = Adams-Bashforth-Moulton of the first order (which is the two-step Predictor-Corrector method)

import numpy as np
#controlla gli appunti
f = lambda x, y: (x**2)/2 + np.sin(y) #ODE da risolvere
h = 0.1 #step size per l'iterazione
x0, y0 = 0, 0 #coincide col dire che y(0) = 0
x1 = x0 + h
w0 = y0 #per consistenza
x_end = 2 #ultimo punto da integrare
eps = 1E-5 #precisione sul ricalcolo del corrector

def rk4(x, y, f): #uso RK4 (senza ciclo, non mi serve) per ottenere solo il primo punto
    k0 = h * f(x, y)
    k1 = h * f(x + (h/2), y + (k0/2))
    k2 = h * f(x + (h/2), y + (k1/2))
    k3 = h * f(x + h, y + k2)
    return (1/6)*(k0 + 2*k1 + 2*k2 + k3)

w1 = rk4(x0, y0, f) #calcolo il primo punto per completare la formula P-C e dare quindi inizio al while
#print(f"Punto ottenuto come valore iniziale: {w1}")

while x1 <= x_end:
    w_predictor = w1 + (h/2)*(3*f(x1, w1) - f(x0, w0)) #applico la formula predictor
    w_corrector = w1 + (h/2)*(f(x1+h, w_predictor) + f(x1, w1)) #applico la corrector
    print(f"\nPrima approssimazione di w_corrector: {w_corrector}")

    err = abs(w_corrector - w_predictor)
    while err > eps: #ricalcolo corrector 
        w_predictor = w_corrector #"w predictor" diventa la mia "iterazione precedente", lo inserisco nella formula che mi sputerà fuori "l'iterazione successiva", cioè il nuovo w corrector
        w_corrector = w1 + (h/2)*(f(x1+h, w_predictor) + f(x1, w1))
        err = abs(w_corrector - w_predictor) #ricalcolo l'errore
        print(f"Valore corrector raffinato: {w_corrector}\nErrore corrector attuale: {err}")
    print(f"Valore della curva soluzione sul punto {round(x1, 2)}: {w_corrector}")
    #si sposta tutto in avanti ora
    x0 = x1
    x1 += h
    w0 = w1
    w1 = w_corrector