# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate

def print_ip_table(list1, list2):
    res = {'Reachable': [], 'Unreachable': []}
    for i in list1:
        res['Reachable'].append(i)
    for i in list2:
        res['Unreachable'].append(i)
    print(tabulate(res, headers=['Reachable', 'Unreachable']))


if __name__ == "__main__":  
    print_ip_table(['172.41.128.128', '172.41.128.129', '172.41.128.130', '172.41.128.131', '172.41.128.132'], ["5.255.255.242", "192.168.0.1"])