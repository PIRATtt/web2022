# Задание 5.1
# В задании создан словарь, с информацией о разных устройствах.

# Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1). И вывести информацию о соответствующем устройстве на стандартный поток вывода (информация будет в виде словаря).

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
name=input('Введите имя: ')
print(london_co[name])

# Задание 5.1а
# Переделать скрипт из задания 5.1 таким образом, чтобы, кроме имени устройства, запрашивался также параметр устройства, который нужно отобразить.

# Вывести информацию о соответствующем параметре, указанного устройства.

keys = str(london_co[name].keys())
keys = keys.replace('dict_keys', "")
keys = keys.strip('([])')
keys = keys.replace("'", "")
print(keys)

print('Введите имя параметра (', keys, '): ')
parametr = input()
parametr = parametr.lower()

print(london_co[name].get(parametr, 'Параметра нет'))



# Задание №5.2
# Запросить у пользователя ввод IP-сети в формате:
ip=input('Введите ip-адрес в формате 10.1.1.0/24: ')
ip=ip.split('/')
ip_mask=ip[1]
ip_address=ip[0].split('.')
print(('{:>8} {:>8} {:>8} {:>8}').format(ip_address[0], ip_address[1], ip_address[2], ip_address[3]))
print(('{:>8b} {:>8b} {:>8b} {:>8b}').format(int(ip_address[0]), int(ip_address[1]), int(ip_address[2]), int(ip_address[3])))

print('Маска: ')
print('/'+ ip_mask)
a= 32 - int(ip_mask)
b=round(a/2)

mask = "1" * (32-b) + "0" * b
mask=str(mask)
end = str(int(mask[24:27])) + '0000'
print(('{:>8} {:>8} {:>8} {:>8}').format(int(mask[0:7]), int(mask[8:15]), int(mask[16:23]), int(end)))

# Задание 5.3
# Скрипт должен запрашивать у пользователя:

# информацию о режиме интерфейса (access/trunk)
# номере интерфейса (тип и номер, вида Gi0/3)
# номер VLANа (для режима trunk будет вводиться список VLANов)

access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

all={'access_template': access_template, 'trunk_template': trunk_template}
work=input('\n\nВведите режим работы интерфейса (access/trunk): ')
inter={'access':'Введите номер VLAN: ', 'trunk':'Введите разрешенные VLANы: '}
typ=input(inter[work])
vlan=input('Введите номер влан(ов): ')


work=work+'_template'

print('\n' + '-' * 30)
print ("\n\ninterface ", typ)
print('\n'.join(all[work]).format(vlan))
