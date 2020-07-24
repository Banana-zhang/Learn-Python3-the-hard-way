# input() 只会输出字符串，要想让输入的数字参与计算可以用int转换成整型
print(type(int(input(25))))

print("How old are you? ", end="")
age = input()
print("How tall are you? ", end='')
height = input()
print("How much do you weigh? ", end=" ") # 注意end=“”里面有没有空格的区别
weight = input()
print(f"So, you're {age} old, {weight} tall and {weight} heavy.")
