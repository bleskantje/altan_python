# Полиморфизм

# поли + морф - разные формы чего-то

# Полиморфизм операторов


res = 100 + 30 # сложение
res = "100 + 30" # конкатинация

# print(res)

# Полиморфизм функций
res = len("python")
res = len([10, 20, 30])

# print(res)

# Полиморфизм методов

class A: 
    def m1(self, arg):
        print(arg + 10)

class B:
    def m1(self, arg):
        print(arg * 2)

obj1 = A()
obj2 = B()

# obj1.m1(100)
# obj2.m1(100)

class C(A):
    pass

class D(A):
    def m1(self):
        print("python")

# obj3 = C()
# obj3.m1(100)

# obj4 = D()
# obj4.m1()


# Полиморфизм с "магическими" методами (методы перегрузки операторов)

# метод, дающий объектам функциональную способность (способность функций)

class Sum:
    # def compute(self, a, b):
    #     print(a + b)
    def __call__(self, a, b):
        print(a + b)

    def __str__(self):
        return "I am Sum obj"

s = Sum()
# s.compute(10, 20)
# s(10, 20)

# print(s)

# Инкапсуляция 

# инкапсуляция - скрытие атрибутов (свойств) и/или методов

# не строгая инкапсуляция 
class X:
    def __init__(self, arg):
        self._attr = arg # _ - проявление нестрогой инкапсуляции

    def _method(self):
        print("Hello!")

x = X(10)
x._attr = 2000
# print(x._attr)
# x._method()

# Строгая инкапсуляция

class Y:
    def __init__(self, arg):
        self.__attr = arg # __ - проявление строгой инкапсуляции

    def __method(self):
        print("Hello!")

y = Y(5)
# print(y.__attr)
# y._method()

# Обходной путь

# print(y._Y__attr) # _class__arg - конструкция для доступа к обьектам со строгой инкапсуляцией
# y._Y__method() # _class__method - конструкция для доступа к обьектам со строгой инкапсуляцией

# Композиция (Агрегация)

class Neuron:
    def __call__(self, x, w):
        s = x[0] * w[0] + x[1] * w[1] + x[2] * w[2]
        return s

class Net:
    n0 = Neuron() # в другом классе создаем объекты другого класс
    n1 = Neuron()
    n2 = Neuron()
    n3 = Neuron()
    def __call__(self, *data):
        res = []
        res.append(self.n0(data, [-1,5, 0.0, 0.75]))
        res.append(self.n1(data, [0,5, 0.5, 1.7]))
        res.append(self.n2(data, [-2,5, -1.0, 0.5]))
        res = self.n3(res, [-2,5, -1.0, 0.5])
        print(res)

nn = Net()

nn(0.1, 0.8, 0.5)



