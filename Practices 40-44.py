# # practice 40
# decibel = float(input("Enter a number: "))
# if decibel < 0:
#     print("This is not a invalid decibel")
# elif decibel <= 40 :
#     print("Decibel levels are under quiet room levels")
# elif decibel <= 70 :
#     print("Decibel levels are at between quiet room levels and alarm clock levels")
# elif decibel <= 106 :
#     print("Decibel levels are at between alarm clock levels and lawn mower levels")
# elif decibel <= 130:
#     print("Decibel levels are at between lawn mower level and jackhammer levels")
# else:
#     print("Decibel levels are beyond jackhammer levels")

# # practice 41
# a =float(input("Please enter first length of the three sides:"))
# b = float(input("Please enter second length of the three sides:"))
# c = float(input("Please enter third length of the three sides:"))
#
# if a + b > c and a + c > b and b + c > a :
#     if a == b or b==c or a==c:
#         print("This is a Isosceles Triangle")
#     elif a == b and b==c:
#         print("This is a Equilateral Triangle")
#     else:
#         print("This is a Scalene Triangle")
# else:
#     print("Three sides are invalid")

# # practice 42
# # convert the name of a note to its frequency
# C4_FEREQ =261.63
# D4_FEREQ =293.66
# E4_FEREQ =329.63
# F4_FEREQ =349.23
# G4_FEREQ =392.00
# A4_FEREQ =440.00
# B4_FEREQ =493.88
#
# # Read tbe note name from the user
# name = input("Enter the two character note name, such as C4 :")
# name = name.upper()
#
# # Save the note and its octave in separate variables
# note = name[0]
# octave = int(name[1])
#
# # Get the frequency of the note, assuming it is in the fourth octave
# if note == "C":
#     frequency = C4_FEREQ
# elif note == "D":
#     frequency = D4_FEREQ
# elif note == "E":
#     frequency = E4_FEREQ
# elif note == "F":
#     frequency = F4_FEREQ
# elif note == "G":
#     frequency = G4_FEREQ
# elif note == "A":
#     frequency = A4_FEREQ
# elif note == "B":
#     frequency = B4_FEREQ
#
# # Now adjust the frequency to bring it into the correct octave
# frequency = frequency / 2 ** (4 - octave)
#
# print(f"the frequency of {name} is {frequency:.2f}")

# # Practice 43
# frey = float(input('Enter the frequency: '))
# if frey >= 260.63 and frey <= 262.63:
#     print(f'The syllable {frey} corresponding to this frequency is:C4')
# elif frey >= 292.66 and frey <= 294.66:
#     print(f'The syllable {frey} corresponding to this frequency is:D4')
# elif frey >= 328.63 and frey <= 330.63:
#     print(f'The syllable {frey} corresponding to this frequency is:E4')
# elif frey >= 348.23 and frey <= 350.23:
#     print(f'The syllable {frey} corresponding to this frequency is:F4')
# elif frey >= 391.00 and frey <= 393.00:
#     print(f'The syllable {frey} corresponding to this frequency is:G4')
# elif frey >= 439.00 and frey <= 441.00:
#     print(f'The syllable {frey} corresponding to this frequency is:A4')
# elif frey >= 492.88 and frey <= 494.88:
#     print(f'The syllable {frey} corresponding to this frequency is:B4')
# else:
#     print(f'The frequencies {frey} do not correspond to known notes')

# # practice 44
# money_pool = {1,2,5,10,20,50,100}
# paper_amount = int(input("Enter the amount of currency: "))
# if paper_amount not in money_pool:
#     print("Sorry, you don't have that many money!")
# if paper_amount == 100:
#     print(f"The person on the banknote of {paper_amount} denomination is called Benjamin Franklin.")
# elif paper_amount == 50:
#     print(f"The person on the banknote of {paper_amount} denomination is called Ulysses Simpson Grant.")
# elif paper_amount == 20:
#     print(f"The person on the banknote of {paper_amount} denomination is called Andrew Jackson.")
# elif paper_amount == 10:
#     print(f"The person on the banknote of {paper_amount} denomination is called Alexander Hamilton.")
# elif paper_amount == 5:
#     print(f"The person on the banknote of {paper_amount} denomination is called Abraham Lincoln.")
# elif paper_amount == 2:
#     print(f"The person on the banknote of {paper_amount} denomination is called Thomas Jefferson.")
# elif paper_amount == 1:
#     print(f"The person on the banknote of {paper_amount} denomination is called George Washington.")









