import numpy as np

epsilon = 1.E-5 #minimum precision
sol = [0, 0, 0, 0] # "sol" is the vector of (iteratively calculated) solutions (can be any values, null vector is just one of the easy choices)
A = [[10, 5, 0, 0],
    [5, 10, -4, 0],
    [0, -4, 8, -1],
    [0, 0, -1, 5]] #coeff matrix
b = [6, 25, -11, -11] #knowns

""" May need to slap this on the jupyter notebook
From this point on we are applying (piece by piece) Jacobi's formula:
x_i(next) = 1/aii * [b_i - sum(coefficient * x_i(prev))]
So every calculation of the i-th x value is being calculated solely on the previous list of values. For instance, our first guess
entirely relies on the [0, 0, 0, 0] array, whereas with Seidel, once we obtain a guess for the first entry of the new solution vector, we use that on the subsequent entry.

Walking through what happens in Jacobi's formula:
Take an array of INITIAL x1, x2, x3, x4 values (our row of zeroes in this case)
x1's first iteration will use the INITIAL x2..4 values.
x2's first iteration will use the INITIAL x1,3,4 values.
And so on.
x1's second iteration will use the x2..4 values we obtained from the FIRST iteration.
x2's second iteration will do the same thing again, and again with the results from the FIRST iteration.

However Gauss-Seidel is as follows:
Take that same initial array.
x1's first iteration will use the INITIAL x2..4 values. And here's the difference.
x2's first iteration will use the CURRENT x1 value and the PREVIOUS (initial) values for any of the higher-indexed variables (3 and 4)
x3's first iteration will use the CURRENT x1 and x2 values and the PREVIOUS x4 value.
x4 will then use all of the CURRENT iteration values from the other variables.
In general, when solving through the GS method, during each calculation we are "centering ourselves" on one variable:
all the variables with lower index will have been already calculated (save of course for the very first), whereas of course any successive variable is yet to be calculated, so we just use the previous iteration's values.
"""

total_iterations = 0
while max(map(abs, np.dot(A, sol) - b)) > epsilon:

    print(f"Iteration {total_iterations}:\n\t{sol}\n")
    total_iterations += 1

    for i in range(4): #working with row i = this iterates over the four unknowns
        sigma = 0 #sum-storing variable, sigma cause of the big sigma notation
        result = b[i]
        for k in range(4): #iterating over column k = iterates over coefficients of row i
            if i != k:
                sigma += A[i][k] * sol[k] #coefficient * solution vector's k-th entry
            else:
                continue #skips diagonal values

        result -= sigma #as per the formula, we're taking that lonely term and subtracting that sum to its right
        result = (1/A[i][i]) * result #final touch up by dividing 1/a_ii

        sol[i] = round(result, 7)
        
print(f"Found solution vector: {sol}")
print(f"Knowns were: {b}")
print(f"Checking that the matrix product A x s returns b: {[round(x) for x in np.dot(A, sol)]} (will match the above vector if result is correct)")