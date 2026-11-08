times = [42, 18, 35, 27, 50]   # commute minutes, Monday to Friday
# Data types of these values:


def fastest_a(times):
    times.sort()
    return times[:3]


def fastest_b(times):
    return sorted(times)[:3]


def fastest_c(times):
    return times.sort()[:3]


print(fastest_b(times))
# Prediction:
# Actual:
# Explanation:

print(times)
# Prediction:
# Actual:
# Explanation:

print(fastest_a(times))
# Prediction:
# Actual:
# Explanation:

print(times)
# Prediction:
# Actual:
# Explanation:

print(fastest_c(times))
# Prediction:
# Actual:
# Explanation:
