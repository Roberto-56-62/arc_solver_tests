import numpy as np
from arc_solver.solver.core import ARCSolver

solver = ARCSolver()

# ======================================================
# TEST STEP 5 – GEOMETRIA + COLOR MAPPING
# ======================================================

# Train input (2x2)
train_input = [
    [1, 2],
    [3, 4],
]

# Train output:
# - rotate90
# - color mapping: 1→9, 2→8, 3→7, 4→6
#
# rotate90(train_input) =
# [
#   [2, 4],
#   [1, 3]
# ]
#
# after color mapping =
train_output = [
    [8, 6],
    [9, 7],
]

# Test input
test_input = [
    [4, 3],
    [2, 1],
]

# Expected:
# rotate90(test_input) =
# [
#   [3, 1],
#   [4, 2]
# ]
#
# color mapping →
expected_output = np.array([
    [7, 9],
    [6, 8],
])

# ======================================================
# RUN
# ======================================================

result = solver.solve(train_input, train_output, test_input)

print("TEST STEP 5 – GEOMETRIA + COLOR MAPPING")
print("OUTPUT:")
print(result)
print("EXPECTED:")
print(expected_output)
print("PASS:", np.array_equal(result, expected_output))

