# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def parse_cdp_neighbors(show):
    with open(show) as file:
        show = file.read()
        q = {}
        show = show.split('\n')
        for line in show:
            main = []
            second = []
            if line.find('>') != -1:
                main_machine = line[:line.find('>')]
            elif line.find('Eth') != -1:
                second_machine, main_eth, main_inter, *other, second_eth, second_inter = line.split()
                main.append(main_machine)
                second.append(second_machine)
                main_interface = main_eth + main_inter
                second_interface = second_eth + second_inter
                main.append(main_interface)
                second.append(second_interface)
                main_tuple = tuple(main)
                second_tuple = tuple(second)
                q[main_tuple] = second_tuple
    return q
if __name__ == "__main__":
    q = parse_cdp_neighbors('sh_cdp_n_sw1.txt')
    print(q)
