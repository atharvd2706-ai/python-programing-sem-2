import math

P = 100000
annual_rate = 10
r = annual_rate / (12 * 100)
n = 24

EMI = (P * r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)

print("EMI =", round(EMI, 2))