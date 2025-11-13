# # 1.print 1-10
# for i in range(1,11,1):
#     print(i)

# # 2.Print 9✖️9 multiplication table
# t=1
# for i in range(1,10):
#     if t == i:
#         for j in range(1, 10):
#             print(f"{i}×{j}={i * j}", end=",")
#     else:
#         t=i
#         print()
#         for j in range(1, 10):
#             print(f"{i}×{j}={i * j}", end=",")

# # 3.Use while to print the sum of 1-100
# sum_count = 0
# for i in range(1,101):
#     sum_count += i
# print(sum_count)

# # Guess the Number Game
# import random
# target_num = random.randint(1, 100)
# for i in range(1,target_num //2 +1):
#     print(f"第{i}次尝试")
#     guess_num = int(input('Guess a number between 1 and 100: '))
#     if guess_num > target_num:
#         print('Sorry, Your guess is high!.')
#     elif guess_num < target_num:
#         print('Sorry, Your guess is low!')
#     else:
#         print('You win!')
# print(target_num)