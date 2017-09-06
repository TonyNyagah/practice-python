"""
Take two lists, say for example these two:
  
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only
the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this.
2. Write this in one line of Python (don’t worry if 
   you can’t figure this out at this point - we’ll get 
   to it soon)
"""
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for x in a:
	if x in b:
		c.append(x)

print(c)
"""
import random
from random import randint

list_A = random.sample(range(1,100), randint(1,10))
list_B = random.sample(range(1,100), randint(1,10))
list_C = []

for n in list_A:
	if n in list_B:
		list_C.append(n)

print("The first list contains: %r" % list_A)
print("The second list contains: %r" % list_B)
print("Numbers in both lists include: %r" % list_C)