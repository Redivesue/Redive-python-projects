# # practice 35
# num = int(input("Enter a integer: "))
# if num % 2 == 0:
#     print(num, "is an even number")
# else:
#     print(num, "is an odd number")

# # practice 36
# human_year = int(input('Enter a year: '))
# if human_year < 0:
#     print('You must enter a positive year.')
# else:
#     if human_year <2:
#         dog_year = human_year * 10.5
#         print("Human year",human_year,'is equals to dog year', dog_year)
#     else:
#         dog_year = (human_year-2) * 4 + 2 * 10.5
#         print("Human year",human_year,'is equals to dog year', dog_year)

# # practice 37
# import string
# lowercase_letters = string.ascii_lowercase
# letter = input('Enter a letter: ').lower()
# if letter not in lowercase_letters:
#     print('That letter is not in Alphabet')
# else :
#     if letter in "aeiou":
#         print(f"The letter entered {letter} is a vowel")
#     elif letter == "y":
#         print(f"The letter entered {letter} sometimes is a vowel or sometime is a consonant!")
#     else:
#         print(f"The letter entered {letter} is a consonant")

# # practice 38
# sides = int(input("please enter sides: "))
# if sides == 3:
#     print("This figure is Triangle")
# elif sides == 4:
#     print("This figure is Quadrilateral or Tetragon")
# elif sides == 5:
#     print("This figure is Pentagon")
# elif sides == 6:
#     print("This figure is Hexagon")
# elif sides == 7:
#     print("This figure is Heptagon or Septagon")
# elif sides == 8:
#     print("This figure is Octagon")
# elif sides == 9:
#     print("This figure is Nonagon or Enneagon")
# elif sides == 10:
#     print("This figure is Decagon")
# else:
#     print("Invalid sides")

# # practice 39
# month = input('Enter a month: ')
# months = [
#     "January", "February", "March", "April", "May", "June",
#     "July", "August", "September", "October", "November", "December"
# ]
# months_31 = ["January", "March", "May", "July", "August", "October", "December"]
# months_30 = ["April", "June", "September", "November"]
# if month in months:
#     if month in months_31:
#         print(f"This {month} has 31 days.")
#     elif month in months_30:
#         print(f"This {month} has 30 days.")
#     else:
#         print(f"This {month} has 28 days or 29 days.")
# else:
#     print(f"The {month} is not a valid month.")
