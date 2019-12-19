"""
Написать функцию host_ping(), в которой с помощью утилиты ping будет
проверяться доступность сетевых узлов. Аргументом функции является список,
в котором каждый сетевой узел должен быть представлен именем хоста или
ip-адресом. В функции необходимо перебирать ip-адреса и проверять их
доступность с выводом соответствующего сообщения («Узел доступен»,
«Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться
с помощью функции ip_address().
"""

import subprocess
import os
import chardet
from ipaddress import ip_address
from pprint import pprint

HOST_LIST = ['10.0.0.1', '8.8.8.8', '192.168.0.1', '5.61.239.21', 'yandex.ru',
             '194.58.97.31']
result = {'Доступные узлы': '', 'Недоступные узлы': ''}

DNULL = open(os.devnull, 'w')  # заглушка, чтобы поток не выводился на экран


def is_ip_adress(ip):
    """
    Проверка на корректность IP-адресо
    :param ip: IP
    :return: ipv4: полученный ip адрес из переданного значения
        Exception: ошибка при невозможности получения ip адреса из значения
    """
    try:
        ipv4 = ip_address(ip)
    except ValueError:
        raise Exception("Некорректный ip адрес")
    return ipv4


def host_ping(host_list, get_list=False):
    for host in host_list:
        try:
            ipv4 = is_ip_adress(host)
        except Exception:
            print(f'{host} - доменное имя')
            ipv4 = host
        # ping_test = subprocess.Popen(['ping -с 1', str(ipv4)], stdout=DNULL)
        ping_test = subprocess.Popen(
            ['ping', '-n', '1', str(ipv4)], stdout=subprocess.PIPE)
        DATA = ping_test.stdout.read()
        RES = chardet.detect(DATA)
        print_res = DATA.decode(RES['encoding'])

        if print_res.find("потеряно = 0") != -1:
            result['Доступные узлы'] += f'{str(ipv4)}, '
            res_string = f'{str(ipv4)} - Узел доступен'
        else:
            result['Недоступные узлы'] += f'{ipv4}, '
            res_string = f'{str(ipv4)} - Узел недоступен'
        if not get_list:  # если результаты не надо добавлять в словарь,
            # значит отображать их в консоли
                print(res_string)
    if get_list:  # если требуется вернуть словарь (для задачи 3),
        # то возвращаем
        return result


if __name__ == '__main__':
    host_ping(HOST_LIST)
    pprint(result)
