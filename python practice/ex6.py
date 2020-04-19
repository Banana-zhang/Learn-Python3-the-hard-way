# round函数：四舍五入函数，第二个参数取小数点后n位
print(round(13.566666, 3))

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said:'{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny? ! {}"

print(joke_evaluation.format(hilarious))

w = "This is left side of..."
e = "a string with a right side"

print(w + e)
