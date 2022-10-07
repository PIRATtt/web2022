# Задание 12.1
# Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса. Функция ожидает как аргумент список IP-адресов.
import subprocess
from pythonping import ping

ip=['1.1.1.1', '5.5.5.5', '8.8.8.8']

def ping_ip_addresses(ip_list):
    good=[]
    bad=[]
    for ip in ip_list:
        result =subprocess.run(['ping', '-n', '1', ip], stdout=subprocess.DEVNULL, encoding="utf-8")
        if result.returncode == 0:
            good.append(ip+' {}'.format(str(check_ip(ip))))
        else:
            bad.append(ip+' {}'.format(str(check_ip(ip))))
    return tuple(good), tuple(bad)

def check_ip(ip):
    ping_check=str(ping(ip, count=1))
    if ping_check.startswith('Reply')==True:
        return True
    elif ping_check.startswith('Request')==True:
        return False

if __name__ == '__main__':
    # print(ping(ip))
    print('Пингующиеся ip-адреса:', ping_ip_addresses(ip)[0])
    print('НЕ пингующиеся ip-адреса:', ping_ip_addresses(ip)[1])


# Задание 12.2
# Функция ping_ip_addresses из задания 12.1 принимает только список адресов, но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.
# import subprocess
# from pythonping import ping

# ip=['1.1.1.1', '5.5.5.5', '8.8.8.2-6', '10.10.10.5-10.10.10.10']
# def sort_ip(ip_list):
#     ip=ip_list
#     dell=[]
#     for i in ip:
#         if '-' in i:
#             dell.append(i)
#             i2=i.split('-')
#             if '.' in i2[1]:
#                 if int(i2[0].split('.')[3])<int(i2[1].split('.')[3]):
#                     for num in list(range(int(i2[0].split('.')[3]), int(i2[1].split('.')[3])+1)):
#                         i2[0]=i2[0].replace('{}'.format(i2[0].split('.')[3]), str(num))
#                         ip.append(i2[0])
#                 else:
#                     print('ERROR!!! Не правильно ввели ip!')
#             else:
#                 if i2[1].isdigit()==True:
#                     if int(i2[0].split('.')[3])<int(i2[1]):
#                         for num in list(range(int(i2[0].split('.')[3]), int(i2[1])+1)):
#                             i2[0]=i2[0].replace('{}'.format(i2[0].split('.')[3]), str(num))
#                             ip.append(i2[0])
#                 else:
#                     print('ERROR!!! Не правильно ввели ip!')
#     for d in dell:
#         ip.remove(d)
#     return ip

# def ping_ip_addresses(ip_list):
#     ip=sort_ip(ip_list)
#     good=[]
#     bad=[]
#     for ip in ip_list:
#         result =subprocess.run(['ping', '-n', '1', ip], stdout=subprocess.DEVNULL, encoding="utf-8")
#         if result.returncode == 0:
#             good.append(ip+' {}'.format(str(check_ip(ip))))
#         else:
#             bad.append(ip+' {}'.format(str(check_ip(ip))))
#     return tuple(good), tuple(bad)

# def check_ip(ip):
#     ping_check=str(ping(ip, count=1))
#     if ping_check.startswith('Reply')==True:
#         return True
#     elif ping_check.startswith('Request')==True:
#         return False

# if __name__ == '__main__':
#     # print(ping(ip))
#     print('Пингующиеся ip-адреса:', ping_ip_addresses(ip)[0])
#     print('НЕ пингующиеся ip-адреса:', ping_ip_addresses(ip)[1])



# Задание 12.3
# Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

# Функция ожидает как аргументы два списка:
import subprocess
from tabulate import tabulate

ip=['1.1.1.1', '5.5.5.5', '8.8.8.2-6', '10.10.10.5-10.10.10.10']
def sort_ip(ip_list):
    ip=ip_list
    dell=[]
    for i in ip:
        if '-' in i:
            dell.append(i)
            i2=i.split('-')
            if '.' in i2[1]:
                if int(i2[0].split('.')[3])<int(i2[1].split('.')[3]):
                    for num in list(range(int(i2[0].split('.')[3]), int(i2[1].split('.')[3])+1)):
                        i2[0]=i2[0].replace('{}'.format(i2[0].split('.')[3]), str(num))
                        ip.append(i2[0])
                else:
                    print('ERROR!!! Не правильно ввели ip!')
            else:
                if i2[1].isdigit()==True:
                    if int(i2[0].split('.')[3])<int(i2[1]):
                        for num in list(range(int(i2[0].split('.')[3])-1, int(i2[1])+1)):
                            i2[0]=i2[0].replace('{}'.format(i2[0].split('.')[3]), str(num))
                            ip.append(i2[0])
                else:
                    print('ERROR!!! Не правильно ввели ip!')
    for d in dell:
        ip.remove(d)
    return ip

def print_ip_table(ip_list):
    ip=sort_ip(ip_list)
    good=[]
    bad=[]
    for ip in ip_list:
        result =subprocess.run(['ping', '-n', '1', ip], stdout=subprocess.DEVNULL, encoding="utf-8")
        if result.returncode == 0:
            good.append(ip)
        else:
            bad.append(ip)
    all_ip={"Reachable": good, "Unreachable": bad}
    result=tabulate(all_ip, headers='keys')
    return result

if __name__ == '__main__':
    print(print_ip_table(ip))