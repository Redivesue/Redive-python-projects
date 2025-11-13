# # practice 45
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))
#
# if month == 1 and day == 1:
#     print(f"The date {month}. {day} corresponding to this month and day is New Year's Day, a national holiday in Canada")
# elif month == 7 and day == 1:
#     print(f"The date {month}. {day} corresponding to this month and day is Canada Day, a national holiday in Canada")
# elif month == 12 and day == 25:
#     print(f"The date {month}. {day} corresponding to this month and day is Christmas, a national holiday in Canada")
# else:
#     print("The date corresponding to this month and day does not correspond to a fixed holiday in Canada")

# # practice 46
# columns = {"a","b","c","d","e","f","g","h"}
# rows = {1,2,3,4,5,6,7,8}
# column_number = input("Enter a column number: ")
# row_number = int(input("Enter a row number: "))
# if column_number not in columns or row_number not in rows:
#     print("Invalid row and column pair")
# else:
#     if column_number in {"a","c","e","g"} and row_number in {1,3,5,7}:
#         colour = "black"
#     elif column_number in {"b","d","f","h"} and row_number in {1,3,5,7}:
#         colour = "white"
#     elif column_number in {"a","c","e","g"} and row_number in {2,4,6,8}:
#         colour = "white"
#     elif column_number in {"b","d","f","h"} and row_number in {2,4,6,8}:
#         colour = "black"
#
# print(f"The color of the square corresponding to the input row {row_number} and column numbers {column_number} is:{colour}")

# # practice 47
# from datetime import datetime
# month = input("Enter a month: ")
# day = int(input("Enter a day: "))
# def to_date(month: str, day: int) -> datetime.date:
#     # Assuming the year 1900 is used
#     return datetime.strptime(f"{month} {day} 1900", "%B %d %Y").date()
# def in_range(target, start, end):
#     """judge target whether in [start, end] ,supporting over a year"""
#     if start <= end:
#         return start <= target <= end
#     else:
#         # 跨年区间：比如 Dec 21 -> Mar 20
#         return target >= start or target <= end
# # fixed datetime
# spring_start, spring_end = to_date("March", 21), to_date("June", 20)
# summer_start, summer_end = to_date("June", 21), to_date("September", 22)
# autumn_start, autumn_end = to_date("September", 23), to_date("December", 20)
# winter_start, winter_end = to_date("December", 21), to_date("March", 20)
#
# def which_season(month: str, day: int) -> str:
#     target = to_date(month, day)
#     if in_range(target, spring_start, spring_end):
#         return "Spring"
#     elif in_range(target, summer_start, summer_end):
#         return "Summer"
#     elif in_range(target, autumn_start, autumn_end):
#         return "Autumn"
#     elif in_range(target, winter_start, winter_end):
#         return "Winter"
#     else:
#         return "Unknown"
#
# # testing
# print(which_season(month, day))

# # practice 48
# month = int(input('Enter your birthday month in number type: '))
# day = int(input('Enter your birthday day in number type: '))
# # Determine the zodiac sign corresponding to your birthday
# if month ==12 and day > 22 or month == 1 and day < 20:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Capricorn')
# elif month ==1 and day >= 20 or month == 2 and day < 19:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Aquarius')
# elif month == 2 and day >= 19 or month == 3 and day < 21:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Pisces')
# elif month == 3 and day >= 21 or month == 4 and day < 20:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Aries')
# elif month == 4 and day >= 20 or month == 5 and day < 21:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Taurus')
# elif month == 5 and day >= 21 or month == 6 and day < 21:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Gemini')
# elif month == 6 and day >= 21 or month == 7 and day < 23:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Cancer')
# elif month == 7 and day >= 23 or month == 8 and day < 23:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Leo')
# elif month == 8 and day >= 23 or month == 9 and day < 23:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Virgo')
# elif month == 9 and day >= 23 or month == 10 and day < 23:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Libra')
# elif month == 10 and day >= 23 or month == 11 and day < 22:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Scorpio')
# elif month == 11 and day >= 22 or month == 12 and day < 22:
#     print(f'The zodiac sign corresponding to your birthday {month}.{day} is:Sagittarius')

# # practice 49
# year = int(input("Enter a year: "))
# if year% 12 == 0:
#     print(f"The zodiac sign of this year {year} is: the Monkey")
# elif year % 12 == 1:
#     print(f"The zodiac sign of this year {year} is: the Rooster")
# elif year % 12 == 2:
#     print(f"The zodiac sign of this year {year} is: the Dog")
# elif year % 12 == 3:
#     print(f"The zodiac sign of this year {year} is: the Pig")
# elif year % 12 == 4:
#     print(f"The zodiac sign of this year {year} is: the Rat")
# elif year % 12 == 5:
#     print(f"The zodiac sign of this year {year} is: the Ox")
# elif year % 12 == 6:
#     print(f"The zodiac sign of this year {year} is: the Tiger")
# elif year % 12 == 7:
#     print(f"The zodiac sign of this year {year} is: the Rabbit")
# elif year % 12 == 8:
#     print(f"The zodiac sign of this year {year} is: the Dragon")
# elif year % 12 == 9:
#     print(f"The zodiac sign of this year {year} is: the Snake")
# elif year % 12 == 10:
#     print(f"The zodiac sign of this year {year} is: the Horse")
# elif year % 12 == 11:
#     print(f"The zodiac sign of this year {year} is: the Goat")





