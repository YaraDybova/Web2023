# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    with open(config_filename, "r") as f:
        access_dictionary = {}
        trunk_dictionary = {}
        flag = False
        for line in f:
            if "interface FastEthernet" in line:
                interface = line.split()[1]
                line = f.readline()
                flag = True
            elif "access vlan" in line:
                access_dictionary[interface] = int(line.split()[3])
                flag = False
            elif "trunk allowed vlan" in line:
                str_trunk = line.split()[4].split(",")
                int_list_trunk = [int(elem) for elem in str_trunk]
                trunk_dictionary[interface] = int_list_trunk
                flag = False
            elif flag == True:
                access_dictionary[interface] = 1
    print("access_dictionary:\n", access_dictionary)
    print("trunk_dictionary:\n", trunk_dictionary)
    return (access_dictionary, trunk_dictionary)

get_int_vlan_map("09_functions\config_sw2.txt")