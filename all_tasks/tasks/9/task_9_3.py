# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    with open(config_filename, "r") as f:
        access_dictionary = {}
        trunk_dictionary = {}
        for line in f:
            if "interface FastEthernet" in line:
                interface = line.split()[1]
            elif "access vlan" in line:
                access_dictionary[interface] = int(line.split()[3])
            elif "trunk allowed vlan" in line:
                str_trunk = line.split()[4].split(",")
                int_list_trunk = [int(elem) for elem in str_trunk]
                trunk_dictionary[interface] = int_list_trunk
    print("access_dictionary:\n", access_dictionary)
    print("trunk_dictionary:\n", trunk_dictionary)
    return (access_dictionary, trunk_dictionary)

get_int_vlan_map("09_functions\config_sw1.txt")