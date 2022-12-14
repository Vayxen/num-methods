import numpy as np

f = lambda x: np.exp(x**2)

a = np.float64(0) #lower
b = np.float64(0.8) #upper
N = 64 #intervals
h = np.float64((b-a) / N) #step
print(h)


xs = np.linspace(a, b, N) #np.arange(a, b+h, h) yields the correct step unlike linspace which gets it horrifyingly wrong, however it still undershoots the final integral
# print(xs)
# print(xs[1:N-1:2]) #passi pari (dispari per l'indicizzazione)
# print(xs[2:N-1:2]) #viceversa


integral = f(a) + f(b)

#! slicing does NOT exclude endpoint

for i in xs[1:N-1:2]: #even index terms
    integral += 4*f(i)

for i in xs[2:N-1:2]:
    integral += 2*f(i)

print((h/3)*integral)

integral = f(a) + f(b)

for i in range(1, N-1):
    if i % 2 == 0:
        integral += 4 * f(xs[i])
    else:
        integral += 2 * f(xs[i])

print((h/3)*integral)


fourthderivative = 4*f(0.8) * (4*(0.8**4) + 12*(0.8**2) + 3)
error = (((-h)**4)/180)*(b-a)*fourthderivative #used for error estimation
print(error) #? WHY IS THE ERROR THE ONLY THING THAT SEEMS CORRECT

#! if done with non composite formula, error is h^5/90 * f(4)(xi)
# calcola errore iterativo con q = log(e_new/e_old)/log(h_new/h_old) dove e_new ed e_old sono gli errori finali, con "new" ed "old" indicanti il numero di intervalli fissati (quindi i new sono i calcoli fatti col doppio degli N precedenti) mentre h_new ed old sono l'ampiezza del passo h tra la versione new e quella old
