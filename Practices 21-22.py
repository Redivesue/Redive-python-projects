# 第一章 练习21-22
import math

# 练习21
b = float(input("请输入三角形底边的长度："))
h = float(input("请输入三角形底边对应的高的长度："))
area = (b * h) / 2
print("该三角形的面积为：", area)

# 练习22
s1 = float(input("输入三角形中较小边的边长："))
s2 = float(input("输入三角形中中间长边的边长："))
s3 = float(input("输入三角形中较大边的边长："))
s = (s1 + s2 + s3) / 2
area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
print("该三角形面积为：", area)
