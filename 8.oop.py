# *** Основы объектно-ориентированного программирования (ООП) ***

# Объекты обладают свойствами и методами
# каждый объект принадлежит определенному классу (типу) или классам
# Класс - "чертеж" объекта.
# Конкретный реализованный объект называется экземпляр (инстанс) класса.

# Создание (определение) класса. Название принято писать с заглавной буквы.
class Cat:
	# метод-конструктор
	def __init__(self):
		# свойство (атрибут, поле)
		self.name = None
		self.color = None

	# метод (атрибут-метод) - функция, принадлежащая классу
	def mur(self):
		print("mur-mur!")
		print(f"Name: {self.name}, color: {self.color}")

# создание объекта (экземпляра) на базе класса Cat
cat_1 = Cat()
cat_2 = Cat()

# запись данных в свойства
cat_1.name = "Gaf"
cat_1.color = "white"

cat_2.name = "Pushok"
cat_2.color = "black"

# чтение данных из свойств
# print(cat_1.name)
# print(cat_2.name)

# вызов метода экземпляров
# cat_1.mur()
# cat_2.mur()


# *** Принципы ООП ***

# Принцип Наследования

# создание родительского (предкового) класса
class Animal:
	def __init__(self, legs):
		self.legs = legs

	def move(self):
		print("Я двигаюсь!")

# создание дочерних классов
class Human(Animal):
	def __init__(self, name, legs):
		super().__init__(legs) # обращение к родителю с вызовом его метода
		self.name = name
	
	def speech(self):
		print(f"My name is {self.name}. Legs: {self.legs}")

class Cat_2(Animal):
	def __init__(self, name, legs, color):
		super().__init__(legs)
		self.name = name
		self.color = color

	def speech(self):
		print(f"My name is {self.name}. Legs: {self.legs}. Color: {self.color}")

	def mur(self):
		print("Mur-mur!")

# Создание объектов
bug = Animal(6)

man_1 = Human("Petya", 2)
women_1 = Human("Katya", 2)

cat_1 = Cat_2("Pushok", 4, "red")
cat_2 = Cat_2("Juchka", 4, "green")


# использование объекта
bug.move()
print(bug.legs)

man_1.move()
man_1.speech()
women_1.move()
women_1.speech()

cat_1.move()
cat_1.speech()
cat_1.mur()



