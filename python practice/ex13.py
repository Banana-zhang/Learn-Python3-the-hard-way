from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# 这个文件需要在终端调用，同时传入参数，如：
# 在该文件目录下输入：
# python ex13.py 1 2 3    它会返回4个值
# 这个函数会返回n+1个值，
# 第一个是文件名，之后依次是传入的参数。