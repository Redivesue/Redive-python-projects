# # practice 68
# grade_levels = {"A+","A","A-","B+","B","B-","C+","C","C-","D+","D","F"}
# total_grades = 0.00
# count = 0
# flag = True
# grade_lev = input("Please enter the letter grade for your results：")
# if grade_lev== '':
#     flag = False
# while flag == True:
#     count = count+ 1
#     if grade_lev == "A+" or grade_lev == "A":
#         total_grades += 4.0
#     elif grade_lev == "A-":
#         total_grades += 3.7
#     elif grade_lev == "B+":
#         total_grades += 3.3
#     elif grade_lev == "B":
#         total_grades += 3.0
#     elif grade_lev == "B-":
#         total_grades += 2.7
#     elif grade_lev == "C+":
#         total_grades += 2.3
#     elif grade_lev == "C":
#         total_grades += 2.0
#     elif grade_lev == "C-":
#         total_grades += 1.7
#     elif grade_lev == "D+":
#         total_grades += .3
#     elif grade_lev == "D":
#         total_grades += 1.0
#     elif grade_lev == "F":
#         total_grades += 0
#     # print(count, total_grades, end='\n')
#     # print(f"The grade point average is {total_grades / count}")
#     grade_lev = input("Please enter the letter grade for your results：")
#     if grade_lev =='':
#         flag = False
#     else:
#         continue
# print(count,total_grades,end='\n')
# print(f"The grade point average is {total_grades/count}")

# # Practice 69
# flag = True
# totol_admission_fee = 0.00
# while flag:
#     guest_old_years = input("Please enter the customer's age：")
#     if guest_old_years == '':
#         flag = False
#     else:
#         gu_old_y = int(guest_old_years)
#         if gu_old_y <=2:
#             admission_fee = 0
#             totol_admission_fee = totol_admission_fee + admission_fee
#         elif gu_old_y >=3 and gu_old_y <=12:
#             admission_fee = 14
#             totol_admission_fee += admission_fee
#         elif gu_old_y >=65:
#             admission_fee = 18
#             totol_admission_fee += admission_fee
#         else:
#             admission_fee = 23
#             totol_admission_fee += admission_fee
#         print(f"The ticket price corresponding to the customer's age is: {admission_fee}")
# print(f"The total admission fee is: {totol_admission_fee}")

# # Practice 70
# line = input("Enter 8 bits: ")
# while line != '':
#     if line.count('0') + line.count('1') != 8 or len(line) != 8:
#         print("That wasn't 8 bits... Try again.")
#     else:
#         ones = line.count('1')
#         if ones % 2 ==0:
#             print("The parity bit should be 0.")
#         else:
#             print("The parity bit should be 1.")
#     line = input("Enter 8 bits: ")

# # Practice 71
# pie_value = 0.0
# def Count_Function(i):
#     value = (-1)**i *(4/(i*(i+1)*(i+2)))
#     return value
# for i in range(1,16):
#     if i == 1:
#         pie_value += 3
#         print(f"π \u2248 {pie_value}")
#     else:
#         pie_value += Count_Function(i)
#         print(f"π \u2248 {pie_value}")


# # Practice 72
# for i in range(1,101):
#     if i%3==0 and i%5!=0:
#         print("fizz!")
#     elif i%3!=0 and i%5==0:
#         print("buzz!")
#     elif i%3==0 and i%5!=0:
#         print("fizz! buzz!")
#     else:
#         print(i)








