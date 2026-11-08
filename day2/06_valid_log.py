# Make 3: valid_log(events)
# A one-lane driveway fits cars in a single line, so the last car in must be the first out.
# Each event is "in:name" or "out:name". Give back True if every "out" was possible, False if not.
#   valid_log(["in:Ana", "in:Bo", "out:Bo", "out:Ana"]) → True
#   valid_log(["in:Ana", "in:Bo", "out:Ana"]) → False
#   valid_log(["out:Ana"]) → False
