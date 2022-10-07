# Задание 7.1
# Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде на стандартный поток вывода:

# f=open('ospf.txt')
# text=['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

# for i in f.readlines():
#     print('\n'*2)

#     i=i.replace('via', '')
#     i=i.replace(',', '').split()
#     i.pop(0)
#     i[1]=i[1].strip('[]')
#     a=0
#     for t in text:
#         print("{:<20} {:<20}".format(t, i[a]))
#         a+=1


# Задание 7.2
# Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt. Имя файла передается как аргумент скрипту.

with open('config_sw1.txt', 'r') as f:
    for line in f:
        if not line.startswith('!'):
            print(line.rstrip())

# Задание 7.2a + 7.2b        
ignore = ["duplex", "alias", "configuration"]
w=open('text.txt', 'w')

with open('config_sw1.txt', 'r') as f:
    for line in f:
        if line.startswith('!')==False and line.startswith('')==True:
            if ignore[0] not in line and ignore[1] not in line and ignore[2] not in line:
                w.writelines(line+'\n'.rstrip())


# Задание 7.3 + 7.3(a)
# Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка, где есть MAC-адрес, должна быть обработана таким образом, чтобы на стандартный поток вывода была выведена таблица вида:
# f=open('CAM_table.txt', 'r+')
# a=[]
# result=[]

# for line in f.readlines():
#     line=line.split()
#     if line!=a:
#         if line[0].isdigit()==True:
#             line.remove('DYNAMIC')
#             line[0]=int(line[0])
#             vlan, mac, ports=line
#             result.append(line)
# result=sorted(result)
# for i in range(len(result)):
#     print("{:<18} {:<18} {:<18}".format(result[i][0], result[i][1], result[i][2]))

# Задание 7.3(b)
# vlan2=int(input('\nВведите номер vlan: '))
# f=open('CAM_table.txt', 'r+')
# a=[]
# result=[]

# for line in f.readlines():
#     line=line.split()
#     if line!=a:
#         if line[0].isdigit()==True:
#             line.remove('DYNAMIC')
#             line[0]=int(line[0])
#             vlan, mac, ports=line
#             result.append(line)
# for i in range(len(result)):
#     if result[i][0]==vlan2:
#         print("{:<18} {:<18} {:<18}".format(result[i][0], result[i][1], result[i][2]))