"""Задание 11.1
Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show cdp neighbors."""


# def parse_cdp_neighbors(command_output):
#     result2 = []
#     f=command_output.split('\n')
#     a=0
#     for test in f:
#         a+=1
#         if test=='':
#             f.pop(a-1)
#     a=0
#     main=f[0].split('>')[0]
#     for line in f:
#         if line!='':

#             a+=1
#             if line.startswith('Device')==True:
#                 device=int(a)
#                 while len(f)!=device:
#                     line=f[device].split()
#                     tuple1=(main, line[1]+line[2])
#                     tuple2=(line[0], line[-1]+line[-2])
#                     result={tuple1: tuple2}
#                     device+=1
#                     result2.append(result)
#     return result2
#     """
#     Тут мы передаем вывод команды одной строкой потому что именно в таком виде
#     будет получен вывод команды с оборудования. Принимая как аргумент вывод
#     команды, вместо имени файла, мы делаем функцию более универсальной: она может
#     работать и с файлами и с выводом с оборудования.
#     Плюс учимся работать с таким выводом.
#     """
# if __name__ == "__main__":
#     with open("sh_cdp_n_sw1.txt") as f:
#         f=parse_cdp_neighbors(f.read())
#         for line in f:
#             print(line)
#     print("\n")
#     with open("sh_cdp_n_r3.txt") as f:
#         f=parse_cdp_neighbors(f.read())
#         for line in f:
#             print(line)

# """Задание 11.2
# Создать функцию create_network_map, которая обрабатывает вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.
# """
infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]

def parse_cdp_neighbors(command_output):
    f=command_output.split('\n')
    a=0
    result={}
    for test in f:
        a+=1
        if test=='':
            f.pop(a-1)
    a=0
    main=f[0].split('>')[0]
    for line in f:
        if line!='':

            a+=1
            if line.startswith('Device')==True:
                device=int(a)
                while len(f)!=device:
                    line=f[device].split()
                    tuple1=(main, line[1]+line[2])
                    tuple2=(line[0], line[-1]+line[-2])
                    result[tuple1]=tuple2
                    device+=1
    return result
#     """
#     Тут мы передаем вывод команды одной строкой потому что именно в таком виде
#     будет получен вывод команды с оборудования. Принимая как аргумент вывод
#     команды, вместо имени файла, мы делаем функцию более универсальной: она может
#     работать и с файлами и с выводом с оборудования.
#     Плюс учимся работать с таким выводом.
#     """
if __name__ == "__main__":
    for file in infiles:
        with open("{}".format(file)) as f: # Тут замена кода
            f=parse_cdp_neighbors(f.read())
            print(f)
        print("\n")


# """Задание 11.2
# Создать функцию create_network_map, которая обрабатывает вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию."""
# import draw_network_graph as dr

# infiles = [
#     "sh_cdp_n_sw1.txt",
#     "sh_cdp_n_r1.txt",
#     "sh_cdp_n_r2.txt",
#     "sh_cdp_n_r3.txt",
# ]

# def parse_cdp_neighbors(command_output):
#     f=command_output.split('\n')
#     a=0
#     result={}
#     for test in f:
#         a+=1
#         if test=='':
#             f.pop(a-1)
#     a=0
#     main=f[0].split('>')[0]
#     for line in f:
#         if line!='':

#             a+=1
#             if line.startswith('Device')==True:
#                 device=int(a)
#                 while len(f)!=device:
#                     line=f[device].split()
#                     tuple1=(main, line[1]+line[2])
#                     tuple2=(line[0], line[-1]+line[-2])
#                     result[tuple1]=tuple2
#                     device+=1
#     return result
#     """
#     Тут мы передаем вывод команды одной строкой потому что именно в таком виде
#     будет получен вывод команды с оборудования. Принимая как аргумент вывод
#     команды, вместо имени файла, мы делаем функцию более универсальной: она может
#     работать и с файлами и с выводом с оборудования.
#     Плюс учимся работать с таким выводом.
#     """
# if __name__ == "__main__":
#     for file in infiles:
#         with open("{}".format(file)) as f: # Тут замена кода
#             f=parse_cdp_neighbors(f.read())
#             dr.draw_topology(f, output_filename="topology")
#         print("\n")