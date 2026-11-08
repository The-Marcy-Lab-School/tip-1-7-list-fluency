# Seat the next guest from a restaurant waitlist. Ana signed up first.


def seat_next_a(waitlist):
    return waitlist.pop()


def seat_next_b(waitlist):
    return waitlist.pop(0)


def seat_next_c(waitlist):
    return waitlist.remove(waitlist[0])


print(seat_next_a(["Ana", "Bo", "Priya"]))
# Prediction:
# Actual:
# Explanation:

print(seat_next_b(["Ana", "Bo", "Priya"]))
# Prediction:
# Actual:
# Explanation:

print(seat_next_c(["Ana", "Bo", "Priya"]))
# Prediction:
# Actual:
# Explanation:
