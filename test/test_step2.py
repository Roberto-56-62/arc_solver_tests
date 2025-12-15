from arc_solver.solver.core import ARCSolver

solver = ARCSolver()

# =========================
# TEST 1 — ROTAZIONE 90
# =========================
train_input = [
    [1, 2],
    [3, 4]
]

train_output = [
    [3, 1],
    [4, 2]
]

test_input = [
    [5, 6],
    [7, 8]
]

expected = [
    [7, 5],
    [8, 6]
]

result = solver.solve(train_input, train_output, test_input)

print("TEST ROT90")
print("OUTPUT:", result)
print("EXPECTED:", expected)
print("PASS:", result == expected)
print("-" * 40)


# =========================
# TEST 2 — FLIP ORIZZONTALE
# =========================
train_input = [
    [1, 2],
    [3, 4]
]

train_output = [
    [2, 1],
    [4, 3]
]

test_input = [
    [5, 6],
    [7, 8]
]

expected = [
    [6, 5],
    [8, 7]
]

result = solver.solve(train_input, train_output, test_input)

print("TEST FLIP H")
print("OUTPUT:", result)
print("EXPECTED:", expected)
print("PASS:", result == expected)
print("-" * 40)

