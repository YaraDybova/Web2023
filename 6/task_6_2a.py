# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip_addres = input("Введите IP адресс ")
correct_ip = True
if len(ip_addres.split(".")) == 4:
   for k in ip_addres.split("."):
      if not (k.isdigit() and int(k) < 256 and int (k) > 0):
         correct_ip = False
         break
else:
   correct_ip = False

if correct_ip:        
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
else:
   print("Вы ввели неккоректный ip адресc")