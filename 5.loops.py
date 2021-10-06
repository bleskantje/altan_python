# *** Циклы (операторы циклов) ***

# Оператор while

# бесконечный цикл (условие всегда True)
# while True:
# 	print("Hello!")

# while с условием
num = 0
# while num < 10:
# 	print(num)
# 	# инкремент
# 	# num = num + 1 # длинная запись
# 	num += 1 # короткая запись
# 	print(num)

# прерывание цикла по дополнительному условию
num = 10

# while True:
# 	if num == 5:
# 		# инструкция прерывания цикла
# 		break
# 	print(num)
# 	# декремент
# 	num -= 1

# while num < 100:
# 	print("Hello!")
# 	s = input("Введите команду: ")
# 	if s == "stop":
# 		print("Bye bye!")
# 		break
# 	print(f"Вы ввели: {s}")
# 	num += 30

# пропуск куска кода в теле цикла
# while True:
# 	s = input("Введите слово ДА: ")
# 	if s == "ДА":
# 		print("цикл продолжается!")
# 		continue
# 	print("конец цикла")
# 	break


# Оператор for

# 1. читает элемент итерируемого объекта по порядку
# 2. значение элемента присваивается в свою переменную
# 3. выполняет блок кода своего тела

# for n in [1,2,3,4,5]:
# 	print(n)

# for n in (10,20,30,40):
# 	print("hi")

# for _ in (10,20,30,40):
# 	print("hi")

# for char in "python":
# 	print(char)

my_tuple = (10,20,30,40)

# for n in my_tuple:
# 	res = n * 2
# 	print(res)

# for n in my_tuple[::-1]:
# 	res = n + 2
# 	print(res)

# r = range(5, 10)
# print(r)

# for i in range(5, 10, 2):
# 	print(i)

# for i in range(10):
# 	print(i)

for i in range(5, 10)[::-1]:
	print(i)

# генератор списка, кортежа, словаря