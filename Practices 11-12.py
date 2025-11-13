# 第一章 练习11-12
# 练习11
# 加仑转换升的因子
import math

transGal = 3.7854
transMile = 1.609344
print("1单位加仑英里数(MPG)等于 %.4f" % (transGal / (transMile * 100)), "单位的百公里升数（L/100公里）")

# 练习12
# 目标点A的经纬度
t1 = float(input("请输入目标A的经度："))
g1 = float(input("请输入目标A的纬度："))
# 将经纬度的角度单位转化为弧度单位
T1 = math.radians(t1)
G1 = math.radians(g1)
# 目标点B的经纬度
t2 = float(input("请输入另一个目标B的经度："))
g2 = float(input("请输入另一个目标B的纬度："))
# 将经纬度的角度单位转化为弧度单位
T2 = math.radians(t2)
G2 = math.radians(g2)
# 计算两点的地球表面距离
dis = 6371.01 * math.acos(math.sin(T1) * math.sin(T2) + math.cos(T1) * math.cos(T2) * math.cos(G1 - G2))
print("目标两点在地球表面的距离为：", dis, "千米")
