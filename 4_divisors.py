"""
Create a program that asks the user for a number and then prints
out a list of all the divisors of that number. (If you don’t know
what a divisor is, it is a number that divides evenly into another 
number. For example, 13 is a divisor of 26 because 26 / 13 has no 
remainder.)
"""
num = int(input("Give me a number: "))
divisible = []
for x in range(1, num):
	#print(x)
	if num % x == 0:
		divisible.append(x)

print("%r is divisible by the following numbers: %r. " % (num, divisible))