# Modify 1: give back the two slowest commutes → [50, 42]
# Modify 2: let the caller choose how many → slowest(times, 3) gives [50, 42, 35]
# Modify 3: give back the total minutes of those commutes → slowest_total(times, 2) gives 92

times = [42, 18, 35, 27, 50]   # commute minutes, Monday to Friday


def fastest(times):
    return sorted(times)[:3]


print(fastest(times))
