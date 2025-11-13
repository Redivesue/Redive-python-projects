# 第一章 练习17-18
# 练习17
waterC = 4.186
waterCapacity = float(input("请输入水的体积（毫升）："))
waterTemperature = float(input("请输入水需要发生的温度变化（摄氏度）："))
heat = waterCapacity * waterC * waterTemperature
print("水发生改温度变化所必须的总能量为：", heat, "焦耳")

# 扩展程序
transJ_to_kwh = 1 / 3600000
elecCast = 8.9
waterCast = heat * transJ_to_kwh * elecCast
print("加热水的成本为：", waterCast, "美分")

# 练习18
import math
r = float(input("请输入圆柱体底部圆的半径为："))
height = float(input("请输入圆柱体的高为："))
capacity = math.pi * (r ** 2) * height
print("圆柱体的体积为：%.1f" % capacity)
