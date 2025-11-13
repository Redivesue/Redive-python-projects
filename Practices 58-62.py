# # practice 58
# year_input = int(input("Enter a year: "))
# if year_input % 400 == 0:
#     print(f"{year_input} is a BNB year")
# else:
#     if year_input % 4 == 0 and year_input % 100 != 0:
#         print(f"{year_input} is a BNB year")
#     else:
#         print(f"{year_input} is not a BNB year")

# # practice 59
# from datetime import date
# # three input sentences
# year1 = int(input("Enter a year: "))
# month1 = int(input("Enter a month(form 1-12): "))
# day1 = int(input("Enter a day(from 1-31): "))
# # convert to date
# def Convert_to_date(year,month,day):
#     d = date(year, month, day)
#     print(d)  # 2025-09-14
# # special date
# months_pool ={1,3,5,7,8,10}
# # add 1 to a new month
# if month1 in months_pool:
#     if day1 == 31:
#         year2 = year1
#         month2 = month1 + 1
#         day2 = 1
#         Convert_to_date(year2, month2, day2)
#     else:
#         year2 = year1
#         month2 = month1
#         day2 = day1+1
#         Convert_to_date(year2, month2, day2)
# else:
#     if month1 ==2:
#         if year1 % 400 == 0 or (year1 % 4 == 0 and year1 % 100 != 0):
#             if day1 == 29:
#                 year2 = year1
#                 month2 = month1 + 1
#                 day2 = 1
#                 Convert_to_date(year2, month2, day2)
#             else:
#                 year2 = year1
#                 month2 = month1
#                 day2 = day1+1
#                 Convert_to_date(year2, month2, day2)
#         else:
#             if day1 ==28:
#                 year2 = year1
#                 month2 = month1 + 1
#                 day2 = 1
#                 Convert_to_date(year2, month2, day2)
#             else:
#                 year2 = year1
#                 month2 = month1
#                 day2 = day1+1
#                 Convert_to_date(year2, month2, day2)
#     elif month1  == 12:
#         if day1 == 31:
#             year2 = year1+1
#             month2 = 1
#             day2 = 1
#             Convert_to_date(year2, month2, day2)
#         else:
#             year2 = year1
#             month2 = month1
#             day2 = day1+1
#             Convert_to_date(year2, month2, day2)
#     else:
#         if day1 ==30:
#             year2 = year1
#             month2 = month1 + 1
#             day2 = 1
#             Convert_to_date(year2, month2, day2)
#         else:
#             year2 = year1
#             month2 = month1
#             day2 = day1+1
#             Convert_to_date(year2, month2, day2)

# # practice 60
# import math
# from math import floor
# year_into_function = int(input("Enter a year: "))
# day_of_the_week = (year_into_function + floor((year_into_function-1)/4) - floor((year_into_function-1)/100)+
#                    floor((year_into_function-1)/400)) % 7
# if day_of_the_week == 0:
#     print(f"Jan 1st of This year{year_into_function} is Sunday!")
# elif day_of_the_week == 1:
#     print(f"Jan 1st of This year{year_into_function} is Monday!")
# elif day_of_the_week == 2:
#     print(f"Jan 1st of This year{year_into_function} is Tuesday!")
# elif day_of_the_week == 3:
#     print(f"Jan 1st of This year{year_into_function} is Wednesday!")
# elif day_of_the_week == 4:
#     print(f"Jan 1st of This year{year_into_function} is Thursday!")
# elif day_of_the_week == 5:
#     print(f"Jan 1st of This year{year_into_function} is Friday!")
# else:
#     print(f"Jan 1st of This year{year_into_function} is Saturday!")

# # practice 61
# car_card_input = input("Enter a car card: ")
# if len(car_card_input)  == 6 and \
#     car_card_input[0]>="A" and car_card_input[0]<="Z" and\
#     car_card_input[1]>="A" and car_card_input[1]<="Z" and \
#     car_card_input[2]>="A" and car_card_input[2]<="Z" and \
#     car_card_input[3]>="0" and car_card_input[3]<="9" and \
#     car_card_input[4]>="0" and car_card_input[4]<="9" and \
#     car_card_input[5]>="0" and car_card_input[5]<="9":
#     print(f"The car card {car_card_input} is a valid older style pattern")
# elif len(car_card_input) == 7 and \
#     car_card_input[0]>="0" and car_card_input[0]<="9" and \
#     car_card_input[1]>="0" and car_card_input[1]<="9" and \
#     car_card_input[2]>='0' and car_card_input[2]<="9" and \
#     car_card_input[3]>="0" and car_card_input[3]<="9" and \
#     car_card_input[4]>="A" and car_card_input[4]<="Z" and \
#     car_card_input[5]>="A" and car_card_input[5]<="Z" and \
#     car_card_input[6]>="A" and car_card_input[6]<="Z":
#     print(f"The car card {car_card_input} is a valid newer style pattern")
# else:
#     print(f"The car card {car_card_input} is not a valid car card")

# # practice 62
# red_pool={1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
# from random import randrange
# value = randrange(0,38)
# if value == 37:
#     print('The spin resulted in 00 ...')
# else:
#     print('The spin resulted in %d' % value)
# # The First Pay
# if value == 38:
#     print("Pay 00")
# else:
#     print("Pay ",value)
# # The Second Pay
# if value in red_pool:
#     print("Pay Red")
# elif value ==0 or value ==37:
#     pass
# else:
#     print("Pay Black")
# # The Third Pay
# if value >=1 and value <=36:
#     if value%2==1:
#         print("Pay Odd")
#     else:
#         print("Pay Even")
# # The fourth Pay
# if value >= 1 and value <= 18:
#     print('Pay 1 to 18')
# elif value >= 19 and value <= 36:
#     print('Pay 19 to 36')











