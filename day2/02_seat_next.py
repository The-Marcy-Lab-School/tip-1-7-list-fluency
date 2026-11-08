# A) Break down the line inside seat_next_c, with waitlist = ["Ana", "Bo", "Priya"].
#
#    Expression                 | Value | Type
#    waitlist[0]                |       |
#    waitlist.remove("Ana")     |       |
#    waitlist (after the line)  |       |
#
# B) seat_next_b and seat_next_c both took Ana off the list.
#    Why did only seat_next_b give her name back? Why did seat_next_a give back Priya?
#
#
# C) Type each line into the Python REPL. Predict each output first.
#    waitlist = ["Ana", "Bo", "Priya", "Bo"]
#    waitlist.count("Bo")
#    waitlist.index("Bo")
#    "Sam" in waitlist
#    waitlist.remove("Bo")
#    waitlist
#    waitlist.index("Sam")
#
# Rule:
