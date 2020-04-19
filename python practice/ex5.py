# 格式化字符串
# 以f开头，引号里是内容，嵌入的变量放在{}里
# 不能嵌套
# 例 f"Hello {variable}"
my_name = 'Zad A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeeh = 'White'
my_hair = 'brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f'He"s {my_weight} pounds heavy.')
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
