# Задание 4.1
# Используя подготовленную строку nat, получить новую строку, в которой в имени интерфейса вместо FastEthernet написано GigabitEthernet. Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.


nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"

nat=nat.replace('FastEthernet', 'GigabitEthernet')
print(nat)

# Задание 4.2
# Преобразовать строку в переменной mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

mac = "AAAA:BBBB:CCCC"

mac=mac.replace(':', '.')
print(mac)

# Задание 4.3
# Записать итоговый список в переменную result. (именно эта переменная будет проверяться в тесте)

# Полученный список result вывести на стандартный поток вывода (stdout) с помощью print. Тут очень важный момент, что надо получить именно список (тип данных), а не, например, строку, которая похожа на показанный список.

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
command = config.split()
result = command[-1].split(',')
print(result)

# Задание 4.4
# Список vlans это список VLANов, собранных со всех устройств сети, поэтому в списке есть повторяющиеся номера VLAN.

# Из списка vlans нужно получить новый список уникальных номеров VLANов, отсортированный по возрастанию номеров. Для получения итогового списка нельзя удалять конкретные vlanы вручную.

# Записать итоговый список уникальных номеров VLANов в переменную result. (именно эта переменная будет проверяться в тесте)

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
vlans=set(vlans)
result=sorted(vlans)

print(result)

# Задание 4.5
# Из строк command1 и command2 получить список VLANов, которые есть и в команде command1 и в команде command2 (пересечение).

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
command1 = command1.split()
command2 = command2.split()
vlans1 = set(command1[-1].split(','))
vlans2 = set(command2[-1].split(','))
result = sorted(vlans1 & vlans2)
print(result)

# Задание 4.6
# Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route=ospf_route.split()
prefix = ospf_route[0]

ADMetric = ospf_route[1].replace('[', "")
ADMetric = ADMetric.replace(']', "")

NextHop = ospf_route[3].replace(',', "")

Lastupdate = ospf_route[4].replace(',', "")

Outbound=ospf_route[-1]

name = {
    'Prefix': prefix,
    'ADMetric': ADMetric,
    'Next-Hop': NextHop,
    'Last update' : Lastupdate,
    'Outbound Interface': Outbound
}
print(name)

print("Prefix:  ", prefix)
print("ADMetric:  ", ADMetric)
print("Next-Hop:  ", NextHop)
print("Last update:  ", Lastupdate)
print("Outbound Interface:  ", Outbound)


# Задание 4.7
# Преобразовать MAC-адрес в строке mac в двоичную строку такого вида: „101010101010101010111011101110111100110011001100“
mac = "AAAA:BBBB:CCCC"
mac=mac.replace(':', "")
result=bin(int(mac, 16))
print(result)

# Задание 4.8
# Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:

# первой строкой должны идти десятичные значения байтов
# второй строкой двоичные значения
# Вывод должен быть упорядочен также, как в примере:

# столбцами
# ширина столбца 10 символов (в двоичном формате надо добавить два пробела между столбцами для разделения октетов между собой)
ip = "192.168.3.1"
ip1, ip2, ip3, ip4 = ip.split(".")
ip1=int(ip1)
ip2=int(ip2)
ip3=int(ip3)
ip4=int(ip4)
print("{:08} {:08} {:08} {:08}".format(ip1, ip2, ip3, ip4))
print("{:08b} {:08b} {:08b} {:08b}".format(ip1, ip2, ip3, ip4))