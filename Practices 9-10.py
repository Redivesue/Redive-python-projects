# 第一章 练习9-10
# 练习9
account_year0 = float(input("请输入您账户初始存入的金额："))
account_year1 = account_year0 * 1.04
print("第一年获得利息后的账户金额：%.2f." % account_year1)
account_year2 = account_year1 * 1.04
print("第二年获得利息后的账户金额：%.2f." % account_year2)
account_year3 = account_year2 * 1.04
print("第三年获得利息后的账户金额：%.2f." % account_year3)

# 练习10
import math
a = int(input("请输入一个正整数："))
b = int(input("请输入另一个正整数："))
print("两个数之和：", a + b, "\n两个数之差（前减后）：", a - b, "\n两个数之积：", a * b, "\n两个数之商（前除后）:", a / b)
print("前除以后的余数：", a % b, "\n前一个数对10的对数：", math.log10(a), "\n前一个数的后一个数次方：", a ** b)

