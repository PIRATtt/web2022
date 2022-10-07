# Задание 9.1
# Создать функцию, которая генерирует конфигурацию для access-портов.

# vlans={"FastEthernet0/12": 10,
#  "FastEthernet0/14": 11,
#  "FastEthernet0/16": 17}

# access_mode_template = [
#     'switchport mode access', 'switchport access vlan',
#     'switchport nonegotiate', 'spanning-tree portfast',
#     'spanning-tree bpduguard enable'
# ]

# access_config = {
#     'FastEthernet0/12': 10,
#     'FastEthernet0/14': 11,
#     'FastEthernet0/16': 17
# }

# access_config_2 = {
#     "FastEthernet0/03": 100,
#     "FastEthernet0/07": 101,
#     "FastEthernet0/09": 107
# }

# def generate_access_config(intf_vlan_mapping, access_template):
#     """
#     intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
#         {"FastEthernet0/12": 10,
#          "FastEthernet0/14": 11,
#          "FastEthernet0/16": 17}
#     access_template - список команд для порта в режиме access

#     Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
#     """
#     for p in access_template:
#         print('\n'*2)
#         print(p)
#         for i in intf_vlan_mapping:
#             i=str(i)
#             if i.endswith('access vlan')==True:
#                 print(i+' {}'.format(access_template[p]))
#             else:
#                 print(i)

# generate_access_config(access_mode_template, access_config)

# generate_access_config(access_mode_template, access_config_2)



# Задание 9.1a
# Сделать копию функции generate_access_config из задания 9.1.

# Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли настроен port-security:

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}
args=None
def generate_access_config(intf_vlan_mapping, access_template, *args):
    for p in access_template:
        print('\n'*2)
        print(p)
        for i in intf_vlan_mapping:
            i=str(i)
            if i.endswith('access vlan')==True:
                print(i+' {}'.format(access_template[p]))
            else:
                print(i)
    print('\n'*2)
    for a in args:
        for a2 in a:
            print(a2)

print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))



# Задание 9.2
# Создать функцию generate_trunk_config, которая генерирует конфигурацию для trunk-портов.

# У функции должны быть такие параметры:

# trunk_config = {
#     "FastEthernet0/1": [10, 20, 30],
#     "FastEthernet0/2": [11, 30],
#     "FastEthernet0/4": [17]
# }

# trunk_mode_template = [
#     "switchport mode trunk", "switchport trunk native vlan 999",
#     "switchport trunk allowed vlan"
# ]

# def trunk_convert(config, template):
#     for c in config:
#         print('interface '+c)
#         for t in template:
#             if str(t).endswith('allowed vlan')==True:
#                 print(t+' {}'.format(str(config[c]).strip('[]')))
#             else:
#                 print(t)

# trunk_convert(trunk_config, trunk_mode_template)



# Задание 9.2a
# Сделать копию функции generate_trunk_config из задания 9.2

# Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:

# ключи: имена интерфейсов, вида «FastEthernet0/1»

# значения: список команд, который надо выполнить на этом интерфейсе

# trunk_config = {
#     "FastEthernet0/1": [10, 20, 30],
#     "FastEthernet0/2": [11, 30],
#     "FastEthernet0/4": [17]
# }

# trunk_mode_template = [
#     "switchport mode trunk", "switchport trunk native vlan 999",
#     "switchport trunk allowed vlan"
# ]
# dict_simple={}
# def trunk_convert(config, template):
#     for c in config:
#         dict_simple['interface '+c]=0
#         l=[]
#         for t in template:
#             if str(t).endswith('allowed vlan')==True:
#                 l.append(t+' {}'.format(str(config[c]).strip('[]')))
#             else:
#                 l.append(t)
#         dict_simple['interface '+c]=l
#     return dict_simple
# trunk_convert(trunk_config, trunk_mode_template)
# print(dict_simple)



# Задание 9.3
# Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:

# access={}
# trunk={}
# all_lines=[] # Список со всеми строками без !
# def get_int_vlan_map(config_filename):
#     with open(config_filename, 'r+') as f:
#         for line in f:
#             if line.startswith('!')==False and line.startswith('')==True:
#                 all_lines.append(line.rstrip())
#         for i in all_lines:
#             i=str(i)
#             if i.startswith('interface Fast')==True:
#                 i2=all_lines.index(i)
#                 i=i.split()
#                 if all_lines[i2+1]==' switchport mode access':
#                     access[i[1]]=str(all_lines[i2+2]).split()[3]
#                 elif all_lines[i2+1]==' switchport trunk encapsulation dot1q':
#                     trunk[i[1]]=str(all_lines[i2+2]).split()[4]
#                 else:
#                     pass
#         tup=(access, trunk)                
#     return tup

# print(get_int_vlan_map('config_sw.txt'))



# Задание 9.3a
# Сделать копию функции get_int_vlan_map из задания 9.3.

# Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта выглядит так:

# access={}
# trunk={}
# all_lines=[] # Список со всеми строками без !
# def get_int_vlan_map(config_filename):
#     with open(config_filename, 'r+') as f:
#         for line in f:
#             if line.startswith('!')==False and line.startswith('')==True:
#                 all_lines.append(line.rstrip())
#         for i in all_lines:
#             i=str(i)
#             if i.startswith('interface Fast')==True:
#                 i2=all_lines.index(i)
#                 i=i.split()
#                 if all_lines[i2+1]==' switchport mode access':
#                     if all_lines[i2+2]==' duplex auto':
#                         access[i[1]]='порт в VLAN 1'
#                     else:
#                         access[i[1]]=str(all_lines[i2+2]).split()[3]
#                 elif all_lines[i2+1]==' switchport trunk encapsulation dot1q':
#                     trunk[i[1]]=str(all_lines[i2+2]).split()[4]
#                 else:
#                     pass
#         tup=(access, trunk)                
#     return tup

# print(get_int_vlan_map('config_sw2.txt'))



# Задание 9.4
# Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:

ignore = ["duplex", "alias", "Current configuration"]
result={}
all_lines=[] # Список со всеми строками без !
key=[]
def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status

def convert_config_to_dict(config_filename):
    with open(config_filename, 'r+') as f:
        for line in f:
            if line.startswith('!')==False and line.startswith('')==True:
                line=line.rstrip()
                if ignore_command(line, ignore)==False:
                    if line!='':
                        all_lines.append(line.rstrip())
                else:
                    pass
        id=0
        for line2 in all_lines:
            line2=str(line2)
            if line2.startswith(' ')==True:
                # while str(all_lines[id+1]).startswith(' ')==False:
                #     key=line2
                #     id=+1
                if str(all_lines[id-1]).startswith(' ')==False:
                    # key.append(line2)
                    result[all_lines[id-1]]=line2
                    wh_id=id+1
                    while str(all_lines[wh_id]).startswith(' ')==False:
                        key.append(wh_id-1)
                        wh_id=+1
                    else:
                        print('what')
                    print(key)
            else:
                result[line2]=''
            id=id+1
            print(id)
        print(result)   
    return result

convert_config_to_dict('config_sw.txt')

# def write_in_line(line, numb):
#     status=False


#     return status