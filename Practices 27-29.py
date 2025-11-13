# practice 27
## Anonymous Gregorian Computus
# 输入年份
year = int(input('Enter a year: '))
## AGC 算法准备的元素：a,b,c,d,e,f,g,h,i,k,l
a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2 * e + 2 * i - h - k) % 7
m = (a + 11 * h + 22 * l) // 451
## 计算当年复活节的月份和天
month = (h+l-7*m+114) // 31
day = (h+l-7*m+114) % 31 +1
# 打印结果
print(f"{year}年的复活节的日期是："+f"{month}月{day}号")

# practice 28
# height in int , weight in ponds
height = int(input('Enter a height(int): '))
weight = int(input('Enter a weight(pond): '))
bmi = (weight * 703) / (height * height)
print(f'your BMI in int/pond system is:{bmi:.1f}')

# height in cm, weight in kg
height = int(input('Enter a height(cm): '))
weight = int(input('Enter a weight(kg): '))
bmi = weight / (height * height)

# practice 29
# input elements
t_a = float(input("Enter the temperature (C LESS THAN 10C):"))
v = float(input("Enter the wind speed (km/h better than 4.8km/h):"))
wci = 13.12 + 0.6215 * t_a - 11.37 * v ** 0.16 + 0.3965 * t_a * v ** 0.16
print(f"Current Wind Chill Index（WCI）is ： {wci:.4f}")

