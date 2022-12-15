import numpy as np

epsilon = 1.E-5 #minimum precision
sol = [0, 0, 0, 0] # "sol" is the vector of (iteratively calculated) solutions (can be any values, null vector is just one of the easy choices)
A = [[10, 5, 0, 0],
    [5, 10, -4, 0],
    [0, -4, 8, -1],
    [0, 0, -1, 5]] #coeff matrix
b = [6, 25, -11, -11] #knowns

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