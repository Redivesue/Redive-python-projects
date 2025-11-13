# # Practice 73 （hard knowing the ord function)
# """Implement a Caesar cipher that shifts all of the letters in a message by an amount provided
#    by the user. Use a negative shift value to decode a message."""
#
# # Read the message and shift amount from the user.
# message = input("Enter a message: ")
# shift = int(input("Enter the shift value: "))
#
# # Process each character to construct the encrypted(or decrypted) message
# new_message = ""
# for letter in message:
#     if letter >="a" and letter <="z":
#         """Process a lowercase letter by determining its position in the alphabet(0-25),
#            computing its new position, and adding it to the new message"""
#         pos = ord(letter) - ord("a")
#         pos = (pos + shift) % 26
#         new_char = chr(pos+ord("a"))
#         new_message += new_char
#     elif letter >="A" and letter <="Z":
#         """Process a uppercase letter by determining its position in the alphabet(0,-25),
#            computing its new position, and adding it to the new message"""
#         pos = ord(letter) - ord("A")
#         pos = (pos + shift) % 26
#         new_char = chr(pos+ord("A"))
#         new_message += new_char
#     else:
#         # If the character is not a letter then copy it into the new message
#         new_message += letter
#
# # Display the shifted message
# print("The shifted message is: ", new_message)


# # Practice 74
# x = float(input('Enter a number: '))
# guess = x / 2
# # Newton's method for calculating square roots
# flag = True
# while flag:
#     i = 1
#     if abs(guess ** 2 - x) > 1*10**(-12):
#         guess = (guess + x / guess) / 2
#         print(f"The {i} th time update of guess is {guess}")
#         i += 1
#     else:
#         flag = False
#         print(f"The guess is {guess}")


# # Practice 75
# text = input('Enter a string: ').lower()
# l = len(text)
# print(l)
# new_letter = ""
#
# for i in range(l-1,-1,-1):
#     new_letter += text[i]
#
# if new_letter == text:
#     print(f"'{new_letter}' is a palindrome")
# else:
#     print(f"'{new_letter}' is not a palindrome")


# Practice 76
# import re
# sentence = input('Enter a sentence: ')
# clean_sentence = re.sub(r"[^\w]", "", sentence)
# clean_sentence = clean_sentence.lower()
# cl_sen_len = len(clean_sentence)
# new_sentence = ''
# for i in range(cl_sen_len-1,-1,-1):
#     new_sentence = new_sentence + clean_sentence[i]
# print(new_sentence)
# if new_sentence == clean_sentence:
#     print(f"Sentence '{new_sentence}' is a palindrome")
# else:
#     print(f"Sentence '{new_sentence}' is not a palindrome")

# # Practice 77 (注意利用“%4d%”来让输出的的值都是占四位的，从而能让0-100的1，2，3位都能对齐
# # for i in range(0,11):
# for i in range(0,11):
#     if i == 0 :
#         print('    ', end=" ")
#         for j in range(1, 11):
#             print("%4d"%j, end=" ")
#         print()
#     else:
#         print("%4d"%i,end=" ")
#         for j in range(1, 11):
#             print("%4d"%(i * j), end=" ")
#         print()


