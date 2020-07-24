formatter = "{} {} {} {}"
# formatter.format()函数，传递（）里的参数传递给formatter
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Try your", "Own text here", "Maybe a poem", "Or a song about fear"))
# 用f"" {}里必须是定义好的变量，不能是字符串
print(f"{formatter} or {True} or {1}")
num1 = "a, b, c, d"
print(num1.format())