n= 150
#1.a)	All squares less than n.

print ("All squares less than", n )
a = 0
while(a*a<n):
    print(a*a)
    a+=1
print()



#1.b)	All positive numbers that are divisible by 10 and less than n.

print ("All positive numbers that are divisible by 10 and less than", n )
num = 10  # Start with the first number that is divisible by 10
while num < n:
    print(num)
    num += 10
print()



#1.c)	All powers of two less than n.

print ("All powers of two less than", n )
power = 1  # Start with the first power of two (2^0)
while power < n:
    print(power)

    power *= 2
print()

