#!/usr/bin/env python3

import os
print('@johanPosada')

def unitconv(opcion):
    switcher = {
        1: valor*1000,
        2: valor*100,
        3: valor*10,
        4: valor/10,
        5: valor/100,
        6: valor/100,
        7: valor/39.37,
        8: valor/10,
        9: valor/100,
        10: valor/1000,
        11: valor/10000,
        12: valor/100000,
        13: valor/1000000,
        14: valor/39370,
        15: valor*10,
        16: valor/10,
        17: valor/100,
        18: valor/1000,
        19: valor/10000,
        20: valor/100000,
        21: valor/3937,
        22: valor*100,
        23: valor*10,
        24: valor/10,
        25: valor/100,
        26: valor/1000,
        27: valor/10000,
        28: valor*394,
        29: valor*10000,
        30: valor*1000,
        31: valor*100,
        32: valor*10,
        33: valor/10,
        34: valor/100,
        35: valor/3.937,
        36: valor*100000,
        37: valor*10000,
        38: valor*1000,
        39: valor*100,
        40: valor*10,
        41: valor/10,
        42: valor*2.54,
        43: valor/0.0000010000,
        44: valor*100000,
        45: valor*10000,
        46: valor*1000,
        47: valor*100,
        48: valor*10,
        49: valor*25.4,
        50: valor*39370,
        51: valor*3937,
        52: valor*394,
        53: valor*39.37,
        54: valor*3.937,
        55: valor/2.54,
        56: valor/25.4
    }
    return switcher.get(opcion)

opciones = [(1, 'Km a m'), (2, 'Hm a m'), (3, 'Dm a m'), (4, 'dm a m'), (5, 'cm a m'), (6, 'mm a m'), (7, 'pulgadas a m'), 
            (8, 'Hm a Km'), (9, 'Dm a km'), (10, 'm a Km'), (11, 'dm a Km'), (12, 'cm a Km'), (13, 'mm a Km'), (14, 'pulgadas a Km'), 
            (15, 'Km a Hm'), (16, 'Dm a Hm'), (17, 'm a Hm'), (18, 'dm a Hm'), (19, 'cm a Hm'), (20, 'mm a Hm'), (21, 'pulgadas a Hm'), 
            (22, 'Km a Dm'), (23, 'Hm a Dm'), (24, 'm a Dm'), (25, 'dm a Dm'), (26, 'cm a Dm'), (27, 'mm a Dm'), (28, 'pulgadas a Dm'), 
            (29, 'Km a dm'), (30, 'Hm a dm'), (31, 'Dm a dm'), (32, 'm a dm'), (33, 'cm a dm'), (34, 'mm a dm'), 
            (35, 'pulgadas a dm'), (36, 'Km a cm'), (37, 'Hm a cm'), (38, 'Dm a cm'), (39, 'm a cm'), (40, 'dm a cm'), (41, 'mm a cm'), (42, 'pulgadas a cm'), 
            (43, 'Km a mm'), (44, 'Hm a mm'), (45, 'Dm a mm'), (46, 'm a mm'), (47, 'dm a mm'), (48, 'cm a mm'), (49, 'pulgadas a mm'),
            (50, 'Km a pulgadas'), (51, 'Hm a pulgadas'), (52, 'Dm a pulgadas'), (53, 'm a pulgadas'), (54, 'dm a pulgadas'), (55, 'cm a pulgadas'), (56, 'mm a pulgadas')
            ]

print('Elija el número de las opciones:\n','\nCovertir a m:\n', opciones[:7])
print('\nConvertir a Km:\n', opciones[7:14])
print('\nConvertir a Hm:\n', opciones[14:21])
print('\nConvertir a Dm:\n', opciones[21:28])
print('\nConvertir a dm:\n', opciones[28:35])
print('\nConvertir a cm:\n', opciones[35:42])
print('\nConvertir a mm:\n', opciones[42:49])
print('\nConvertir a pulgada:\n', opciones[49:56])

while True:
    try: 
        opcion = int(input('\nInserte la opción que desea: '))
    except ValueError:
        print('Debe ser entero o decimal')
        continue
    if opcion not in range(1, 57):
        print('Debe indicar una opción válida')
        continue
    else:
        print('Opción escogida:', opciones[opcion-1]) 
        break

while True:
    try:
        valor = int(input('\nInserte el valor a convertir, sin indicar unidades: '))
    except ValueError:
        print('Dede ser entero o decimal, no indique unidades')
    else:
        break

valorf = unitconv(opcion)
print(f"\nEl valor final es: {valorf}\n")

while True:
    try:
        exec_ = input('¿Quiere continuar? S/n ~ ')
    except ValueError:
        print('Deben ser carácteres')
        continue
    if exec_ == '':
        print('Inserte algo')
        continue
    else:
        break

if exec_ == 'S' or exec_ == 's':
    os.system('python3 ' + __file__)
else:
    print('Bye!')
