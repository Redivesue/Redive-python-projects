# 第一章 练习25-26
import math
from time import asctime

# # 练习25
# totalSeconds =int(input("请输入用户持续的总秒数："))
# # 计算天数
# days = totalSeconds // 86400
# # 更新剩余秒数
# totalSeconds = totalSeconds - (86400 * days)
# #计算小时
# hours = totalSeconds // 3600
# #更新秒数
# totalSeconds = totalSeconds - (3600 * hours)
# #计算分钟
# minutes = totalSeconds // 60
# #更新秒数
# totalSeconds = totalSeconds - (60 * minutes)
#
# #格式化展示结果
# print("D:HH:MM:SS"+"  ---->  "+"%d" % days+":"+f"{hours:02d}"+":"+f"{minutes:02d}"+":"+f"{totalSeconds:02d}")


# 练习26
current_time = asctime()
print(current_time)

