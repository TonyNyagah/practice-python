"""
Ask the user for a string and print out whether this string is a palindrome 
or not. (A palindrome is a string that reads the same forwards and backwards.)
"""
user_input = input("Give me a word or sentence: ")
input_no_space = user_input.replace(" ", "").lower()
user_input_backwards = input_no_space[::-1]

if input_no_space == user_input_backwards:
	print("%r is a palindrome." % user_input)
else:
	print("%r is a not palindrome." % user_input)