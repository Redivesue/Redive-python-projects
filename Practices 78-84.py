# # Practice 78 Kratz conjecture
# # Loop control to determine whether to continue the program
# def Continue_or_not():
#     print("Would you want to restart the program with anohter positive integer?(Y/N)")
#     willing = input('Please enter "Y" or "N" :')
#     if willing.upper() == "Y":
#         return True
#     elif willing.upper() == "N":
#         return False
#     else:
#         print("Please enter Y or N")
#         Continue_or_not()
#
# # The main algorithm of the Kratz conjecture
# def Kratz_fucntion(positive_integer):
#     kratz_list = []
#     kratz_list.append(positive_integer)
#     print("开始程序")
#     while kratz_list[-1] != 1:
#         if kratz_list[-1] % 2 == 0:
#             new_added_kratz_number = kratz_list[-1] / 2
#             kratz_list.append(new_added_kratz_number)
#             # print(new_added_kratz_number)
#         else:
#             new_added_kratz_number = kratz_list[-1] * 3 + 1
#             kratz_list.append(new_added_kratz_number)
#             # print(new_added_kratz_number)
#     return kratz_list
#
#
# def main():
#     flag = True
#     while flag:
#         try:
#             first_number = int(input('Enter a positive integer n: '))
#             print(Kratz_fucntion(first_number))
#         except:
#             print("Please enter a positive integer")
#         flag = Continue_or_not()
#     print("Exit the program!")
#     print("Thank you for using Kratz Fucntion!")
#
# main()

# # Practice 79 Greatest common divisor
# def Continue_or_not():
#     print("Would you want to restart the program with anohter positive integer?(Y/N)")
#     willing = input('Please enter "Y" or "N" :')
#     if willing.upper() == "Y":
#         return True
#     elif willing.upper() == "N":
#         return False
#     else:
#         print("Please enter Y or N")
#         Continue_or_not()
#
# def Greatest_common_divisor(n:int,m:int) -> int:
#     d = min(m,n)
#     while d > 0:
#         if n % d != 0 or m % d != 0:
#             d = d - 1
#         else:
#             print(f"{d} is the greatest common divisor of the number combination {n} and {m}")
#             break
#
# def input_M_N():
#     try:
#         m = int(input("Please enter a positive integer: "))
#         n = int(input("Please enter another positive integer: "))
#
#         if m <= 0 or n <= 0:
#             print("Both numbers must be positive!")
#             return input_M_N()  # 重新输入
#
#         if m == n:
#             print("The two numbers must be different!")
#             return input_M_N()  # 重新输入
#
#         return n, m  # ✅ 输入正确时返回结果
#
#     except ValueError:
#         print("Please enter valid integers!")
#         return input_M_N()  # 重新输入
#
#
#
# def main():
#     flag = True
#     while flag:
#         n,m = input_M_N()
#         Greatest_common_divisor(n,m)
#         flag = Continue_or_not()
# main()

# # Practice 80 prime factors
# def Continue_or_not():
#     print("Would you want to restart the program?(Y/N)")
#     willing = input('Please enter "Y" or "N" :')
#     if willing.upper() == "Y":
#         return True
#     elif willing.upper() == "N":
#         return False
#     else:
#         print("Please enter Y or N")
#         Continue_or_not()
#
# def judge_n():
#     try:
#         n = int(input("Please enter a positive integer larger than 2: "))
#         if n >= 2:
#             return n
#         else:
#             print("Please enter a positive integer larger than 2! ")
#             print()
#             return judge_n()
#     except ValueError:
#         print("Please enter a positive integer larger than 2!")
#         print()
#         return judge_n()
#
#
# flag = True
# while flag:
#     n =judge_n()
#     factor = 2
#     while factor <= n:
#         if n % factor == 0:
#             print(factor, "is a prime number.")
#             n = n / factor
#         else:
#             factor += 1
#     flag = Continue_or_not()
# print("The program is finished!")

# # Practice 81 Binary to Decimal
# def Continue_or_not():
#     print("Would you want to restart the program?(Y/N)")
#     willing = input('Please enter "Y" or "N" :')
#     if willing.upper() == "Y":
#         return True
#     elif willing.upper() == "N":
#         return False
#     else:
#         print("Please enter Y or N")
#         Continue_or_not()
#
# # Make sure the input is a numeric string.
# def is_binary() -> str:
#     converted_binary = input("Please enter a binary number :")
#     if set(converted_binary ) <= {"0", "1"}:
#         return converted_binary
#     else:
#         print("Please enter a binary number")
#         return is_binary()
#
# def Binary_to_Decimal(converted_binary:str) -> int:
#     converted_list = list(converted_binary)
#     print(converted_list)
#     decimal_value = 0
#     for i in range(0,len(converted_list)):
#         decimal_value = decimal_value + 2**i * int(converted_list[-1-i])
#     print(f"The binary number {converted_binary} converted to decimal is: {decimal_value}")
#
# def main():
#     flag = True
#     while flag:
#         t = is_binary()
#         Binary_to_Decimal(t)
#         flag = Continue_or_not()
#     print("Thank you!")
#
# main()

# # Practice 82 Decimal to Binary
# def Continue_or_not():
#     print("Would you want to restart the program?(Y/N)")
#     willing = input('Please enter "Y" or "N" :')
#     if willing.upper() == "Y":
#         return True
#     elif willing.upper() == "N":
#         return False
#     else:
#         print("Please enter Y or N")
#         Continue_or_not()
#
# # Make sure the input is a decimal string.
# def is_decimal() -> str:
#     converted_decimal= input("Please enter a positive integer:")
#     try:
#         judge = int(converted_decimal)
#         return judge
#     except ValueError:
#         print("Please enter a positive integer")
#         is_decimal()
#
# def Decimal_to_Binary(n:int) -> str:
#     result = ""
#     while n != 0:
#         r = n % 2
#         print(r)
#         result = str(r) + result
#         n = n//2
#     print(f"The decimal number {n} converted to binary is: {result}")
#
# flag = True
# while flag:
#     Decimal_to_Binary(is_decimal())
#     flag = Continue_or_not()
# print("Thank you!")

# # Practice 83 The largest integer
# import random
# experiment_time = 10
# count = experiment_time
# total_average_time = 0
# each_experiment_average_time = []
# while count !=0:
#     n = 100
#     trigger = 1
#     simulated_updated_list = []
#     sum_of_updated_times = 0
#     while trigger <= n:
#         # print(f"The {trigger} times of simulation begins")
#         a = random.randint(1, 100)
#         the_maximum_value = a
#         updated_time = 0
#         for i in range(1, 100):
#             random_number = random.randint(1, 100)
#             # print(random_number)
#             if the_maximum_value < random_number:
#                 the_maximum_value = random_number
#                 updated_time += 1
#             else:
#                 continue
#         # print(f"The maximum value found was {the_maximum_value}")
#         # print(f"The maximum value was updated {updated_time} times")
#         simulated_updated_list.append(updated_time)
#         sum_of_updated_times += updated_time
#         trigger += 1
#     # print(f"The simulated updated list is {simulated_updated_list}")
#     print(f"The average number of maximum value updates is:{sum_of_updated_times / n}")
#     each_experiment_average_time.append(sum_of_updated_times / n)
#     total_average_time += sum_of_updated_times / n
#     count -= 1
# print(each_experiment_average_time)
# print(f"The average number of maximum value updates is:{total_average_time / experiment_time}")

# # Practice 84 Coin toss simulation
# import random
# # The result of one coin toss
# def toss_coins():
#     # 'H' for Head，'T' for Tail
#     coins = random.choice(['H', 'T'])
#     return coins
#
# # Calculate the number of throws required to achieve the first identical result.
# def Calculate_times_to_same():
#     flag = True
#     result_list = []
#     result_list.append(toss_coins())
#     result_list.append(toss_coins())
#     times_counter = 3
#     while flag:
#         coins = toss_coins()
#         print(coins,end="  ")
#         result_list.append(coins)
#         if (result_list[times_counter-3] == result_list[times_counter-2] and
#             result_list[times_counter-2] == result_list[times_counter-1]):
#             flag = False
#         else:
#             pass
#         times_counter += 1
#     for i in result_list:
#         print(i,end ="  ")
#     print(f"({times_counter} flips)")
#     return times_counter
#
# # The experiment of "recording the number of times the same face result appears
# # for the first time" was simulated ten times.
#
# times_of_experiment = 10
# trigger = 10
# sum_of_times = 0
# while trigger != 0:
#     times = Calculate_times_to_same()
#     sum_of_times += times
#     trigger -= 1
# print(f"On average,{sum_of_times / times_of_experiment} flips were needed.")









