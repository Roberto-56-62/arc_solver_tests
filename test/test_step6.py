import numpy as np
from arc_solver.solver.core import ARCSolver

solver = ARCSolver()

train_input = [
    [0,0,0,0],
    [0,1,2,0],
    [0,3,4,0],
    [0,0,0,0],
]

train_output = [
    [0,0,0,0],
    [0,3,1,0],
    [0,4,2,0],
    [0,0,0,0],
]

test_input = [
    [0,0,0,0],
    [0,5,6,0],
    [0,7,8,0],
    [0,0,0,0],
]

expected = np.array([
    [0,0,0,0],
    [0,7,5,0],
    [0,8,6,0],
    [0,0,0,0],
])

result = solver.solve(train_input, train_output, test_input)

print("OUTPUT:\n", result)
print("EXPECTED:\n", expected)
print("PASS:", np.array_equal(result, expected))

