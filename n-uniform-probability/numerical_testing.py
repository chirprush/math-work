from math import factorial, comb, pi

# Pick some arbitrary large number to act as infinity
Inf = 1e10

# We'll truncate the series at 10 terms
def inverse_part(k: int):
    t = 1
    return 1 / (2 * pi) * sum((-1) ** m * (t - k) ** (2 * m + n) / (factorial(2 * m + n) * (2 * m + 1)) * Inf ** (2 * m + 1) for m in range(0, 11))

n = 4

# Quite obviously, this seems to grow larger and diverge, meaning that there's
# some mistake regarding how I used Mellin's inversion formula.
print(sum(comb(n, k) * (-1) ** k * inverse_part(k) for k in range(0, n + 1)))
