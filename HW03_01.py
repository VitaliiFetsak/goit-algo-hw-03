# Модуль 3 ДЗ №1
from datetime import datetime
   
def get_days_from_today(date): # За умовчання час буде 00:00:00, якщо явно не вказано
    
    # Перевірка на коректність введеної дати методом try ... except
    is_not_data = True
    while is_not_data:
        try:
            parsing_date = datetime.strptime(date, '%Y-%m-%d').date() # Відокремлення дати від часу
            is_not_data = False
        except Exception as error: # Опрацювання винятку - запрошення коректно ввести дату
            print(f'Помилка вводу: {error}')
            print(f'Введена дата не відповідає формату "РРРР-ММ-ДД"')
            date = input('Введіть дату в форматі "РРРР-ММ-ДД":')
    
    # current_date = datetime(year=2021, month=5, day=5) # Тестове значення
    current_date = datetime.today().date() # Визначення теперішньої дати і часу та відокремлення дати від часу
    
    difference = parsing_date.toordinal() - current_date.toordinal()

    return difference
    
        
date = '2024-01-23'
    
print(f'Для дати = {date}\n\
і поточної дати = {datetime.today().date()}\n\
різниця {get_days_from_today(date)}')