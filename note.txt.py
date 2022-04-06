#变量：可以看成一个盛装数据的盒子。名字独一无二，从底层看，程序中的数据最终都要放到内存中，变量就是这块内存的名字
只能包含字母、数字和下划线，字母下划线大头，不能以数字。"_"代替空格

	print(name.title())	大写
	print(name.lower())	小写
	\n换行 \t缩进
	print(name.rstrip())	去处末尾空格
	print(name.lstrip())/print(name.strip())
	print（str(123))	数值转字符串


#列表：
cars = ['trek', 'redline', 'specialized']
	cars[123]

	cars.append('abc')	末尾添加一个元素
	del cars[123]	删除指定元素
	cars.pop('123')	删除末尾元素
	cars.remove('abc')

		cars.sort(reverse=True))	按字母永久排序
		cars.sorted(reverse=True))	按字母临时排序
		cars.reverse()	列表反序
		len(cars)	列表长度

	for car in cars: for 循环

	range(1,3):	生成1	2

	numbers = list(range(1,6))	数字生成列表
	numbers**2	乘方
	#列表解析
		squares = []
		for value in range(1,11):
			square = value**2
			squares.append(square)
		print(squares)

		chenfangs = [value**2 for value in range(1,11)]
		print(chenfangs)

	#数值计算
	>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	>>> min(digits)
	0
	>>> max(digits)
	9
	>>> sum(digits)
	45

	#切片
	players = ['charles', 'martina', 'michael', 'florence', 'eli']
	print(players[-3:])
		#切片复制
		friend_foods = my_foods[:]#可各自独立修改

#'元组'元素不可修改，可给元组重新赋值()，'列表'可编辑[],字典内元素键值对应{}
alien_0 = {'color': 'green'}

#字典
	alien_0 = {'color': 'green', 'points': 5}
	print(alien_0)
	alien_0['x_position'] = 0
	alien_0['y_position'] = 25
	print(alien_0)

	#遍历字典	for k, v in user_0.items()

集合类似元组，不可重复

s = {'python', 'hello', 5}




#if语句
	判断相等==
	不等！=
	多个判断and，or
	#元素是否存在列表内
	in，不在not in

	#if else
	age = 17
	if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
	else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
	#if-elif-else 多个条件单个判断

	#多条件持续判断
	if*:
	if*:
	if*:

#input()
	message = input("Tell me something, and I will repeat it back to you: ")
	print(message)

#while
	x = 1
	while x <= 5:
		print(x)
		x += 1

#创建列表
for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以
跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user.title())

print("\nThe following users have been confirmed：\n\t")
for confirmed_user in confirmed_users:
    print(confirmed_user)

#打印调查结果
	responses = {}

	active = True

	while active:
		ask = input("what's your name? ")
		place = input("If you could visit one place in the world,where would you go? ")

		responses[ask] = place
		print(ask + " want to go to the " + place + ".")
		repeat = input("Somebody else? (yes/no)")

		if repeat == 'yes':
			active = True
		else:
			active = False
	print(responses)

	#形参、实参

函数后面必须跟括号
def get_formatted_name(first_name, last_name, middle_name=''):#非默认参数不能跟随默认参数
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)






































































