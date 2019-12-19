"""
Написать функцию host_range_ping() для перебора ip-адресов из заданного
диапазона. Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""
from hw11 import is_ip_adress, host_ping


def host_range_ping(get_list=False):
    while True:
        # запрос первоначального адреса
        start_ip = input('Введите первоначальный адрес: ')
        try:
            ipv4_start = is_ip_adress(start_ip)  # пробуем привести к ip-адресу

            # смотрим чему равен последний октет
            last_oct = int(start_ip.split('.')[3])
            break
        except Exception as e:
            print(e)
    while True:

        # запрос на количество проверяемых адресов
        end_ip = input('Сколько адресов проверить?: ')
        if not end_ip.isnumeric():
            print('Необходимо ввести число: ')
        else:
            # по условию меняется только последний октет
            if (last_oct + int(end_ip)) > 254:
                print(
                    f"Можем менять только последний октет, "
                    f"т.е. максимальное число хостов для проверки: "
                    f"{254 - int(end_ip)}")
            else:
                break

    HOST_LIST = []
    # формируем список ip адресов
    [HOST_LIST.append(str(ipv4_start + x)) for x in range(int(end_ip))]

    # передаем список в функцию из задания 1 для проверки доступности
    # (словарь не нужен)
    if not get_list:
        host_ping(HOST_LIST)

    # передаем список в функцию из задания 1 для проверки доступности
    # (отдаем словарь)
    else:
        return host_ping(HOST_LIST, True)


if __name__ == '__main__':
    host_range_ping()
