# Modify 1: make hot_days give back every day over 80 → [85, 90]
# Modify 2: let the caller choose the cutoff → hot_days(temps, 75) gives [85, 90, 77]
# Modify 3: give back a label for every day, "hot" or "ok" → hot_days(temps, 80) gives ['hot', 'ok', 'hot', 'ok']

temps = [85, 72, 90, 77]


def hot_days(temps):
    for temp in temps:
        hot = []
        if temp > 80:
            hot.append(temp)
    return hot


print(hot_days(temps))
