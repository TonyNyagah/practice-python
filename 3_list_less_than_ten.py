"""
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
Extras:
1. Instead of printing the elements one by one, make a new list that has all the 
   elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from the 
   original list a that are smaller than that number given by the user.
"""
user_input = input("Enter a bunch of numbers separated by commas: ")
user_number = int(input("Give me a number: "))
list_input = list(user_input.split(','))
int_list = list(map(int, list_input))
new_list = []

for n in int_list:
	if n < user_number:
		new_list.append(n)

print("Your given list was %r." % int_list)
print("The numbers smaller than %d are %r." % (user_number, new_list))
