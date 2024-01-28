# Модуль 3 ДЗ №2
import random

def get_numbers_ticket(min, max, quantity):
# Перевірка відповідності типів  
    if type(min) != int or type(max) != int or type(quantity) != int:
        return []
# Перевірка на ліміти мін, макс та чи вибірка не більша за діапазон можливих значень
    elif (min < 1) or (max > 1000) or (min > max) or (quantity > (max - min + 1)):
        return []
     
    list_numbers_ticket = []
    while len(list_numbers_ticket) < quantity:
             el = random.randint(min, max)
             if not el in list_numbers_ticket:
                 list_numbers_ticket.append(el)
    list_numbers_ticket.sort()
    return list_numbers_ticket
 
min = 1
max = 49
quantity = 6 

lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа: ", lottery_numbers)