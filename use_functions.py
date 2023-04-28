"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
def my_bill():
    import os
    import json
    if os.path.exists('my_bill.txt'):
        with open('my_bill.txt', 'r') as f:
            count = int(f.read())
    else:
        count = 0
    if os.path.exists('buy_history.json'):
        with open('buy_history.json', 'r') as f:
            history = json.load(f)
    else:
        history = {}

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')

        if choice == '1':
            top_up = int(input('На какую сумму пополнить счет?: '))
            count += top_up
            with open('my_bill.txt', 'w') as f:
                f.write(str(count))
        elif choice == '2':
            buy = input('Что покупаем?: ')
            price = int(input('Сколько это стоит?: '))
            if price > count:
                print('На вашем счету недостаточно средств')
            else:
                count -= price
                history[buy] = price
                print(f'Остаток на счету {count}')
                with open('my_bill.txt', 'w') as f:
                    f.write(str(count))
                with open('buy_history.json','w') as f:
                    json.dump(history, f)

        elif choice == '3':
            print(f'История покупок: {history}')
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
