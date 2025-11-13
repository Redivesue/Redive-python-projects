# 第一章 练习15-16
# 练习15
import math

dataInch = float(input("请输入英尺数据："))
print("相当于", dataInch * 12, "英寸", "\n相当于", dataInch * 1/3, "码", "\n相当于", dataInch * 0.00018939, "英里")

# 练习16
R= float(input("输入圆的的半径R："))
squareR = (R ** 2) * math.pi
capacityR = (R ** 3) * math.pi * (4/3)
print("以半径R的圆的面积：", squareR, "\n以半径R的球体体积为：", capacityR)