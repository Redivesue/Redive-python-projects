# # Practice 63 average
# flag = True;t=0;count = 0
# while flag:
#     a = int(input("Enter a number: "))
#     if a != 0 :
#         t = t + a
#         count = count + 1
#         continue
#     else:
#         flag = False
# if t ==0:
#     print("Error Input!You should not enter 0 at the first time!")
# else:
#     print(f"Total amount of those number is {t}.\n The amount of number in the group is {count}.\n"
#       f"And the average of this group of numbers is {t/count}")
#

# # Practice 64 Discount Table(No y to break the
# flag = True
# while flag:
#     original_price = round(float(input('Enter the original price of the product: ')),2)
#     discounted_price = round(original_price*0.6,2)
#     discount_amount = original_price - discounted_price
#     print(f"Original price: {original_price},\n"
#           f"Discount amount: {discount_amount},\n"
#           f"Discounted price: {discounted_price}"
#           )
#     judegement_val=input("Would you want to continue inputting the information of a new product? (y/n):  ").lower()
#     if judegement_val != 'y':
#         flag = False
#     else:
#         continue

# # Practice 65
# for i in range(0,11):
#     print(f"{i*10} degrees Celsius equals {(i*10*9)/5 +32} degrees Fahrenheit",end="\n")

# # Practice 66
# ##
# # Compute the total due when several items are purchased.The amount payable for cash
# # transactions is rounded to the closest nickel because pennies have been phased out in Canada.
# #
# pennies_per_nickel = 5
# nickel = 0.05
# # Track the total cost for all of the items
# total = 0.00
# # Read the price of the first item as a string
# line = input("Enter the price of the item(blank to quit):")
# # Continue reading items until a blank line is entered
# while line != '':
#     total = total + float(line)
#     line = input("Enter the price of the item(blank to quit):")
#     print('The exact amount payable is %.02f'%total)
#     rounding_indicator = total * 100 % pennies_per_nickel
#     if rounding_indicator < pennies_per_nickel / 2:
#         cash_total = total - rounding_indicator/100
#     else:
#         cash_total = total + nickel - rounding_indicator/100
#     print("The cash total is %.02f"%cash_total)

# # Practice 67
# import math
# # 初始化周长
# perimeter_of_polygon = 0.00
# # 输入第一个坐标
# first_x_co = input("Enter the first x co-ordinates: ")
# first_y_co = input("Enter the first y co-ordinates: ")
# # 第一个坐标信息的记录（不改变）
# first_x = first_x_co
# first_y = first_y_co
# # 如果第一个信息没有内容则直接退出程序
# if first_x_co == "" or first_y_co == "":
#     flag = False
#     print("没有初始点坐标错误！")
# else:
#     # 有内容，进入第二个输出
#     sec_x_co = input("Enter the next x co-ordinates: ")
#     sec_y_co = input("Enter the next y co-ordinates: ")
#     if sec_x_co == "" or sec_y_co == "":
#         flag = False
#         print("只有一个点坐标，不能形成边或多边形！")
#     else:
#         flag = True
#
# # 主题循环
# while flag:
#     pre_x_co = first_x_co
#     pre_y_co = first_y_co
#     next_x_co = sec_x_co
#     next_y_co = sec_y_co
#     perimeter_of_polygon = perimeter_of_polygon + math.sqrt(
#         (float(pre_x_co) - float(next_x_co)) ** 2 + (float(pre_y_co) - float(next_y_co)) ** 2)
#     # 向前迭代坐标信息
#     pre_x_co = next_x_co
#     pre_y_co = next_y_co
#     sec_x_co = input("Enter the next x co-ordinates: ")
#     sec_y_co = input("Enter the next y co-ordinates: ")
#     if sec_x_co == "" or sec_y_co == "":
#         flag = False
#         perimeter_of_polygon = perimeter_of_polygon + math.sqrt(
#             (float(pre_x_co) - float(first_x_co)) ** 2 + (float(pre_y_co) - float(first_y_co)) ** 2)
#     else:
#         perimeter_of_polygon = perimeter_of_polygon + math.sqrt(
#             (float(pre_x_co) - float(next_x_co)) ** 2 + (float(pre_y_co) - float(next_y_co)) ** 2)
# print(f"The perimeter of that polygon is{perimeter_of_polygon}")
# print("\nProgram Complete!")




