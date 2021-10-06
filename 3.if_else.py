#  Условные операторы(: - синтаксический элемент)

var = 5

# if имеет условие 
# выполняет код внутри тела если услоеие истинно 
# if var != 0:
#     print("var не равно 0")

# if var != 5:
#     print("var не равно 0")

# if var < 0:
#     print("меньше нуля")
# else:
#     print("не меньше нуля") 

var = 'A'

if var == 'A':
    res = 'lit A'
elif var == 'B':
    res = 'lit B'
else:
    res = 'var is not A and B'

# print(res)


# Пример термостат

# текущая температура
current_temp = 25 

# диапазон температур которые должен поддерживать котел
min_temp = 21
max_temp = 26

# логика термостата
if current_temp < min_temp:
    print("Включен нагрев")
elif current_temp > max_temp:
    print("Выключен нагрев")
else:
    print("Температура оптимальна")

