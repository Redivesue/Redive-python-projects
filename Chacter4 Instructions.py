# # practice 1 drawbox
# def DrawBox(width,height):
#     if width < 2 and height < 2:
#         print("Error:The width or height is too small!")
#         quit()
#
#     # Draw the top of the box
#     print("*" * width)
#     # Draw two legs of the box
#     for i in range(height - 2):
#         print("*"+" "*(width - 2)+ "*")
#     # Draw the bottom of the box
#     print("*" * width)
#
#
# if __name__ == "__main__":
#     DrawBox(10,10)

# # practice 2 Can choose between square border symbols and internal fill symbols.
# def DrawBox(width,height,outline,fill):
#     if width < 2 and height < 2:
#         print("Error:The width or height is too small!")
#         quit()
#
#     # Draw the top of the box
#     print(outline * width)
#     # Draw two legs of the box
#     for i in range(height - 2):
#         print(outline+fill*(width - 2)+ outline)
#     # Draw the bottom of the box
#     print(outline * width)
#
# if __name__ == '__main__':
#     outline = input("Enter the outline of the box: ")
#     fill = input("Enter the fill of the box: ")
#     DrawBox(15,10,outline,fill)

# # practice 3 The default assignment in a function can be replaced by a new assignment.
# # # practice 2 Can choose between square border symbols and internal fill symbols.
# def DrawBox(width,height,outline="@",fill="."):
#     if width < 2 and height < 2:
#         print("Error:The width or height is too small!")
#         quit()
#
#     # Draw the top of the box
#     print(outline * width)
#     # Draw two legs of the box
#     for i in range(height - 2):
#         print(outline+fill*(width - 2)+ outline)
#     # Draw the bottom of the box
#     print(outline * width)
#
# if __name__ == '__main__':
#     DrawBox(10,10)
#     outline = input("Enter the outline of the box: ")
#     fill = input("Enter the fill of the box: ")
#     DrawBox(15,10,outline,fill)

# # practice 4 The sum of the first n terms of a geometric sequence
# # @param a : the first term in the sequence
# # @param r : the common ratio for the sequence
# # @param n : the number of terms to include in the sum
# # @return the sum of the first n term of the sequence
# def sumGeometric(a, r, n):
#     # Compute and return the sum when the common ratio is 1
#     if r == 1:
#         return a * n
#
#     s = a * (1 - r ** n) / (1 - r)
#     return s
#
# # The main body of using this function
# def main():
#     # initial the value from user
#     init = float(input("Enter the value of a (0 to quit):"))
#
#     while init !=0:
#         ratio = float(input("Enter the value of r :"))
#         num = int(input("Enter the value of n : "))
#
#         # Compute and display the total
#         total = sumGeometric(init, ratio, num)
#         print("The sum of the first ",num," terms is ",total)
#         init = float(input("Enter the value of a (0 to quit):"))
#
# if __name__ == '__main__':
#     main()

