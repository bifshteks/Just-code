from easygui import *
from calendar import *


m = (
        'Январь',
        'Февраль',
        'Март',
        'Апрель',
        'Май',
        'Июнь',
        'Июль',
        'Август',
        'Сентябрь',
        'Октябрь',
        'Ноябрь',
        'Декабрь'
        )
months = {
        'Январь': 1,
        'Февраль': 2,
        'Март': 3,
        'Апрель': 4,
        'Май': 5,
        'Июнь': 6,
        'Июль': 7,
        'Август': 8,
        'Сентябрь': 9,
        'Октябрь': 10,
        'Ноябрь': 11,
        'Декабрь': 12
            
            }

weekday = {
            1: 'Понедельник',
            2: 'Вторник',
            3: 'Среда',
            4: 'Четверг',
            5: 'Пятница',
            6: 'Суббота',
            7: 'Воскресенье'
            }

month = months[choicebox('Month:', 'Datelist', m)] # месяц цифрой
day = enterbox('Day:', 'Datelist') # число без нуля в начале

if day.startswith('0'): day = int(day[1:]) # yбираем ноль у day
else:  day = int(day)

# return (номер дня недели первого(пн - 0, вс - 6) , всего дней в месяце)
weekday_alldays = monthrange(2017, month) # ниже

wd = weekday_alldays[0] # день недели

for i in range(1, day + 1):
    wd += 1 if wd != 7 else -6

# ищем номер данного дня в году:
day_in_year = 0
for i in range(1, month):
    day_in_year += monthrange(2017, i)[1]
day_in_year += day
 

def get_subj(week, num_week):
    res = []
    for time, dict_of_time in prac[week].items():
        for subj, tupl_weeks in dict_of_time.items():
            if num_week in tupl_weeks:
                res.append(tuple([ time , subj ]))
        
    return res


num_weekday = round( (day_in_year - 1 - wd ) / 7  + 2)


prac = {
            'Понедельник': {'09:00 - 10:35': {'Физ - ра': (1,2,3,4,5,6,7,8,9)},
                            '10:55 - 12:30': {'Анатомия л': (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)},
                            '13:10 - 16:35': {'Уход': (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)}},      # [ str(time) , {subject1: [1 ,3 ,5 ,8], subject2: [2, 4, 6]}]
            'Вторник': {'09:00 - 12:30': {'Биология': (1,3,5,7,9,11,13), 'Латинский': (2,4,6,8,10,12,14,15,16,17)},
                        '13:10 - 14:45': {'Гиста': (1,2,3,4,5,6,7,8,9,10,11,12,13), 'Экономика': (14)},
                        '13:10 - 16:35': {'Экономика' : (15,16,17)}},
            'Среда': { '10:55 - 12:30': {'Экономика': (1,3,5,7,9,11,13,15,17)},
                       '13:10 - 16:35' : {'Химия': (2,4,6,8,10,12,13,14,15,16,17), 'Физика': (1,3,5,7,9,11)}},
            'Четверг': {'09:00 - 12:30': {'Анатомия': (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)},
                        '13:10 - 14:45': {'Инфа': (1,3,5,7,9),'Био': (2,4,6,8,10,11,12)},
                        '13:10 - 16:35': {'Ин.яз': (13,), 'Гиста': (14,), 'Латинский': (15,)}      },
            'Пятница': {'09:00 - 12:30': {'Экономика': (6,8,10,12,14,16,17)},
                        '10:50 - 12:30': {'Химия': (1,2,3,4,5,7,9,11,13,15)},
                        '13:10 - 16:35': {'Гиста': (1,3,5,7,9,11,12,13,14,15,16,17), 'Инфа': (2,4,6,8,10)}},
            'Суббота': {'09:00 - 12:30': {'Ин. яз.': (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)},
                        '13:10 - 14:45': {'Физика': (1,3,5,7,9,11)},
                        '13:10 - 16:35': {'Анатомия': (6,)}},
            'Воскресенье': {} 
            }
            
result = sorted(get_subj(weekday[wd], num_weekday), key=lambda t: int(t[0][:2]))
msgbox('\n'.join([' :  '.join((str(k[0]), str(k[1]))) for k in result]), 'Раписание')
if '__name__' == '__main__':
    month = months[choicebox('Month:', 'Datelist', m)]
    n = input()
