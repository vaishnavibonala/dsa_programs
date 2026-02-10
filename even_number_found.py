# Given a list of integers:
# If any even number exists → print "Even found"

# Otherwise → print "No even numbers"

# Requirements

# Use a loop

# Use break when an even number is found

# Use for-else (the else should run only if the loop completes without break)

# Example
# Input: [1, 3, 5] → Output: No even numbers
# Input: [1, 4, 5] → Output: Even found

def even_number(nums):

    for i in nums:
        if i % 2 == 0:
            print("Even Found")
            continue
    else:
        print("No even numbers")

output = even_number([1,2,3,5])

