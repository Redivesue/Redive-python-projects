# 第一章 练习13-14
# 练习13
# 将两美元硬币和一美元硬币转换为美分
cents_per_toonie = 200
cents_per_loonie = 100
# 读取用户的整数
cents = int(input("顾客所给的现金："))
# 先判断需要找多少二美元硬币
print("需要找的二元硬币的数量为：", cents // cents_per_toonie, "个")
centsRemain = cents % cents_per_toonie
# 后判断需要找多少一元硬币
print("需要找的一元硬币的数量为：", centsRemain // cents_per_loonie, "个")
centsRemain = centsRemain % cents_per_loonie
# 判断需要多少25分硬币
print("需要找的25分硬币的数量为：", centsRemain // 25, "个")
centsRemain = centsRemain % 25
# 判断需要多少10分硬币
print("需要找的10分硬币的数量为：", centsRemain // 10, "个")
centsRemain = centsRemain % 10
# 判断需要多少5分硬币
print("需要找的5分硬币的数量为：", centsRemain // 5, "个")
centsRemain = centsRemain % 5
# 判断需要多少1分的硬币
print("需要找的1分硬币的数量为：", centsRemain // 1, "个")

# 练习14
lenFt = int(input("请输入身高的英尺数："))
lenIn = int(input("请输入身高的英寸数："))
print("这个人的身高为：", (lenFt * 12 + lenIn) * 2.54, "厘米")
