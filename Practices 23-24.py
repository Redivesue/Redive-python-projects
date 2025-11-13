# 第一章 练习23-24
import math

# 练习23
n = int(input("请输入正多边形的边数："))
s = float(input("请输入正多边形的边长："))
area = n * (s ** 2) / 4 * (math.pi / n)
print("边长为：", s, "的正", n, "边形的面积为：", area)

# 练习24
day = int(input("用户持续时间的天数："))
hours = float(input("用户持续时间的小时数："))
minutes = float(input("用户持续时间的分钟数："))
seconds = float(input("用户持续时间的秒数："))
totalSeconds = day * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
print("持续时间所表示的总秒数为：", totalSeconds)

