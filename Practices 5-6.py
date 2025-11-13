# 第一章 练习5-6
# 练习5
lessCapacity = float(input("请输入容量小于等于一升的容器的数量："))
moreCapacity = float(input("请输入容量大于一升的容器的数量："))
refund = lessCapacity * 0.1+moreCapacity * 0.25
print("总共的退款金额为：$%.2f."%refund)


# 练习6
originalFee = float(input("请输入本顿饭的费用为："))
consumptionTax = originalFee * 0.22
tips = originalFee * 0.18
totalFee = originalFee + consumptionTax + tips
print("消费税金额为：%.2f."%consumptionTax,"\n小费的金额为：%.2f."%tips,"\n包括税和小费的总餐费为：%.2f."%totalFee)

