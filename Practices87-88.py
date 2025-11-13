# # Practice 87
# def deliverFeeCounter(n):
#     if n ==1:
#         total_fee = 10.95
#         return total_fee
#     total_fee = 10.95 + 2.95 * (n-1)
#     return total_fee
#
# def main():
#     n = int(float(input("Enter a number: ")))
#     while n<=0:
#         print("Please enter a number larger than 0")
#         n = int(float(input("Enter a number: ")))
#     return n
#
# if __name__ == '__main__':
#     print(f"The total deliver fee is : {deliverFeeCounter(main())}")
#
# # Practice 88
# def mediabThreeValues(value1,value2,value3):
#     max_value = max(value1,value2,value3)
#     min_value = min(value1,value2,value3)
#     median_value = (value1+value2+value3) - max_value - min_value
#     return median_value
#
# def main():
#     value1 = float(input("Enter the first value: "))
#     value2 = float(input("Enter the second value: "))
#     value3 = float(input("Enter the third value: "))
#     return value1,value2,value3
#
# if __name__ == '__main__':
#     print(f"The median value of these three values is {mediabThreeValues(*main())}")
