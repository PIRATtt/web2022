# Задание 6.1
# Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.

# Написать код, который преобразует MAC-адреса в формат cisco и добавляет их в новый список result. Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.


# mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
# mac2=[]
# for i in mac:
#     i=i.replace(':', '.')
#     i=i.upper()
#     mac2.append(i)
# print(mac2)


# Задание 6.2
# Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
# В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
# «unicast» - если первый байт в диапазоне 1-223
# «multicast» - если первый байт в диапазоне 224-239
# «local broadcast» - если IP-адрес равен 255.255.255.255
# «unassigned» - если IP-адрес равен 0.0.0.0
# «unused» - во всех остальных случаях

# ip=str(input("Введите ip-адрес в формате 10.0.1.1: "))
# while True:
#     if ip.count('.') == 3:
#         ip2=ip.split('.')
#         for i in ip2:
#             if i.isdigit()==True:
#                 i=int(i)
#                 if 0<=i<=255:
#                     if ip=='255.255.255.255':
#                         print('local broadcast')
#                     elif ip=='0.0.0.0':
#                         print('unassigned')
#                     elif ip.count('.') == 3:
#                         a=ip.split('.')[0]
#                         a=int(a)
#                         if 1<a<223:
#                             print('unicast')
#                         elif 224<a<239:
#                             print('multicast')
#                     else:
#                         print('unused')
#                 else:
#                     print('Неправильный IP-адрес')
#             else:
#                 print('Неправильный IP-адрес')
#     else:
#         print('Неправильный IP-адрес')
#         break


# 6.2a + 6.2b

ip=input("Введите ip-адрес в формате 10.0.1.1: ")
t=False
while t==False:
    if ip.count('.')!= 3:
        print('Неправильный IP-адрес - {}'.format(ip))
        ip=str(input("Введите ip-адрес ещё раз: "))
        t==True
    else:
        ip2=ip.split('.')
        sum_ip=ip2[0]+ip2[1]+ip2[2]+ip2[3]
        if sum_ip.isdigit()==False:
            print('Неправильный IP-адрес - {}'.format(ip))
            ip=str(input("Введите ip-адрес ещё раз: "))
            t==True
        else:
            if int(ip2[0])>255 or int(ip2[0])<0 or int(ip2[1])>255 or int(ip2[1])<0 or int(ip2[2])>255 or int(ip2[2])<0 or int(ip2[3])>255 or int(ip2[3])<0:
                print('Неправильный IP-адрес - {}'.format(ip))
                ip=str(input("Введите ip-адрес ещё раз: "))
                t==True
            else:
                if ip=='255.255.255.255':
                    print('local broadcast')
                    t==False
                    break
                elif ip=='0.0.0.0':
                    print('unassigned')
                    t==False
                    break
                elif ip.count('.') == 3:
                    a=ip.split('.')[0]
                    a=int(a)
                    if 1<a<223:
                        print('unicast')
                        t==False
                        break
                    elif 224<a<239:
                        print('multicast')
                        t==False
                        break
                else:
                    print('unused')
                    t==False
                    break


# Задание 6.3
# В скрипте сделан генератор конфигурации для access-портов. Сделать аналогичный генератор конфигурации для портов trunk.

# access_template = [
#     "switchport mode access",
#     "switchport access vlan",
#     "spanning-tree portfast",
#     "spanning-tree bpduguard enable",
# ]

# trunk_template = [
#     "switchport trunk encapsulation dot1q",
#     "switchport mode trunk",
#     "switchport trunk allowed vlan",
# ]

# access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
# trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}

# for intf, vlan in trunk.items():
#     print(f"interface FastEthernet {intf}")
#     for command in trunk_template:
#         if command.endswith("allowed vlan"):
#             if vlan[0]=='add':
#                 vlan.pop(0)
#                 vlan2=','.join(vlan)
#                 print(f" {command} add {vlan2}")
#             if vlan[0]=='only':
#                 vlan.pop(0)
#                 vlan2=','.join(vlan)
#                 print(f" {command} {vlan2}")
#             if vlan[0]=='del':
#                 vlan.pop(0)
#                 vlan2=','.join(vlan)
#                 print(f" {command} remove {vlan2}")
#         else:
#             print(f" {command}")