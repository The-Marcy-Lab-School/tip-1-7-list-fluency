temps = [85, 72, 90, 77]   # this week's highs in Queens
# Data types of these values:


def hot_days_a(temps):
    hot = []
    for temp in temps:
        if temp > 80:
            hot.append(temp)
    return hot


def hot_days_b(temps):
    for temp in temps:
        hot = []
        if temp > 80:
            hot.append(temp)
    return hot


def hot_days_c(temps):
    hot = []
    for temp in temps:
        if temp > 80:
            hot.append(temp)
        return hot


print(hot_days_a(temps))
# Prediction:
# Actual:
# Explanation:

print(hot_days_b(temps))
# Prediction:
# Actual:
# Explanation:

print(hot_days_c(temps))
# Prediction:
# Actual:
# Explanation:
