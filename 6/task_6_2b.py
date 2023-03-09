# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

correct_ip = False
while correct_ip == False:
    ip_addres = input("Введите IP адресс ")
    correct_ip = True
    if len(ip_addres.split(".")) == 4:
        for k in ip_addres.split("."):
            if not (k.isdigit() and int(k) < 256 and int (k) > 0):
                correct_ip = False
                break
    else:
        correct_ip = False
    if correct_ip == False:
        print("Вы ввели неккоректный ip адрес")
    

first_byte = int(ip_addres.split(".")[0])
if first_byte > 0 and first_byte < 224:
    print("unicast")
elif first_byte > 223 and first_byte < 240:
    print("multicast")
elif ip_addres == "255.255.255.255":
    print("local broadcast")
elif ip_addres == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
