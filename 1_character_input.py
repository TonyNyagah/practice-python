"""
Create a program that asks the user to enter their name and 
their age. Print out a message addressed to them that tells 
them the year that they will turn 100 years old.
"""
import datetime

name = input("Give me your name: ")
age = int(input("How old are you?: "))

current_date = datetime.datetime.now()
current_year = current_date.year
years_to_hundred = (100 - age) 

print("=====================================================")
print("Your name is " + name + ".")
print("You are " + str(age) + " years old.")
print("You will be 100 years old in " + str(current_year + years_to_hundred) + ".")