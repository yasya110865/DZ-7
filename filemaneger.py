from victory import victory as vic
from use_functions import my_bill
import os
import shutil
import json
while True:
    print('1.создать папку')
    print('2.удалить файл/папку')
    print('3.копировать файл/папку')
    print('4.просмотр содержимого рабочей директории')
    print('5.посмотреть только папки')
    print('6.посмотреть только файлы')
    print('7.просмотр информации об операционной системе')
    print('8.создатель программы')
    print('9.играть в викторину')
    print('10.мой банковский счет')
    print('11.смена рабочей директории')
    print('12.выход')

    choice = int(input('Выберите пункт меню'))

    if os.path.exists('listdir.json'):
        with open('listdir.json', 'r') as f:
            listdir = json.load(f)
    else:
        listdir = {}
    if choice == 1:
        dir = input('Имя каталога: ')
        if not os.path.exists(dir):
            os.mkdir(dir)
    elif choice == 2:
        dir = input('имя каталога для удаления: ')
        if os.path.exists(dir):
            os.rmdir(dir)
    elif choice == 3:
        filename = input('Имя файла для копирования: ')
        newfilename = input('Имя нового файла: ')
        shutil.copyfile(filename, newfilename)
    elif choice == 4:
        print(os.listdir(os.getcwd()))
    elif choice == 5:

        path = os.getcwd()
        dirlist = []
        for i in os.listdir(path):
            if os.path.isdir(os.path.join(path, i)):
                dirlist.append(i)
        print(dirlist)
        listdir['dirs'] = dirlist
        with open('listdir.json', 'w') as f:
            json.dump(listdir, f)
    elif choice == 6:
        path = os.getcwd()
        filelist = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))]
        print(filelist)
        listdir['files'] = filelist
        with open('listdir.json', 'w') as f:
            json.dump(listdir, f)
    elif choice == 7:
        print(os.uname())
    elif choice == 8:
        print(os.getlogin())
    elif choice == 9:
        n = int(input('Сколько раз играем?: '))
        vic(n)
    elif choice == 10:
        my_bill()
    elif choice == 11:
        dirname = input('Введите имя директории ')
        os.chdir(dirname)
    elif choice == 12:
        break
    else:
        print('Неверный пункт меню')
