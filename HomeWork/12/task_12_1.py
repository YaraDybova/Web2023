# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(list_ip):
    ping = []
    no_ping = []
    for ip in list_ip:
        # result = subprocess.run("ping {}".format(ip))
        # to_subprocess = ['ping', ip]
        to_subprocess = ['ping', ip, '-n', '1']
        result = subprocess.run(to_subprocess)
        if result.returncode == 0:
            ping.append(ip)
        elif not result.returncode == 0:
            no_ping.append(ip)
    res = tuple([ping, no_ping])
    return res

if __name__ == "__main__":
    list_ip = ["5.255.255.242", "192.168.0.1", "62.122.170.171", "1.255.2.255"]
    print(ping_ip_addresses(list_ip))