# # practice 50
# magnitude = float(input("Enter a Magnitude: "))
# if magnitude < 2.0:
#     print(f"Earthquakes of magnitude {magnitude:.1f} are regarded as Super micro intyensit earthquakes")
# elif magnitude >= 2.0 and magnitude < 3.0:
#     print(f"Earthquakes of magnitude {magnitude:.1f} are regarded as Very little intyensit earthquakes")
# elif magnitude >= 3.0 and magnitude < 4.0:
#     print(f"Earthquakes of magnitude {magnitude:.1f} are regarded as Tiny intyensit earthquakes")
# elif magnitude >= 4.0 and magnitude < 5.0:
#     print(f"Earthquakes of magnitude {magnitude:.1f} are regarded as Weak intyensit earthquakes")
# elif magnitude >= 5.0 and magnitude < 6.0:
#     print(f"Earthquakes of magnitude {magnitude:.1f} are regarded as Medium intyensit earthquakes")
# elif magnitude >= 6.0 and magnitude < 7.0:
#     print(f"Earthquakes of magnitude {magnitude:.1f} are regarded as Strong intyensit earthquakes")
# elif magnitude >= 7.0 and magnitude < 8.0:
#     print(f"Earthquakes of magnitude {magnitude:.1f} are regarded as Very strong intyensit earthquakes")
# elif magnitude >= 9.0 and magnitude < 10.0:
#     print(f"Earthquakes of magnitude {magnitude:.1f} are regarded as Extremely strong intyensit earthquakes")
# elif magnitude >= 10.0:
#     print(f"Earthquakes of magnitude {magnitude:.1f} are regarded as Super strong intyensit earthquakes")


# # practice 51
# import math
# """Given that the form of a quadratic function with one variable is:f(x) = ax^2 + bx + c"""
# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))
# c = int(input("Enter the value of c: "))
# if a == 0 and b != 0:
#     print(f"The root of the equation corresponding to this function is:{-c/b}")
# if a==0 and b==0:
#     print(f"The root of the equation corresponding to this function is: None")
# if a!=0:
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         print("The equation corresponding to this function has no real roots")
#     elif delta == 0:
#         print(f"The equation corresponding to this function has one real roots {-b/(2*a)}")
#     else:
#         print(f"The equation corresponding to this function has two real roots! One is {(-b-math.sqrt(delta))/(2*a)},  "
#               f"the ohter one is {(-b+math.sqrt(delta))/(2*a)}")


# # practice 52
# grade_levels = {"A+","A","A-","B+","B","B-","C+","C","C-","D+","D","F"}
# grade_lev = input("Enter a grade level: ")
# if grade_lev not in grade_levels:
#     print("Invalid Grade Level")
# if grade_lev == "A+":
#     print(f"The grade level {grade_lev} average corresponding to this score is:4.0")
# elif grade_lev == "A":
#     print(f"The grade level {grade_lev} average corresponding to this score is:4.0")
# elif grade_lev == "A-":
#     print(f"The grade level {grade_lev} average corresponding to this score is:3.7")
# elif grade_lev == "B+":
#     print(f"The grade level {grade_lev} average corresponding to this score is:3.3")
# elif grade_lev == "B":
#     print(f"The grade level {grade_lev} average corresponding to this score is:3.0")
# elif grade_lev == "B-":
#     print(f"The grade level {grade_lev} average corresponding to this score is:2.7")
# elif grade_lev == "C+":
#     print(f"The grade level {grade_lev} average corresponding to this score is:2.3")
# elif grade_lev == "C":
#     print(f"The grade level {grade_lev} average corresponding to this score is:2.0")
# elif grade_lev == "C-":
#     print(f"The grade level {grade_lev} average corresponding to this score is:1.7")
# elif grade_lev == "D+":
#     print(f"The grade level {grade_lev} average corresponding to this score is:1.3")
# elif grade_lev == "D":
#     print(f"The grade level {grade_lev} average corresponding to this score is:1.0")
# elif grade_lev == "F":
#     print(f"The grade level {grade_lev} average corresponding to this score is:0")

# # practice 53
# gp_unrouded = float(input('Enter a grade point: '))
# gp = round(gp_unrouded,1)
# if gp >= 4.0:
#     print('Grade point level is A+')
# elif gp >=3.7 and gp < 4.0:
#     print('Grade point level is A-')
# elif gp >= 3.3 and gp < 3.7:
#     print('Grade point level is B+')
# elif gp >= 3.0 and gp < 3.3:
#     print('Grade point level is B')
# elif gp >= 2.7 and gp<3.0:
#     print('Grade point level is B-')
# elif gp >= 2.3 and gp<2.7:
#     print('Grade point level is C+')
# elif gp >= 2.0 and gp<2.3:
#     print('Grade point level is C')
# elif gp >= 1.7 and gp<2.0:
#     print('Grade point level is C-')
# elif gp >= 1.3 and gp<1.7:
#     print('Grade point level is D+')
# elif gp >= 1.0 and gp<1.3:
#     print('Grade point level is D')
# else :
#     print('Grade point level is F')

# # practice 54
# grading_pool = {0.0,0.4}
# grading = float(input("Enter your grading: "))
# grading_level = round(grading,1)
# if grading_level < 0.6 and grading_level not in grading_pool:
#     print("Invalid Grading")
# else:
#     if grading_level == 0.0:
#         print(f"This grading level {grading_level} means that this employee's performance is unacceptable")
#     elif grading_level == 0.4:
#         print(f"This grading level {grading_level} is acceptable")
#     else:
#         print(f"This grading level {grading_level} means that it's very good performance")

# # practice 55
# light_wavelength = float(input("Please enter the wavelength of your light："))
# l_wavelength = round(light_wavelength, 1)
# if l_wavelength < 380 or l_wavelength > 750:
#     print("The wavelength of your light has exceeded the spectrum")
# elif l_wavelength >=380 and l_wavelength < 450:
#     print("Your light is purple")
# elif l_wavelength >=450 and l_wavelength < 495:
#     print("Your light is blue")
# elif l_wavelength >=495 and l_wavelength < 570:
#     print("Your light is green")
# elif l_wavelength >=570 and l_wavelength < 590:
#     print("Your light is yellow")
# elif l_wavelength >=590 and l_wavelength < 620:
#     print("Your light is orange")
# else:
#     print("Your light is red")

# practice 56
# from decimal import Decimal
# user_input = input("Please enter a value (scientific notation is acceptable): ")
# value = Decimal(user_input)
# if value < 3.0E+9 :
#     print("This electromagnetic radiation should be called radio waves!")
# elif value >= 3.0E+9 and value < 3.0E+12 :
#     print("This electromagnetic radiation should be called microwave!")
# elif value >= 3.0E+12 and value < 4.3E+14 :
#     print("This electromagnetic radiation should be called infrared light!")
# elif value >= 4.3E+14 and value < 7.5E+14 :
#     print("This electromagnetic radiation should be called Visible light!")
# elif value >= 7.5E+14 and value < 3.0E+17 :
#     print("This electromagnetic radiation should be called UV rays!")
# elif value >= 3.0E+17 and value < 3.0E+19 :
#     print("This electromagnetic radiation should be called X-ray!")
# else:
#     print("This electromagnetic radiation should be called Gamma-rays!")

# # practice 57
# def Fee_printing(extra_call_fee, extra_mails_fee, support_911_fee):
#     print(f"Basic fee: 15.00\n"
#           f"Extra_call_fee:{extra_call_fee}\n"
#           f"Extra_mails_fee{extra_mails_fee}\n"
#           f"911 supporting fee:{support_911_fee}\n"
#           f"Tax amount:{tax_fee}\n"
#           f"Total amount：{15 + extra_call_fee + support_911_fee + extra_mails_fee + tax_fee}")
#
# # fee calculation
# def Bill_list(total_call_time, total_mails_counts, extra_call_fee, extra_mails_fee, support_911_fee, sale_rate):
#     if total_call_time <= 50 and total_mails_counts <= 50:
#         Fee_printing(extra_call_fee, extra_mails_fee, support_911_fee)
#     elif total_call_time > 50 and total_mails_counts <= 50:
#         extra_call_fee = (total_call_time - 50) * 0.25
#         Fee_printing(extra_call_fee, extra_mails_fee, support_911_fee)
#     elif total_call_time <= 50 and total_mails_counts > 50:
#         extra_mails_fee = (total_mails_counts - 50) * 0.15
#         Fee_printing(extra_call_fee, extra_mails_fee, support_911_fee)
#     else:
#         extra_call_fee = (total_call_time - 50) * 0.25
#         extra_mails_fee = (total_mails_counts - 50) * 0.15
#         Fee_printing(extra_call_fee, extra_mails_fee, support_911_fee)
#
#
# # Total call time in a month
# total_call_time = round(float(input("Enter total call time: ")),2)
# total_mails_counts = round(float(input("Enter total mail counts: ")),2)
# extra_call_fee = 0
# extra_mails_fee = 0
# support_911_fee = 0.44
# sale_rate = 0.05
# tax_fee = (15+extra_mails_fee+extra_call_fee+support_911_fee)*sale_rate
# Bill_list(total_call_time, total_mails_counts, extra_call_fee, extra_mails_fee, support_911_fee, sale_rate)
















