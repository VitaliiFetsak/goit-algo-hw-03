# Модуль 3 ДЗ №4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users:list) -> list:
    today = datetime.today().date()
    congratulation_list = []     
    
    for user in users:
        congratulation_user_dict = {} 
        user_birthday = datetime.strptime(user.get('birthday'), '%Y.%m.%d').date()
        
        birthday_this_year = datetime(year=today.year,
                                      month=user_birthday.month,
                                      day=user_birthday.day).date()
        
        if birthday_this_year < today:
            continue
        elif birthday_this_year.toordinal() - today.toordinal() >7:
            continue
        else:
            congratulation_date = datetime(year = today.year,
                                           month = birthday_this_year.month,
                                           day = birthday_this_year.day).date()
            if congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)
            elif congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
        
            congratulation_date = congratulation_date.strftime('%Y-%m-%d')
            congratulation_user_dict.update({'name': user['name'],
                                            'congratulation_date' : congratulation_date})
            congratulation_list.append(congratulation_user_dict)
    
    return congratulation_list

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Vasily Gr", "birthday": "1985.02.02"},
    {"name": "John Vick", "birthday": "1990.12.31"},
    {"name": "Joanna", "birthday": "1970.01.28"},
    {"name": "Victor", "birthday": "1900.01.29"}
]
print('users = \n',users)
upcoming_birthdays = get_upcoming_birthdays(users)

print('Список привітань на цьому тижні:\n', upcoming_birthdays)