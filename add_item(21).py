# Write a function add_item(item, items_list=...) that adds items to a list and returns it.
# Call it twice:

# first call adds 1

# second call adds 2


# Expected behavior
# The two calls should produce separate lists:

# First output: [1]

# Second output: [2]

# Catch
# A naive implementation often produces:

# [1]

# [1, 2]

# Task

# First write it naively and observe the bug

# Then fix it so each call is independent unless a list is explicitly passed