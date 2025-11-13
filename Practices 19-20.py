# 第一章 练习19-20
# 练习19
import math
gravity = 9.8
v_i = float(input('请输入物体下落的初始速度为：'))
d = float(input("请输入物体自由落体的距离："))
v_f = math.sqrt(v_i ** 2 + 2 * gravity * d)
print("物体最终速度为：", v_f, "米/秒")

# 练习20
Pressure = 2000 * (10 ** 4)
Volume = 12
Temperature = 20 + 273.15
R = 8.314
print("一个典型的SCUBA水箱中的气体量为：", Pressure * Volume /(Temperature * R), "mol")