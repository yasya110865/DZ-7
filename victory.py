
import random
import copy
def victory(n):

    date_dict = {
    'Альберт Эйнштейн':'14.03.1879',
    'Уильям Шекспир':'26.04.1564',
    'Опра Уинфри':'29.01.1954',
    'Махатма Ганди':'02.10.1869',
    'Дж.К. Роулинг':'31.07.1965',
    'Майкл Джексон':'29.08.1958',
    'Мартин Лютер Кинг': '15.01.1929',
    'Нельсон Мандела':'18.07.1918',
    'Мать Тереза':'26.08.1910',
    'Стив Джобс':'24.02.1955'
    }
    new_format_date = ['четырнадцатое марта 1879 года',
                       'двадцать шестое апреля 1564 года',
                       'двадцать девятое января 1954 года',
                       'второе октября 1869 года',
                       'тридцать первое июля 1965 года',
                       'двадцать девятое августа 1958 года',
                       'пятнадцатое января 1929 года',
                       'восемнадцатое июля 1918 года',
                       'двадцать шестое августа 1910 года',
                       'двадцать четвертое февраля 1955 года']
    date_dict_1 = date_dict.copy()

    new_format_dict = dict(zip(list(date_dict_1.keys()), new_format_date))

    sample_list = random.sample(list(date_dict.keys()), n)
    for sample in sample_list:
        date = input(f'Дата рождения {sample}: ')
        if date == date_dict[sample]:
            print('Верно!')
        else:
            print(f'Верный ответ: {new_format_dict[sample]}')

