"""
Написать функцию host_range_ping_tab(), возможности которой основаны
на функции из примера 2. Но в данном случае результат должен быть итоговым
по всем ip-адресам, представленным в табличном формате (использовать модуль
tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:

Reachable       Unreachable
-------------   -------------
10.0.0.1        10.0.0.3
10.0.0.2        10.0.0.4
"""

# для формирования списка хостов и проверки доступности используем
# функцию из задания 2
from hw12 import host_range_ping
from tabulate import tabulate


def host_range_ping_tab():
    """
           Запрос диапазона ip адресов,проверка их доступности, вывод результатов в табличном виде
           :param
           :return:
           """
    # запрашиваем хосты, проверяем доступность, получаем словарь результатов
    res_dict = host_range_ping(True)
    print()
    # выводим в табличном видк
    print(tabulate(
        [res_dict], headers='keys', tablefmt="pipe", stralign="center"))


if __name__ == "__main__":
    host_range_ping_tab()