import random

# Function validate if the first argument is less than the second one.
def get_random(start, end):
    if start >= end:
        raise ValueError("The start value must be less than the end value.")
    return random.randint(start, end)

#function should accept an integer as an argument and returns True if it is even, false if odd.
def is_even(num):
    return num % 2 == 0

# Initialize counts for even and odd numbers
even_count = 0
odd_count = 0

# List to store the generated random numbers
random_numbers = []

# Generate 100 random numbers and count even and odd numbers
for _ in range(100):
    random_num = get_random(1, 1000)
    random_numbers.append(random_num)
    if is_even(random_num):
        even_count += 1
    else:
        odd_count += 1

# Print all random generated numbers
print("Generated random numbers:", random_numbers)
print()

# Print the results
print("Total even numbers:", even_count)
print()

print("Total odd numbers:", odd_count)
