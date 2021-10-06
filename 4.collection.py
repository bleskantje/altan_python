# Коллекции
# Список (list)

# Создание пустого списка
my_list = []
my_list = list()

# добавление объекта (элемента) в список
my_list.append(100)
my_list.append(3.14)
my_list.append("hello")
my_list.append([10,20,30,40])

# чтение элемента списка
# прямая индексация (слева направо)

el = my_list[3]
el = my_list[0]

# обратная индексация
el = my_list[-1]

# замена элементов 
my_list[0] = 777.0

# удаление элементов по значению
my_list.remove(3.14)

# удаление элемента по индексу
del my_list[-1]

# срез списка

# создание исходного списка из строки
s = "hello, world"
my_list = list(s)

# срез от начала до конца
my_slice = my_list[:]

# срез с 2 индекса до конца исходного списка
my_slice = my_list[2:]

# срез со второго до 10 индекса не включительно с шагом 2
my_slice = my_slice[2:10:2]

# переворот списка
my_slice = my_list[::-1]

# длину можно узнать можно с помощью функции len()
print(len(my_list))

print(my_list)
print(my_slice)
# print(el)