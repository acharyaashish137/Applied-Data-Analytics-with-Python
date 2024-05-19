
#2.a The sum of all even numbers between 2 and 100 (inclusive).

sum = 0
for num in range(2, 101, 2):
    sum += num
print("Sum of even numbers between 2 and 100 (inclusive):", sum)

#2.b The sum of all squares between 1 and 100 (inclusive).

sum_sqr = 0
for num in range(1, 101):
    sum_sqr += num ** 2
print("Sum of squares between 1 and 100 (inclusive):", sum_sqr)


#2.c The sum of all odd numbers between a and b (inclusive).
# Assuming a and b are the lower and upper bounds of the range

a = 1
b = 100
sum_odd = 0
for num in range(a, b + 1):
    if num % 2 != 0:  # Check if the number is odd
        sum_odd += num
print("Sum of odd numbers between {} and {} (inclusive): {}".format(a, b, sum_odd))


#2.d The sum of all odd digits of n. (For example, if n is 32677, the sum would be 3 + 7 + 7 = 17.)

num= n = 587283
num_odd = 0

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        num_odd += digit
    n //= 10

print("Sum of odd digits of", num,"is",num_odd)

