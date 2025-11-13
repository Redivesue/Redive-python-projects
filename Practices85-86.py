# # Practice 85
# import math
# def main(side1,side2):
#     hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
#     print(f"The length of the hypotenuse of a right triangle with legs {side1} and {side2} is: {hypotenuse}")
#
#
# if __name__ == "__main__":
#     side1 = float(input("Enter the length of one leg of a right triangle:"))
#     side2 = float(input("Enter the length of another leg of a right triangle:"))
#     main(side1,side2)
#
#
# # Practice 86
#
# def taxFeecounting(distance):
#     basic_fee = 4
#     extra_fee_rate = 0.25
#     if distance <= 140:
#         total_fee = basic_fee
#         return total_fee
#
#     # print(distance // 140)
#     extra_fee = extra_fee_rate * (distance//140)
#     total_fee = basic_fee + extra_fee
#     return total_fee
#
# if __name__ == '__main__':
#     distance = float(input('Enter the distance in kilometers: '))
#     print(f"The total tax fee of {distance} km is : {taxFeecounting(distance)}")
#
#
#