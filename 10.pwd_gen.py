# генератор паролей

# import tkinter
from tkinter import Tk, StringVar, Label, Entry, Button # класс для создания объекта окна
import hashlib
# stringVar умеет хранить строки
# Label - текст
# Entry - текстовое поле
# Button - кнопочка

# объект окна
window = Tk()
window.title("Генератор паролей v 0.1")

# основная функция
def generator():
    """
    Функция хэширования строк паролей
    """
    # прием строки сырого пароля
    pwd_str = pwd.get()

    # кодирование в байт-строку
    byte_str = pwd_str.encode()

    # хеширование (применение хеш-функции)
    hash_str = hashlib.sha256(byte_str)

    # преобразование хеш-строки в обычную строку
    hex_str = hash_str.hexdigest()[:10]

    # print(hex_str)

    # запись хеш-строки в объект StringVar
    hash_pwd.set(hex_str)

# generator("password")

# контейнеры для хранения строк
pwd = StringVar()
hash_pwd = StringVar()

# виджет (компонент) текстовой метки
Label(text="Пароль:").grid(row=0, column=0, padx=5, pady=5)
# виджет поля ввода
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)
# виджет кнопки
btn = Button(text="Старт", command=generator)
btn.grid(row=1, column=0, padx=5, pady=5)
# виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=1, column=1, padx=5, pady=5)

# запуск программы (точка входа программы)
window.mainloop()

