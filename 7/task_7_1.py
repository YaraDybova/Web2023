# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}"""

with open('ospf.txt') as f:
    for ospf_route in f:
        ospf_route = ospf_route[1:]
        ospf_route = ospf_route.replace(',', '').replace('via', '').strip()
        item_list = ospf_route.split()
        print(template.format(item_list[0], item_list[1].strip('[]'), item_list[2], item_list[3], item_list[4]))