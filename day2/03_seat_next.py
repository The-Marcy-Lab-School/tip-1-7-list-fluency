# Modify 1: seat_next([]) crashes. Make it give back None instead → seat_next([]) gives None
# Modify 2: seat a guest by name, or give back None if they aren't on the list
#           → seat(["Ana", "Bo", "Priya"], "Bo") gives 'Bo' · seat(["Ana"], "Sam") gives None
# Modify 3: give back a guest's place in line (1 = next), or 0 if they aren't on it
#           → place(["Ana", "Bo", "Priya"], "Priya") gives 3


def seat_next(waitlist):
    return waitlist.pop(0)


print(seat_next(["Ana", "Bo", "Priya"]))
print(seat_next([]))
