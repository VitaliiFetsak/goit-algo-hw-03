# Модуль 3 ДЗ №3
import re

def normalize_phone(phone_number:str):

    
    # Виокремлення плюса та чисел з телефонного номеру
    pattern_num = r'\+|\d+'
    num = re.findall(pattern_num, phone_number)
    
    # Формування з масиву num чисел num-строки
    # з усіми числами та плюсом за наявності
    num = "".join(num)
    #print('num = ',num) # Перевірка
    
    # Додавання префіксів:
    match num[0]:
        case '3':
            num = '+' + num
        case '8':
            num = '+3' + num
        case '0':
            num = '+38' + num
        case _:
            num = '+380' + num 
    if len(num) !=13:   # Якщо номер введено невірно
        num = None 
    return num

list_of_numbers = [ "067\\t123 4567",
    "(050)8889900",
    "38050-111-22-22",
    "     0503451234",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "    +38(050)123-32-34",
    "380501234567",
    "38050 111 22 1   "]

sanitized_numbers = [normalize_phone(num) for num in list_of_numbers]

print('Нормалізовані номери телефонів для SMS-розсилки:\n', sanitized_numbers)