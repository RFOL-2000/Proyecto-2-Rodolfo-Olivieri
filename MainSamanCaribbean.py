from CruiseManagement import CruiseManagement #Importando
from CruiseManagement import Ship1, Ship2, Ship3, Ship4 #Importando
import requests #Importando
from RoomManagement import RoomManagment #Importando
from RoomManagement import Simple, Premium, Vip #Importando
import math  #Importando
from Registry import Registry #Importando
from TourSale import TourSale #Importando
from TourSale import Port, Tasting, Jogging, History #Importando
from RestaurantManagement import RestauranteManagement #Importando

url = "https://saman-caribbean.vercel.app/api/cruise-ships" #Url
a = requests.get(url) #metoodo get al url
data = a.json() #Convirtiendo en un json la data

def ships_info(): # Funcion para obtener la informacion de los barcos
    ship1_list = []
    ship2_list = []
    ship3_list = []
    ship4_list = []

    ship1 = Ship1(data[0]["name"], data[0]["route"], data[0]["departure"], data[0]["cost"], data[0]["rooms"], data[0]["capacity"])
    ship1_list.append(ship1)
    
    ship2 = Ship2(data[1]["name"], data[1]["route"], data[1]["departure"], data[1]["cost"], data[1]["rooms"], data[1]["capacity"])
    ship2_list.append(ship2)

    ship3 = Ship3(data[2]["name"], data[2]["route"], data[2]["departure"], data[2]["cost"], data[2]["rooms"], data[2]["capacity"])
    ship3_list.append(ship3)

    ship4 = Ship4(data[3]["name"], data[3]["route"], data[3]["departure"], data[3]["cost"], data[3]["rooms"], data[3]["capacity"])
    ship4_list.append(ship4)

    for ship in ship1_list: # Arreglando el print 
        print("Nombre : ",ship.ship_name)
        print("Ruta : ",ship.ship_route)
        print("Fecha de salida : ",ship.departure_date)
        print("Costo del boleto por tipo de habitacion : ",ship.ticket_cost)
        print("Cantidad de habitaciones y pasillos por piso : ",ship.rooms_and_corridors)
        print("Capacidad por tipo de habitacion : ",ship.room_capacity)
        print("\n")

    for ship in ship2_list: # Arreglando el print 
        print("Nombre : ",ship.ship_name)
        print("Ruta : ",ship.ship_route)
        print("Fecha de salida : ",ship.departure_date)
        print("Costo del boleto por tipo de habitacion : ",ship.ticket_cost)
        print("Cantidad de habitaciones y pasillos por piso : ",ship.rooms_and_corridors)
        print("Capacidad por tipo de habitacion : ",ship.room_capacity)
        print("\n")

    for ship in ship3_list: # Arreglando el print 
        print("Nombre : ",ship.ship_name)
        print("Ruta : ",ship.ship_route)
        print("Fecha de salida : ",ship.departure_date)
        print("Costo del boleto por tipo de habitacion : ",ship.ticket_cost)
        print("Cantidad de habitaciones y pasillos por piso : ",ship.rooms_and_corridors)
        print("Capacidad por tipo de habitacion : ",ship.room_capacity)
        print("\n")

    for ship in ship4_list: # Arreglando el print 
        print("Nombre : ",ship.ship_name)
        print("Ruta : ",ship.ship_route)
        print("Fecha de salida : ",ship.departure_date)
        print("Costo del boleto por tipo de habitacion : ",ship.ticket_cost)
        print("Cantidad de habitaciones y pasillos por piso : ",ship.rooms_and_corridors)
        print("Capacidad por tipo de habitacion : ",ship.room_capacity)
        print("\n")

ship1_simple_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range (4):
    ship1_simple_matrix.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

ship1_premium_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(3):
    ship1_premium_matrix.append([1, 2, 3, 4, 5, 6, 7, 8, 9])

ship1_vip_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(1):
    ship1_vip_matrix.append([1, 2, 3, 4, 5, 6])

ship2_simple_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(6):
    ship2_simple_matrix.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

ship2_premium_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(4):
    ship2_premium_matrix.append([1, 2, 3, 4, 5, 6, 7, 8])

ship2_vip_matrix = [] # Generando las matrices para la representacion de cada piso       
for i in range(2):
    ship2_vip_matrix.append([1, 2, 3, 4])

ship3_simple_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(6):
    ship3_simple_matrix.append([1, 2, 3, 4, 5, 6, 7, 8])

ship3_premium_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(4):
    ship3_premium_matrix.append([1, 2, 3, 4, 5, 6])

ship3_vip_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(4):
    ship3_vip_matrix.append([1, 2])

ship4_simple_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(4):
    ship4_simple_matrix.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

ship4_premium_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(3):
    ship4_premium_matrix.append([1, 2, 3, 4, 5, 6, 7])

ship4_vip_matrix = [] # Generando las matrices para la representacion de cada piso
for i in range(2):
    ship4_vip_matrix.append([1, 2, 3, 4])

def check_prime(dni , c=2): #Funcion para validar si el dni es primo
    if dni % c == 0 and dni != 2: 
        return False
    elif c > dni / 2:  
        return True
    else:
        return check_prime(dni, c+1)

def check_abundate(dni): #Funcion para validar si el dni es abundante
    factores = [f for f in range(1, dni) if dni % f == 0]
    suma = sum(factores)
    return suma > dni

def check_dni(dni_selection): #Funcion para validar si el dni esta registrado para la venta de tours
    with open ("Dni.txt", "r") as f:
        for line in f:
            if dni_selection in line:
                return True

def ship_a_1(): # Funcion del barco 
    hall_letter = ""
    print(f"""
    {ship1_simple_matrix[0]}\n
    {ship1_simple_matrix[1]}\n
    {ship1_simple_matrix[2]}\n
    {ship1_simple_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship1_simple_matrix[target_a][target_b] = 0
    print(f"""
    {ship1_simple_matrix[0]}\n
    {ship1_simple_matrix[1]}\n
    {ship1_simple_matrix[2]}\n
    {ship1_simple_matrix[3]}\n
    """)
    person_list1 = []
    person1 = Simple(hall_letter, room_number, 2, "Si puede tener servicio a la habitación")
    person_list1.append(person1)
    for i in person_list1:
        person1.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list1

def ship_a_1_register(): # Funcion del barco 
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list1 = []
    person_info1 = Registry(name, dni, age, discapacity)
    person_info_list1.append(person_info1)

    for i in person_info_list1:
        person_info1.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list1

    

    price_a_1 = 69.99
    normal_price_a_1 = 69.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_1 = price_a_1
    elif check_prime(dni) == True:
        price_a_1 = price_a_1 - (normal_price_a_1 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_1 = price_a_1
    elif check_abundate(dni) == True:
        price_a_1 = price_a_1 - (normal_price_a_1 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if age > 65:
        question = int(input(("Ha obtenido la opcion de un upgrade para una habitacion premium. (1) si desea obtenerlo, (2) si lo rechaza : ")))

        if question == 1:
            ship_a_2()
        elif question == 2:
            print("El upgrade no ha sido aceptado")

    if discapacity == "Si":
        price_a_1 = price_a_1 - (normal_price_a_1 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_1 < normal_price_a_1:
        final1 = price_a_1
    elif price_a_1 == normal_price_a_1:
        final1 = normal_price_a_1
    else:
        print("Invalido")
        sell_room()
    tax1 = (final1 * 0.16)

    total1 = (final1 + tax1)
    ticket_tours.append(total1)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_1}
Monto con descuento si aplica : {price_a_1}
Impuesto : {tax1}
Total : {total1}
""")
    sell_room()

def ship_a_2(): # Funcion del barco 
    hall_letter = ""
    print(f"""
    {ship1_premium_matrix[0]}\n
    {ship1_premium_matrix[1]}\n
    {ship1_premium_matrix[2]}\n
    {ship1_premium_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship1_premium_matrix[target_a][target_b] = 0
    print(f"""
    {ship1_premium_matrix[0]}\n
    {ship1_premium_matrix[1]}\n
    {ship1_premium_matrix[2]}\n
    {ship1_premium_matrix[3]}\n
    """)
    person_list2 = []
    person2 = Simple(hall_letter, room_number, 4, "Si puede tener servicio a la habitación")
    person_list2.append(person2)
    for i in person_list2:
        person2.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list2

def ship_a_2_register(): # Funcion del barco 
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list2 = []
    person_info2 = Registry(name, dni, age, discapacity)
    person_info_list2.append(person_info2)

    for i in person_info_list2:
        person_info2.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list2

    price_a_2 = 89.99
    normal_price_a_2 = 89.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_2 = price_a_2
    elif check_prime(dni) == True:
        price_a_2 = price_a_2 - (normal_price_a_2 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_2 = price_a_2
    elif check_abundate(dni) == True:
        price_a_2 = price_a_2 - (normal_price_a_2 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_2 = price_a_2 - (normal_price_a_2 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_2 < normal_price_a_2:
        final2 = price_a_2
    elif price_a_2 == normal_price_a_2:
        final2 = normal_price_a_2
    else:
        print("Invalido")
        sell_room()
    tax2 = (final2 * 0.16)

    total2 = (final2 + tax2)
    ticket_tours.append(total2)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_2}
Monto con descuento si aplica : {price_a_2}
Impuesto : {tax2}
Total : {total2}
""")
    sell_room()

def ship_a_3(): # Funcion del barco 
    hall_letter = ""
    print(f"""
    {ship1_vip_matrix[0]}\n
    {ship1_vip_matrix[1]}\n
    {ship1_vip_matrix[2]}\n
    {ship1_vip_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship1_vip_matrix[target_a][target_b] = 0
    print(f"""
    {ship1_vip_matrix[0]}\n
    {ship1_vip_matrix[1]}\n
    {ship1_vip_matrix[2]}\n
    {ship1_vip_matrix[3]}\n
    """)
    person_list3 = []
    person3 = Simple(hall_letter, room_number, 8, "Si puede tener servicio a la habitación")
    person_list3.append(person3)
    for i in person_list3:
        person3.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list3

def ship_a_3_register(): # Funcion del barco 
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list3 = []
    person_info3 = Registry(name, dni, age, discapacity)
    person_info_list3.append(person_info3)

    for i in person_info_list3:
        person_info3.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list3

    price_a_3 = 129.99
    normal_price_a_3 = 129.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_3 = price_a_3
    elif check_prime(dni) == True:
        price_a_3 = price_a_3 - (normal_price_a_3 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_3 = price_a_3
    elif check_abundate(dni) == True:
        price_a_3 = price_a_3 - (normal_price_a_3 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_3 = price_a_3 - (normal_price_a_3 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_3 < normal_price_a_3:
        final3 = price_a_3
    elif price_a_3 == normal_price_a_3:
        final3 = normal_price_a_3
    else:
        print("Invalido")
        sell_room()
    tax3 = (final3 * 0.16)

    total3 = (final3 + tax3)
    ticket_tours.append(total3)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_3}
Monto con descuento si aplica : {price_a_3}
Impuesto : {tax3}
Total : {total3}
""")
    sell_room()

def ship_b_1(): # Funcion del barco
    hall_letter = ""
    print(f"""
    {ship2_simple_matrix[0]}\n
    {ship2_simple_matrix[1]}\n
    {ship2_simple_matrix[2]}\n
    {ship2_simple_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship2_simple_matrix[target_a][target_b] = 0
    print(f"""
    {ship2_simple_matrix[0]}\n
    {ship2_simple_matrix[1]}\n
    {ship2_simple_matrix[2]}\n
    {ship2_simple_matrix[3]}\n
    """)
    person_list4 = []
    person4 = Simple(hall_letter, room_number, 2, "Si puede tener servicio a la habitación")
    person_list4.append(person4)
    for i in person_list4:
        person4.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list4

def ship_b_1_register(): # Funcion del barco 
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list4 = []
    person_info4 = Registry(name, dni, age, discapacity)
    person_info_list4.append(person_info4)

    for i in person_info_list4:
        person_info4.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list4

    price_a_4 = 59.99
    normal_price_a_4 = 59.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_4 = price_a_4
    elif check_prime(dni) == True:
        price_a_4 = price_a_4 - (normal_price_a_4 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_4 = price_a_4
    elif check_abundate(dni) == True:
        price_a_4 = price_a_4 - (normal_price_a_4 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_4 = price_a_4 - (normal_price_a_4 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_4 < normal_price_a_4:
        final4 = price_a_4
    elif price_a_4 == normal_price_a_4:
        final4 = normal_price_a_4
    else:
        print("Invalido")
        sell_room()
    tax4 = (final4 * 0.16)

    total4 = (final4 + tax4)
    ticket_tours.append(total4)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_4}
Monto con descuento si aplica : {price_a_4}
Impuesto : {tax4}
Total : {total4}
""")
    sell_room()

def ship_b_2(): # Funcion del barco
    hall_letter = ""
    print(f"""
    {ship2_premium_matrix[0]}\n
    {ship2_premium_matrix[1]}\n
    {ship2_premium_matrix[2]}\n
    {ship2_premium_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship2_premium_matrix[target_a][target_b] = 0
    print(f"""
    {ship2_premium_matrix[0]}\n
    {ship2_premium_matrix[1]}\n
    {ship2_premium_matrix[2]}\n
    {ship2_premium_matrix[3]}\n
    """)
    person_list5 = []
    person5 = Simple(hall_letter, room_number, 4, "Si puede tener servicio a la habitación")
    person_list5.append(person5)
    for i in person_list5:
        person5.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list5

def ship_b_2_register(): # Funcion del barco
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list5 = []
    person_info5 = Registry(name, dni, age, discapacity)
    person_info_list5.append(person_info5)

    for i in person_info_list5:
        person_info5.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list5

    price_a_5 = 99.99
    normal_price_a_5 = 99.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_5 = price_a_5
    elif check_prime(dni) == True:
        price_a_5 = price_a_5 - (normal_price_a_5 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_5 = price_a_5
    elif check_abundate(dni) == True:
        price_a_5 = price_a_5 - (normal_price_a_5 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_5 = price_a_5 - (normal_price_a_5 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_5 < normal_price_a_5:
        final5 = price_a_5
    elif price_a_5 == normal_price_a_5:
        final5 = normal_price_a_5
    else:
        print("Invalido")
        sell_room()
    tax5 = (final5 * 0.16)

    total5 = (final5 + tax5)
    ticket_tours.append(total5)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_5}
Monto con descuento si aplica : {price_a_5}
Impuesto : {tax5}
Total : {total5}
""")
    sell_room()

def ship_b_3(): # Funcion del barco
    hall_letter = ""
    print(f"""
    {ship2_vip_matrix[0]}\n
    {ship2_vip_matrix[1]}\n
    {ship2_vip_matrix[2]}\n
    {ship2_vip_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship2_vip_matrix[target_a][target_b] = 0
    print(f"""
    {ship2_vip_matrix[0]}\n
    {ship2_vip_matrix[1]}\n
    {ship2_vip_matrix[2]}\n
    {ship2_vip_matrix[3]}\n
    """)
    person_list6 = []
    person6 = Simple(hall_letter, room_number, 8, "Si puede tener servicio a la habitación")
    person_list6.append(person6)
    for i in person_list6:
        person6.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list6

def ship_b_3_register(): # Funcion del barco
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list6 = []
    person_info6 = Registry(name, dni, age, discapacity)
    person_info_list6.append(person_info6)

    for i in person_info_list6:
        person_info6.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list6

    price_a_6 = 119.99
    normal_price_a_6 = 119.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_6 = price_a_6
    elif check_prime(dni) == True:
        price_a_6 = price_a_6 - (normal_price_a_6 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_6 = price_a_6
    elif check_abundate(dni) == True:
        price_a_6 = price_a_6 - (normal_price_a_6 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_6 = price_a_6 - (normal_price_a_6 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_6 < normal_price_a_6:
        final6 = price_a_6
    elif price_a_6 == normal_price_a_6:
        final6 = normal_price_a_6
    else:
        print("Invalido")
        sell_room()
    tax6 = (final6 * 0.16)

    total6 = (final6 + tax6)
    ticket_tours.append(total6)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_6}
Monto con descuento si aplica : {price_a_6}
Impuesto : {tax6}
Total : {total6}
""")
    sell_room()

def ship_c_1(): # Funcion del barco
    hall_letter = ""
    print(f"""
    {ship3_simple_matrix[0]}\n
    {ship3_simple_matrix[1]}\n
    {ship3_simple_matrix[2]}\n
    {ship3_simple_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship3_simple_matrix[target_a][target_b] = 0
    print(f"""
    {ship3_simple_matrix[0]}\n
    {ship3_simple_matrix[1]}\n
    {ship3_simple_matrix[2]}\n
    {ship3_simple_matrix[3]}\n
    """)
    person_list7 = []
    person7 = Simple(hall_letter, room_number, 3, "Si puede tener servicio a la habitación")
    person_list7.append(person7)
    for i in person_list7:
        person7.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list7

def ship_c_1_register(): # Funcion del barco
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list7 = []
    person_info7 = Registry(name, dni, age, discapacity)
    person_info_list7.append(person_info7)

    for i in person_info_list7:
        person_info7.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list7

    price_a_7 = 49.99
    normal_price_a_7 = 49.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_7 = price_a_7
    elif check_prime(dni) == True:
        price_a_7 = price_a_7 - (normal_price_a_7 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_7 = price_a_7
    elif check_abundate(dni) == True:
        price_a_7= price_a_7 - (normal_price_a_7 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_7 = price_a_7 - (normal_price_a_7 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_7 < normal_price_a_7:
        final7 = price_a_7
    elif price_a_7 == normal_price_a_7:
        final7 = normal_price_a_7
    else:
        print("Invalido")
        sell_room()
    tax7 = (final7 * 0.16)

    total7 = (final7 + tax7)
    ticket_tours.append(total7)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_7}
Monto con descuento si aplica : {price_a_7}
Impuesto : {tax7}
Total : {total7}
""")
    sell_room()

def ship_c_2(): # Funcion del barco
    hall_letter = ""
    print(f"""
    {ship3_premium_matrix[0]}\n
    {ship3_premium_matrix[1]}\n
    {ship3_premium_matrix[2]}\n
    {ship3_premium_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship3_premium_matrix[target_a][target_b] = 0
    print(f"""
    {ship3_premium_matrix[0]}\n
    {ship3_premium_matrix[1]}\n
    {ship3_premium_matrix[2]}\n
    {ship3_premium_matrix[3]}\n
    """)
    person_list8 = []
    person8 = Simple(hall_letter, room_number, 5, "Si puede tener servicio a la habitación")
    person_list8.append(person8)
    for i in person_list8:
        person8.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list8

def ship_c_2_register(): # Funcion del barco
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list8 = []
    person_info8 = Registry(name, dni, age, discapacity)
    person_info_list8.append(person_info8)

    for i in person_info_list8:
        person_info8.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list8

    price_a_8 = 89.99
    normal_price_a_8 = 89.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_8 = price_a_8
    elif check_prime(dni) == True:
        price_a_8 = price_a_8 - (normal_price_a_8 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_8 = price_a_8
    elif check_abundate(dni) == True:
        price_a_8= price_a_8 - (normal_price_a_8 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_8 = price_a_8 - (normal_price_a_8 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_8 < normal_price_a_8:
        final8 = price_a_8
    elif price_a_8 == normal_price_a_8:
        final8 = normal_price_a_8
    else:
        print("Invalido")
        sell_room()
    tax8 = (final8 * 0.16)

    total8 = (final8 + tax8)
    ticket_tours.append(total8)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_8}
Monto con descuento si aplica : {price_a_8}
Impuesto : {tax8}
Total : {total8}
""")
    sell_room()

def ship_c_3(): # Funcion del barco
    hall_letter = ""
    print(f"""
    {ship3_vip_matrix[0]}\n
    {ship3_vip_matrix[1]}\n
    {ship3_vip_matrix[2]}\n
    {ship3_vip_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship3_vip_matrix[target_a][target_b] = 0
    print(f"""
    {ship3_vip_matrix[0]}\n
    {ship3_vip_matrix[1]}\n
    {ship3_vip_matrix[2]}\n
    {ship3_vip_matrix[3]}\n
    """)
    person_list9 = []
    person9 = Simple(hall_letter, room_number, 12, "Si puede tener servicio a la habitación")
    person_list9.append(person9)
    for i in person_list9:
        person9.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list9

def ship_c_3_register(): # Funcion del barco
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list9 = []
    person_info9 = Registry(name, dni, age, discapacity)
    person_info_list9.append(person_info9)

    for i in person_info_list9:
        person_info9.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list9

    price_a_9 = 139.99
    normal_price_a_9 = 139.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_9 = price_a_9
    elif check_prime(dni) == True:
        price_a_9 = price_a_9 - (normal_price_a_9 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_9 = price_a_9
    elif check_abundate(dni) == True:
        price_a_9 = price_a_9 - (normal_price_a_9 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_9 = price_a_9 - (normal_price_a_9 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_9 < normal_price_a_9:
        final9 = price_a_9
    elif price_a_9 == normal_price_a_9:
        final9 = normal_price_a_9
    else:
        print("Invalido")
        sell_room()
    tax9 = (final9 * 0.16)

    total9 = (final9 + tax9)
    ticket_tours.append(total9)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_9}
Monto con descuento si aplica : {price_a_9}
Impuesto : {tax9}
Total : {total9}
""")
    sell_room()

def ship_d_1(): # Funcion del barco
    hall_letter = ""
    print(f"""
    {ship4_simple_matrix[0]}\n
    {ship4_simple_matrix[1]}\n
    {ship4_simple_matrix[2]}\n
    {ship4_simple_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship4_simple_matrix[target_a][target_b] = 0
    print(f"""
    {ship4_simple_matrix[0]}\n
    {ship4_simple_matrix[1]}\n
    {ship4_simple_matrix[2]}\n
    {ship4_simple_matrix[3]}\n
    """)
    person_list10 = []
    person10 = Simple(hall_letter, room_number, 3, "Si puede tener servicio a la habitación")
    person_list10.append(person10)
    for i in person_list10:
        person10.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list10

def ship_d_1_register(): # Funcion del barco
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list10 = []
    person_info10 = Registry(name, dni, age, discapacity)
    person_info_list10.append(person_info10)

    for i in person_info_list10:
        person_info10.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list10

    price_a_10 = 59.99
    normal_price_a_10 = 59.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_10 = price_a_10
    elif check_prime(dni) == True:
        price_a_10 = price_a_10 - (normal_price_a_10 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_10 = price_a_10
    elif check_abundate(dni) == True:
        price_a_10 = price_a_10 - (normal_price_a_10 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_10 = price_a_10 - (normal_price_a_10 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_10 < normal_price_a_10:
        final10 = price_a_10
    elif price_a_10 == normal_price_a_10:
        final10 = normal_price_a_10
    else:
        print("Invalido")
        sell_room()
    tax10 = (final10 * 0.16)

    total10 = (final10 + tax10)
    ticket_tours.append(total10)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_10}
Monto con descuento si aplica : {price_a_10}
Impuesto : {tax10}
Total : {total10}
""")
    sell_room()

def ship_d_2(): # Funcion del barco
    hall_letter = ""
    print(f"""
    {ship4_premium_matrix[0]}\n
    {ship4_premium_matrix[1]}\n
    {ship4_premium_matrix[2]}\n
    {ship4_premium_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship4_premium_matrix[target_a][target_b] = 0
    print(f"""
    {ship4_premium_matrix[0]}\n
    {ship4_premium_matrix[1]}\n
    {ship4_premium_matrix[2]}\n
    {ship4_premium_matrix[3]}\n
    """)
    person_list11 = []
    person11 = Simple(hall_letter, room_number, 5, "Si puede tener servicio a la habitación")
    person_list11.append(person11)
    for i in person_list11:
        person11.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list11

def ship_d_2_register(): # Funcion del barco
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    elif discapacity == 2:
        discapacity = "No"
    person_info_list11 = []
    person_info11 = Registry(name, dni, age, discapacity)
    person_info_list11.append(person_info11)

    for i in person_info_list11:
        person_info11.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list11

    price_a_11 = 99.99
    normal_price_a_11 = 99.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_11 = price_a_11
    elif check_prime(dni) == True:
        price_a_11 = price_a_11 - (normal_price_a_11 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_11 = price_a_11
    elif check_abundate(dni) == True:
        price_a_11 = price_a_11 - (normal_price_a_11 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_11 = price_a_11 - (normal_price_a_11 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")

    if price_a_11 < normal_price_a_11:
        final11 = price_a_11
    elif price_a_11 == normal_price_a_11:
        final11 = normal_price_a_11
    else:
        print("Invalido")
        sell_room()
    tax11 = (final11 * 0.16)

    total11 = (final11 + tax11)
    ticket_tours.append(total11)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_11}
Monto con descuento si aplica : {price_a_11}
Impuesto : {tax11}
Total : {total11}
""")
    sell_room()

def ship_d_3(): # Funcion del barco
    hall_letter = ""
    print(f"""
    {ship4_vip_matrix[0]}\n
    {ship4_vip_matrix[1]}\n
    {ship4_vip_matrix[2]}\n
    {ship4_vip_matrix[3]}\n
    """)
    print("Que habitacion desea elegir? Tomando en cuanta que las representadas como 0 ya estan ocupadas")
    corridor = int(input("Indique que pasillo desea elegir desde el 1 hasta el 4 (Los pasillos son las columnas : "))
    room_number = int(input("Indique la habitacion que desea elegir desde el 1 hasta el 10 (las habitaciones son las filas) : "))
    if corridor == 1:
        hall_letter = "A"
    elif corridor == 2:
        hall_letter = "B"
    elif corridor == 3:
        hall_letter = "C"
    elif corridor == 4:
        hall_letter = "D"
    else:
        print("Invalido")
        sell_room()
    target_a = corridor - 1
    target_b = room_number - 1
    ship4_vip_matrix[target_a][target_b] = 0
    print(f"""
    {ship4_vip_matrix[0]}\n
    {ship4_vip_matrix[1]}\n
    {ship4_vip_matrix[2]}\n
    {ship4_vip_matrix[3]}\n
    """)
    person_list12 = []
    person12 = Simple(hall_letter, room_number, 10, "Si puede tener servicio a la habitación")
    person_list12.append(person12)
    for i in person_list12:
        person12.see_room()  
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f"""Habitacion : {i.hall_letter}{i.room_number} \n """)
    del person_list12

def ship_d_3_register(): # Funcion del barco
    name = input("Introduzca su nombre : ")
    dni = int(input("Introduzca su dni : "))
    age = int(input("Introduzca su edad : "))
    discapacity = int(input("Introduza (1) si tiene discapacidad (2) si no tiene : "))
    if discapacity == 1:
        discapacity = "Si"
    if discapacity == 2:
        discapacity = "No"
    person_info_list12 = []
    person_info12 = Registry(name, dni, age, discapacity)
    person_info_list12.append(person_info12)

    for i in person_info_list12:
        person_info12.see_info()
        with open ("SuperMegaArchivo.txt", "a") as a:
            a.write(f""" Nombre : {i.name}. """)
            a.write(str(f"""Dni : {i.dni}  """))
            a.write(str(f""" Edad : {i.age}  """))
            a.write(f""" Discapacidad : {i.discapacity} \n""")
        with open ("Dni.txt", "a") as a:
            a.write(str(f"""{i.dni}\n"""))
    del person_info_list12

    price_a_12 = 119.99
    normal_price_a_12 = 119.99

    check_prime(dni)

    if check_prime(dni) == False:
        price_a_12 = price_a_12
    if check_prime(dni) == True:
        price_a_12 = price_a_12 - (normal_price_a_12 * 0.10)
        print("Ha obtenido un descuento de 10% por ser primo su dni")

    check_abundate(dni)

    if check_abundate(dni) == False:
        price_a_12 = price_a_12
    if check_abundate(dni) == True:
        price_a_12 = price_a_12 - (normal_price_a_12 * 0.15)
        print("Ha obtenido un descuento de 15% por ser abundante su dni")

    if discapacity == "Si":
        price_a_12 = price_a_12 - (normal_price_a_12 * 0.30)
        print("Ha obtenido un descuento de 30% por tener una discapacidad")
        sell_room()
    if price_a_12 < normal_price_a_12:
        final12 = price_a_12
    if price_a_12 == normal_price_a_12:
        final12 = normal_price_a_12
    else:
        print("Invalido")
        sell_room()
    tax12 = (final12 * 0.16)

    total12 = (final12 + tax12)
    ticket_tours.append(total12)
    print(f"""
FACTURA 
Nombre : {name}
Dni : {dni}
Edad : {age}
Discapacidad : {discapacity}
Monto : {normal_price_a_12}
Monto con descuento si aplica : {price_a_12}
Impuesto : {tax12}
Total : {total12}
""")

def tour_sale(): # Funcion para vender el tour
    dni_selection = str(input("""
Dni: """))

    check_dni(dni_selection)
    if check_dni(dni_selection) == True:
        no_tour.append(1)
        answer_tour = int(input("""
Seleccione el numero del tour
Que tour desea elegir: 
1. Tour en el puerto (Max 4 personas)
2. Degustación de comida local (Max 2 personas)
3. Trotar por el pueblo/ciudad (Ilimtado)
4. Visita a lugares históricos (Max 4 personas)
--> """))
        persons = int(input("""
Seleccione el numero del tour
Cantidad de personas: 
--> """))
        if answer_tour == 1 and persons == 1:
            ticket_tours.append(30)
            tour_list_1 = []
            person1 = Port(30, 4, "12 PM", 10)
            if len(tour_list_1) < 10:
                for i in tour_list_1:
                    tour_list_1.append(person1)
                    person1.see_tour1()
            if len(tour_list_1) > 10:
                print("Cupo del tour lleno")

        if answer_tour == 1 and persons == 2:
            ticket_tours.append(30)
            tour_list_1 = []
            person1 = Port(30, 4, "12 PM", 10)
            if len(tour_list_1) < 10:
                for i in tour_list_1:
                    tour_list_1.append(person1)
                    person1.see_tour1()
            if len(tour_list_1) > 10:
                print("Cupo del tour lleno")
        
        if answer_tour == 1 and persons == 3:
            ticket_tours.append(30)
            tour_list_1 = []
            person1 = Port(30, 4, "12 PM", 10)
            if len(tour_list_1) < 10:
                price = (price) - (price * 0.10)
                for i in tour_list_1:
                    tour_list_1.append(person1)
                    person1.see_tour1()
            if len(tour_list_1) > 10:
                print("Cupo del tour lleno")

        if answer_tour == 1 and persons == 4:
            ticket_tours.append(30)
            tour_list_1 = []
            person1 = Port(30, 4, "12 PM", 10)
            if len(tour_list_1) < 10:
                price = (price) - (price * 0.20)
                for i in tour_list_1:
                    tour_list_1.append(person1)
                    person1.see_tour1()
            if len(tour_list_1) > 10:
                print("Cupo del tour lleno")

        if answer_tour == 2 and persons == 1:
            ticket_tours.append(100)
            tour_list_2 = []
            person2 = Tasting(100, 2, "12 PM", 100)
            if len(tour_list_2) < 100:
                for i in tour_list_2:
                    tour_list_2.append(person2)
                    person2.see_tour2()
            if len(tour_list_2) > 100:
                print("Cupo del tour lleno")

        if answer_tour == 2 and persons == 2:
            ticket_tours.append(100)
            tour_list_2 = []
            person2 = Tasting(100, 2, "12 PM", 100)
            if len(tour_list_2) < 100:
                for i in tour_list_2:
                    tour_list_2.append(person2)
                    person2.see_tour2()
            if len(tour_list_2) > 100:
                print("Cupo del tour lleno")

        if answer_tour == 3:
            tour_list_3 = []
            person3 = Jogging(0, "Ilimitado", "6 AM", "Ilimitado")
            for i in tour_list_3:
                tour_list_3.append(person3)
                person2.see_tour3()

        if answer_tour == 4 and persons == 1:
            ticket_tours.append(40)
            tour_list_4= []
            person4 = History(40, 4, "10 AM", 15)
            if len(tour_list_4) < 15:
                for i in tour_list_4:
                    tour_list_4.append(person4)
                    person4.see_tour4()
            if len(tour_list_4) > 15:
                print("Cupo del tour lleno")

        if answer_tour == 4 and persons == 2:
            ticket_tours.append(40)
            tour_list_4 = []
            person4 = History(40, 4, "10 AM", 15)
            if len(tour_list_4) < 15:
                for i in tour_list_4:
                    tour_list_4.append(person4)
                    person4.see_tour4()
            if len(tour_list_1) > 15:
                print("Cupo del tour lleno")
        
        if answer_tour == 4 and persons == 3:
            ticket_tours.append(40)
            tour_list_4 = []
            person4 = History(40, 4, "10 AM", 15)
            if len(tour_list_4) < 15:
                price = (price) - (price * 0.10)
                for i in tour_list_4:
                    tour_list_4.append(person4)
                    person4.see_tour4()
            if len(tour_list_1) > 15:
                print("Cupo del tour lleno")

        if answer_tour == 4 and persons == 4:
            ticket_tours.append(40)
            tour_list_4 = []
            person4 = History(40, 4, "10 AM", 15)
            if len(tour_list_4) < 15:
                price = (price) - (price * 0.20)
                for i in tour_list_4:
                    tour_list_4.append(person4)
                    person4.see_tour1()
            if len(tour_list_4) > 15:
                print("Cupo del tour lleno")

        else:
            print("Invalido")
            tour_sale()
    else:
        print("Invalido")
        tour_sale()

    sell_room()

def vacate_room(): # Funcion para desocupar habitacion
    vacate = int(input(f"""
En que barco se esta hospedando? : 
1.{name1}
2.{name2}
3.{name3}
4.{name4}
--> """))
    room = int(input(f"""
Que tipo de habitacion desea elegir : 
1. Simple
2. Premium 
3. Vip
--> """))
    if vacate == 1 and room == 1:
        print(f"""
{ship1_simple_matrix[0]}\n
{ship1_simple_matrix[1]}\n
{ship1_simple_matrix[2]}\n
{ship1_simple_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship1_simple_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship1_simple_matrix[0]}\n
{ship1_simple_matrix[1]}\n
{ship1_simple_matrix[2]}\n
{ship1_simple_matrix[3]}\n
    """)
    if vacate == 1 and room == 2:
        print(f"""
{ship1_premium_matrix[0]}\n
{ship1_premium_matrix[1]}\n
{ship1_premium_matrix[2]}\n
{ship1_premium_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship1_premium_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship1_premium_matrix[0]}\n
{ship1_premium_matrix[1]}\n
{ship1_premium_matrix[2]}\n
{ship1_premium_matrix[3]}\n
    """)
    if vacate == 1 and room == 3:
        print(f"""
{ship1_vip_matrix[0]}\n
{ship1_vip_matrix[1]}\n
{ship1_vip_matrix[2]}\n
{ship1_vip_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship1_vip_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship1_vip_matrix[0]}\n
{ship1_vip_matrix[1]}\n
{ship1_vip_matrix[2]}\n
{ship1_vip_matrix[3]}\n
    """)
    if vacate == 2 and room == 1:
        print(f"""
{ship2_simple_matrix[0]}\n
{ship2_simple_matrix[1]}\n
{ship2_simple_matrix[2]}\n
{ship2_simple_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship2_simple_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship2_simple_matrix[0]}\n
{ship2_simple_matrix[1]}\n
{ship2_simple_matrix[2]}\n
{ship2_simple_matrix[3]}\n
    """)
    if vacate == 2 and room == 2:
        print(f"""
{ship2_premium_matrix[0]}\n
{ship2_premium_matrix[1]}\n
{ship2_premium_matrix[2]}\n
{ship2_premium_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship2_premium_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship2_premium_matrix[0]}\n
{ship2_premium_matrix[1]}\n
{ship2_premium_matrix[2]}\n
{ship2_premium_matrix[3]}\n
    """)
    if vacate == 2 and room == 3:
        print(f"""
{ship2_vip_matrix[0]}\n
{ship2_vip_matrix[1]}\n
{ship2_vip_matrix[2]}\n
{ship2_vip_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship2_vip_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship2_vip_matrix[0]}\n
{ship2_vip_matrix[1]}\n
{ship2_vip_matrix[2]}\n
{ship2_vip_matrix[3]}\n
    """)
    if vacate == 3 and room == 1:
        print(f"""
{ship3_simple_matrix[0]}\n
{ship3_simple_matrix[1]}\n
{ship3_simple_matrix[2]}\n
{ship3_simple_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship3_simple_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship3_simple_matrix[0]}\n
{ship3_simple_matrix[1]}\n
{ship3_simple_matrix[2]}\n
{ship3_simple_matrix[3]}\n
    """)
    if vacate == 3 and room == 2:
        print(f"""
{ship3_premium_matrix[0]}\n
{ship3_premium_matrix[1]}\n
{ship3_premium_matrix[2]}\n
{ship3_premium_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship3_premium_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship3_premium_matrix[0]}\n
{ship3_premium_matrix[1]}\n
{ship3_premium_matrix[2]}\n
{ship3_premium_matrix[3]}\n
    """)
    if vacate == 3 and room == 3:
        print(f"""
{ship3_vip_matrix[0]}\n
{ship3_vip_matrix[1]}\n
{ship3_vip_matrix[2]}\n
{ship3_vip_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship3_vip_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship3_vip_matrix[0]}\n
{ship3_vip_matrix[1]}\n
{ship3_vip_matrix[2]}\n
{ship3_vip_matrix[3]}\n
    """)
    if vacate == 4 and room == 1:
        print(f"""
{ship4_simple_matrix[0]}\n
{ship4_simple_matrix[1]}\n
{ship4_simple_matrix[2]}\n
{ship4_simple_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship4_simple_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship4_simple_matrix[0]}\n
{ship4_simple_matrix[1]}\n
{ship4_simple_matrix[2]}\n
{ship4_simple_matrix[3]}\n
    """)
    if vacate == 4 and room == 2:
        print(f"""
{ship4_premium_matrix[0]}\n
{ship4_premium_matrix[1]}\n
{ship4_premium_matrix[2]}\n
{ship4_premium_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship4_premium_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship4_premium_matrix[0]}\n
{ship4_premium_matrix[1]}\n
{ship4_premium_matrix[2]}\n
{ship4_premium_matrix[3]}\n
    """)
    if vacate == 4 and room == 3:
        print(f"""
{ship4_vip_matrix[0]}\n
{ship4_vip_matrix[1]}\n
{ship4_vip_matrix[2]}\n
{ship4_vip_matrix[3]}\n
    """)
        z = int(input("Pasillo en el que se esta hospendando : "))
        x = int(input("Habitacion en la que se esta hospendando : "))
        vacate_target1 = (z - 1)
        vacate_target2 = (x - 1)
        ship4_vip_matrix[vacate_target1][vacate_target2] = x
        print(f"""
{ship4_vip_matrix[0]}\n
{ship4_vip_matrix[1]}\n
{ship4_vip_matrix[2]}\n
{ship4_vip_matrix[3]}\n
    """)
    else:
        print("Invalido")
        vacate_room()
    sell_room()

def menu(): # Funcion para la gestion del restaurante
    ship_choice_selection = int(input(f"""
Introduzca el numero 
En que barco se esta hospedando: 
1.{name1}
2.{name2}
3.{name3}
4.{name4}
--> """))

    if ship_choice_selection == 1:
        product1 = "Coca Cola"
        price1 = 3.99
        amount1 = 500
        product2 = "Pizza"
        price2 = 11.99
        amount2 = 230
        product3 = "Hamburguesa"
        price3 = 25.99
        amount3 = 250
        product4 = "Hamburguesa & Refresco"
        price4 = 19.99
        amount4 = 250
        product5 = "Ron"
        price5 = 6.99
        amount5 = 300
        
        menu_info1 = []
        menu_price1 = []

        menu1 = RestauranteManagement(product1, price1, amount1, product2, price2, amount2, product3, price3, amount3, product4, price4 , amount4, product5, price5, amount5)
        for i in menu_info1:
            menu1.see_menu1()
        del menu_info1
        
        while True:
            product_choice1 = int(input("Introduzca el numero del producto que va a escoger : "))
            if product_choice1 == 1:
                top_coca.append(1)
                size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                if size == 1:
                    menu_size = "Pequeño"
                if size == 2:
                    menu_size = "Mediano"
                if size == 3:
                    menu_size = "Grande"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product1)
                menu_info1.append(menu_size)
                menu_price1.append(price1)
                amount1 = amount1 - 1
                if amount1  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 2:
                top_pizza.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product2)
                menu_info1.append(menu_type)
                menu_price1.append(price2)
                amount2 = amount2 - 1
                if amount2  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 3:
                top_hamburguesa.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product3)
                menu_info1.append(menu_type)
                menu_price1.append(price3)
                amount3 = amount3 - 1
                if amount3  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 4:
                top_hambirguesa_refresco.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product4)
                menu_info1.append(menu_type)
                menu_price1.append(price4)
                amount4 = amount4 - 1
                if amount4  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 5:
                top_ron.append(1)
                size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                if size == 1:
                    menu_size = "Pequeño"
                if size == 2:
                    menu_size = "Mediano"
                if size == 3:
                    menu_size = "Grande"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product5)
                menu_info1.append(size)
                menu_price1.append(price5)
                amount5 = amount5 - 1
                if amount5  < 1:
                        print("No obtenemos mas de este producto")

            menu_question = int(input("Desea algo mas? (1) si (2) no : "))
            if menu_question == 1:
                return True
            if menu_question == 2:
                return False

        delete_product = int(input("Desea eliminar un producto en su pedido? (1) si (2) no : "))
        if delete_product == 1:
            product_position = int(input("Que producto desea eliminar? en que posicion se encuentra empezando desde el 1 : "))
            product_target = product_position - 1
            del menu_info1[product_target]
            del menu_price1[product_target]

        menu_price1_total = sum(menu_price1)
        menu_price1_total_iva = (menu_price1_total * 0.16)
        menu_price1_final = (menu_price1_total + menu_price1_total_iva)
        menu_factura = (f"""
FACTURA NORMAL
Pedido : {menu_info1}
Monto : {menu_price1_total}
Iva : {menu_price1_total_iva}
Monto Total : {menu_price1_final}
    """)
        print(menu_factura)

        combo_question = int(input("Desea agregar un combo? (1) si (2) no : "))
        menu_info1c = []
        menu_price1c = []
        if combo_question == 1:
            while True:
                combo_choice =  int(input("Numero del combio que desea agregar? : "))
                if combo_choice == 1:
                    top_coca.append(1)
                    size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                    if size == 1:
                        menu_size = "Pequeño"
                    if size == 2:
                        menu_size = "Mediano"
                    if size == 3:
                        menu_size = "Grande"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product1)
                    menu_info1c.append(menu_size)
                    menu_price1c.append(price1)
                    amount1 = amount1 - 1
                    if amount1  < 1:
                        print("No obtenemos mas de este producto")

                if combo_choice == 2:
                    top_pizza.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product2)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price2)
                    amount2 = amount2 - 1
                    if amount2  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 3:
                    top_hamburguesa.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product3)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price3)
                    amount3 = amount3 - 1
                    if amount3  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 4:
                    top_hambirguesa_refresco.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product4)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price4)
                    amount4 = amount4 - 1
                    if amount4  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 5:
                    top_ron.append(1)
                    size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                    if size == 1:
                        menu_size = "Pequeño"
                    if size == 2:
                        menu_size = "Mediano"
                    if size == 3:
                        menu_size = "Grande"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product5)
                    menu_info1c.append(size)
                    menu_price1c.append(price5)
                    amount1 = amount1 - 1
                    if amount5  < 1:
                        print("No obtenemos mas de este producto")
                        

                menu_questionc = int(input("Desea algo mas? (1) si (2) no : "))
                if menu_questionc == 1:
                    return True
                if menu_questionc == 2:
                    return False

            delete_combo = int(input("Desea eliminar un producto en su pedido? (1) si (2) no : "))
            if delete_combo == 1:
                product_positionc = int(input("Que producto desea eliminar? en que posicion se encuentra empezando desde el 1 : "))
                product_targetc = product_positionc - 1
            del menu_info1c[product_targetc]
            del menu_price1c[product_targetc]

            menu_price1_totalc = sum(menu_price1c)
            menu_price1_total_ivac = (menu_price1_totalc * 0.16)
            menu_price1_finalc = (menu_price1_totalc + menu_price1_total_ivac)
            menu_facturac = (f"""
FACTURA COMBO
Pedido : {menu_info1c}
Monto : {menu_price1_totalc}
Iva : {menu_price1_total_ivac}
Monto Total : {menu_price1_finalc}
    """)
            print(menu_facturac)

    if ship_choice_selection == 2:
        product1 = "Coca Cola"
        price1 = 5.99
        amount1 = 100
        product2 = "Pasta"
        price2 = 12.99
        amount2 = 150
        product3 = "Hamburguesa"
        price3 = 13.99
        amount3 = 230
        product4 = "Donas"
        price4 = 2.99
        amount4 = 250
        product5 = "Ron"
        price5 = 11.99
        amount5 = 250
        
        menu_info1 = []
        menu_price1 = []

        menu1 = RestauranteManagement(product1, price1, amount1, product2, price2, amount2, product3, price3, amount3, product4, price4 , amount4, product5, price5, amount5)
        for i in menu_info1:
            menu1.see_menu1()
        del menu_info1
        
        while True:
            product_choice1 = int(input("Introduzca el numero del producto que va a escoger : "))
            if product_choice1 == 1:
                top_coca.append(1)
                size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                if size == 1:
                    menu_size = "Pequeño"
                if size == 2:
                    menu_size = "Mediano"
                if size == 3:
                    menu_size = "Grande"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product1)
                menu_info1.append(menu_size)
                menu_price1.append(price1)
                amount1 = amount1 - 1
                if amount1  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 2:
                top_pasta.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product2)
                menu_info1.append(menu_type)
                menu_price1.append(price2)
                amount2 = amount2 - 1
                if amount2  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 3:
                top_hamburguesa.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product3)
                menu_info1.append(menu_type)
                menu_price1.append(price3)
                amount3 = amount3 - 1
                if amount3  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 4:
                top_donas.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product4)
                menu_info1.append(menu_type)
                menu_price1.append(price4)
                amount4 = amount4 - 1
                if amount4  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 5:
                top_ron.append(1)
                size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                if size == 1:
                    menu_size = "Pequeño"
                if size == 2:
                    menu_size = "Mediano"
                if size == 3:
                    menu_size = "Grande"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product5)
                menu_info1.append(size)
                menu_price1.append(price5)
                amount5 = amount5 - 1
                if amount5  < 1:
                        print("No obtenemos mas de este producto")

            menu_question = int(input("Desea algo mas? (1) si (2) no : "))
            if menu_question == 1:
                return True
            if menu_question == 2:
                return False

        delete_product = int(input("Desea eliminar un producto en su pedido? (1) si (2) no : "))
        if delete_product == 1:
            product_position = int(input("Que producto desea eliminar? en que posicion se encuentra empezando desde el 1 : "))
            product_target = product_position - 1
            del menu_info1[product_target]
            del menu_price1[product_target]

        menu_price1_total = sum(menu_price1)
        menu_price1_total_iva = (menu_price1_total * 0.16)
        menu_price1_final = (menu_price1_total + menu_price1_total_iva)
        menu_factura = (f"""
FACTURA NORMAL
Pedido : {menu_info1}
Monto : {menu_price1_total}
Iva : {menu_price1_total_iva}
Monto Total : {menu_price1_final}
    """)
        print(menu_factura)

        combo_question = int(input("Desea agregar un combo? (1) si (2) no : "))
        menu_info1c = []
        menu_price1c = []
        if combo_question == 1:
            while True:
                top_coca.append(1)
                combo_choice =  int(input("Numero del combio que desea agregar? : "))
                if combo_choice == 1:
                    size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                    if size == 1:
                        menu_size = "Pequeño"
                    if size == 2:
                        menu_size = "Mediano"
                    if size == 3:
                        menu_size = "Grande"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product1)
                    menu_info1c.append(menu_size)
                    menu_price1c.append(price1)
                    amount1 = amount1 - 1
                    if amount1  < 1:
                        print("No obtenemos mas de este producto")

                if combo_choice == 2:
                    top_pasta.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product2)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price2)
                    amount2 = amount2 - 1
                    if amount2  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 3:
                    top_hamburguesa.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product3)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price3)
                    amount3 = amount3 - 1
                    if amount3  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 4:
                    top_donas.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product4)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price4)
                    amount4 = amount4 - 1
                    if amount4  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 5:
                    top_ron.append(1)
                    size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                    if size == 1:
                        menu_size = "Pequeño"
                    if size == 2:
                        menu_size = "Mediano"
                    if size == 3:
                        menu_size = "Grande"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product5)
                    menu_info1c.append(size)
                    menu_price1c.append(price5)
                    amount1 = amount1 - 1
                    if amount5  < 1:
                        print("No obtenemos mas de este producto")
                        

                menu_questionc = int(input("Desea algo mas? (1) si (2) no : "))
                if menu_questionc == 1:
                    return True
                if menu_questionc == 2:
                    return False

            delete_combo = int(input("Desea eliminar un producto en su pedido? (1) si (2) no : "))
            if delete_combo == 1:
                product_positionc = int(input("Que producto desea eliminar? en que posicion se encuentra empezando desde el 1 : "))
                product_targetc = product_positionc - 1
            del menu_info1c[product_targetc]
            del menu_price1c[product_targetc]

            menu_price1_totalc = sum(menu_price1c)
            menu_price1_total_ivac = (menu_price1_totalc * 0.16)
            menu_price1_finalc = (menu_price1_totalc + menu_price1_total_ivac)
            menu_facturac = (f"""
FACTURA COMBO
Pedido : {menu_info1c}
Monto : {menu_price1_totalc}
Iva : {menu_price1_total_ivac}
Monto Total : {menu_price1_finalc}
    """)
            print(menu_facturac)

    if ship_choice_selection == 4:
        product1 = "Coca Cola"
        price1 = 5.99
        amount1 = 100
        product2 = "Pizza"
        price2 = 12.99
        amount2 = 130
        product3 = "Hamburguesa"
        price3 = 15.99
        amount3 = 260
        product4 = "Cotufa"
        price4 = 6.99
        amount4 = 150
        product5 = "Cofuta & Refresco"
        price5 = 12.99
        amount5 = 350
        
        menu_info1 = []
        menu_price1 = []

        menu1 = RestauranteManagement(product1, price1, amount1, product2, price2, amount2, product3, price3, amount3, product4, price4 , amount4, product5, price5, amount5)
        for i in menu_info1:
            menu1.see_menu1()
        del menu_info1
        
        while True:
            product_choice1 = int(input("Introduzca el numero del producto que va a escoger : "))
            if product_choice1 == 1:
                top_coca.append(1)
                size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                if size == 1:
                    menu_size = "Pequeño"
                if size == 2:
                    menu_size = "Mediano"
                if size == 3:
                    menu_size = "Grande"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product1)
                menu_info1.append(menu_size)
                menu_price1.append(price1)
                amount1 = amount1 - 1
                if amount1  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 2:
                top_pizza.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product2)
                menu_info1.append(menu_type)
                menu_price1.append(price2)
                amount2 = amount2 - 1
                if amount2  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 3:
                top_hamburguesa.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product3)
                menu_info1.append(menu_type)
                menu_price1.append(price3)
                amount3 = amount3 - 1
                if amount3  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 4:
                top_cotufa.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product4)
                menu_info1.append(menu_type)
                menu_price1.append(price4)
                amount4 = amount4 - 1
                if amount4  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 5:
                top_cotufas_refresco.append(1)
                size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                if size == 1:
                    menu_size = "Pequeño"
                if size == 2:
                    menu_size = "Mediano"
                if size == 3:
                    menu_size = "Grande"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product5)
                menu_info1.append(size)
                menu_price1.append(price5)
                amount5 = amount5 - 1
                if amount5  < 1:
                        print("No obtenemos mas de este producto")

            menu_question = int(input("Desea algo mas? (1) si (2) no : "))
            if menu_question == 1:
                return True
            if menu_question == 2:
                return False

        delete_product = int(input("Desea eliminar un producto en su pedido? (1) si (2) no : "))
        if delete_product == 1:
            product_position = int(input("Que producto desea eliminar? en que posicion se encuentra empezando desde el 1 : "))
            product_target = product_position - 1
            del menu_info1[product_target]
            del menu_price1[product_target]

        menu_price1_total = sum(menu_price1)
        menu_price1_total_iva = (menu_price1_total * 0.16)
        menu_price1_final = (menu_price1_total + menu_price1_total_iva)
        menu_factura = (f"""
FACTURA NORMAL
Pedido : {menu_info1}
Monto : {menu_price1_total}
Iva : {menu_price1_total_iva}
Monto Total : {menu_price1_final}
    """)
        print(menu_factura)

        combo_question = int(input("Desea agregar un combo? (1) si (2) no : "))
        menu_info1c = []
        menu_price1c = []
        if combo_question == 1:
            while True:
                combo_choice =  int(input("Numero del combio que desea agregar? : "))
                if combo_choice == 1:
                    top_coca.append(1)
                    size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                    if size == 1:
                        menu_size = "Pequeño"
                    if size == 2:
                        menu_size = "Mediano"
                    if size == 3:
                        menu_size = "Grande"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product1)
                    menu_info1c.append(menu_size)
                    menu_price1c.append(price1)
                    amount1 = amount1 - 1
                    if amount1  < 1:
                        print("No obtenemos mas de este producto")

                if combo_choice == 2:
                    top_pizza.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product2)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price2)
                    amount2 = amount2 - 1
                    if amount2  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 3:
                    top_hamburguesa.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product3)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price3)
                    amount3 = amount3 - 1
                    if amount3  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 4:
                    top_cotufa.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product4)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price4)
                    amount4 = amount4 - 1
                    if amount4  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 5:
                    top_cotufas_refresco.append(1)
                    size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                    if size == 1:
                        menu_size = "Pequeño"
                    if size == 2:
                        menu_size = "Mediano"
                    if size == 3:
                        menu_size = "Grande"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product5)
                    menu_info1c.append(size)
                    menu_price1c.append(price5)
                    amount1 = amount1 - 1
                    if amount5  < 1:
                        print("No obtenemos mas de este producto")
                        

                menu_questionc = int(input("Desea algo mas? (1) si (2) no : "))
                if menu_questionc == 1:
                    return True
                if menu_questionc == 2:
                    return False

            delete_combo = int(input("Desea eliminar un producto en su pedido? (1) si (2) no : "))
            if delete_combo == 1:
                product_positionc = int(input("Que producto desea eliminar? en que posicion se encuentra empezando desde el 1 : "))
                product_targetc = product_positionc - 1
            del menu_info1c[product_targetc]
            del menu_price1c[product_targetc]

            menu_price1_totalc = sum(menu_price1c)
            menu_price1_total_ivac = (menu_price1_totalc * 0.16)
            menu_price1_finalc = (menu_price1_totalc + menu_price1_total_ivac)
            menu_facturac = (f"""
FACTURA COMBO
Pedido : {menu_info1c}
Monto : {menu_price1_totalc}
Iva : {menu_price1_total_ivac}
Monto Total : {menu_price1_finalc}
    """)
            print(menu_facturac)

    if ship_choice_selection == 3:
        product1 = "Coca Cola"
        price1 = 2.99
        amount1 = 150
        product2 = "Pizza"
        price2 = 11.99
        amount2 = 200
        product3 = "Hamburguesa"
        price3 = 16.99
        amount3 = 200
        product4 = "Cerveza"
        price4 = 3.99
        amount4 = 180
        product5 = "Cofuta & Refresco"
        price5 = 11.99
        amount5 = 150
        
        menu_info1 = []
        menu_price1 = []

        menu1 = RestauranteManagement(product1, price1, amount1, product2, price2, amount2, product3, price3, amount3, product4, price4 , amount4, product5, price5, amount5)
        for i in menu_info1:
            menu1.see_menu1()
        del menu_info1
        
        while True:
            product_choice1 = int(input("Introduzca el numero del producto que va a escoger : "))
            if product_choice1 == 1:
                top_coca.append(1)
                size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                if size == 1:
                    menu_size = "Pequeño"
                if size == 2:
                    menu_size = "Mediano"
                if size == 3:
                    menu_size = "Grande"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product1)
                menu_info1.append(menu_size)
                menu_price1.append(price1)
                amount1 = amount1 - 1
                if amount1  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 2:
                top_pizza.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product2)
                menu_info1.append(menu_type)
                menu_price1.append(price2)
                amount2 = amount2 - 1
                if amount2  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 3:
                top_hamburguesa.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product3)
                menu_info1.append(menu_type)
                menu_price1.append(price3)
                amount3 = amount3 - 1
                if amount3  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 4:
                top_cerveza.append(1)
                product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                if product_type == 1:
                    menu_type = "Empaque"
                if product_type == 2:
                    menu_type = "Preparacion"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product4)
                menu_info1.append(menu_type)
                menu_price1.append(price4)
                amount4 = amount4 - 1
                if amount4  < 1:
                        print("No obtenemos mas de este producto")

            if product_choice1 == 5:
                top_cotufas_refresco.append(1)
                size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                if size == 1:
                    menu_size = "Pequeño"
                if size == 2:
                    menu_size = "Mediano"
                if size == 3:
                    menu_size = "Grande"
                else:
                        print("Invalido")
                        menu()
                menu_info1.append(product5)
                menu_info1.append(size)
                menu_price1.append(price5)
                amount5 = amount5 - 1
                if amount5  < 1:
                        print("No obtenemos mas de este producto")

            menu_question = int(input("Desea algo mas? (1) si (2) no : "))
            if menu_question == 1:
                return True
            if menu_question == 2:
                return False

        delete_product = int(input("Desea eliminar un producto en su pedido? (1) si (2) no : "))
        if delete_product == 1:
            product_position = int(input("Que producto desea eliminar? en que posicion se encuentra empezando desde el 1 : "))
            product_target = product_position - 1
            del menu_info1[product_target]
            del menu_price1[product_target]

        menu_price1_total = sum(menu_price1)
        menu_price1_total_iva = (menu_price1_total * 0.16)
        menu_price1_final = (menu_price1_total + menu_price1_total_iva)
        menu_factura = (f"""
FACTURA NORMAL
Pedido : {menu_info1}
Monto : {menu_price1_total}
Iva : {menu_price1_total_iva}
Monto Total : {menu_price1_final}
    """)
        print(menu_factura)

        combo_question = int(input("Desea agregar un combo? (1) si (2) no : "))
        menu_info1c = []
        menu_price1c = []
        if combo_question == 1:
            while True:
                top_coca.append(1)
                combo_choice =  int(input("Numero del combio que desea agregar? : "))
                if combo_choice == 1:
                    size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                    if size == 1:
                        menu_size = "Pequeño"
                    if size == 2:
                        menu_size = "Mediano"
                    if size == 3:
                        menu_size = "Grande"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product1)
                    menu_info1c.append(menu_size)
                    menu_price1c.append(price1)
                    amount1 = amount1 - 1
                    if amount1  < 1:
                        print("No obtenemos mas de este producto")

                if combo_choice == 2:
                    top_pizza.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product2)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price2)
                    amount2 = amount2 - 1
                    if amount2  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 3:
                    top_hamburguesa.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product3)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price3)
                    amount3 = amount3 - 1
                    if amount3  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 4:
                    top_cerveza.append(1)
                    product_type = int(input("Introduzca (1) Empaque (2) Preparacion : "))
                    if product_type == 1:
                        menu_type = "Empaque"
                    if product_type == 2:
                        menu_type = "Preparacion"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product4)
                    menu_info1c.append(menu_type)
                    menu_price1c.append(price4)
                    amount4 = amount4 - 1
                    if amount4  < 1:
                        print("No obtenemos mas de este producto")
                        
                if combo_choice == 5:
                    top_cotufas_refresco.append(1)
                    size = int(input("Introduzca el tamaño de la bebida (1) Pequeño (2) Mediano (3) Grande : "))
                    if size == 1:
                        menu_size = "Pequeño"
                    if size == 2:
                        menu_size = "Mediano"
                    if size == 3:
                        menu_size = "Grande"
                    else:
                        print("Invalido")
                        menu()
                    menu_info1c.append(product5)
                    menu_info1c.append(size)
                    menu_price1c.append(price5)
                    amount1 = amount1 - 1
                    if amount5  < 1:
                        print("No obtenemos mas de este producto")
                        

                menu_questionc = int(input("Desea algo mas? (1) si (2) no : "))
                if menu_questionc == 1:
                    return True
                if menu_questionc == 2:
                    return False
                else:
                    print("Invalido")
                    menu()

            delete_combo = int(input("Desea eliminar un producto en su pedido? (1) si (2) no : "))
            if delete_combo == 1:
                product_positionc = int(input("Que producto desea eliminar? en que posicion se encuentra empezando desde el 1 : "))
                product_targetc = product_positionc - 1
            del menu_info1c[product_targetc]
            del menu_price1c[product_targetc]
            
            menu_price1_totalc = sum(menu_price1c)
            menu_price1_total_ivac = (menu_price1_totalc * 0.16)
            menu_price1_finalc = (menu_price1_totalc + menu_price1_total_ivac)
            menu_facturac = (f"""
FACTURA COMBO
Pedido : {menu_info1c}
Monto : {menu_price1_totalc}
Iva : {menu_price1_total_ivac}
Monto Total : {menu_price1_finalc}
    """)
            print(menu_facturac)
    else:
        print("Invalido")
        menu()

    sell_room()

name1 = data[0]["name"]
name2 = data[1]["name"]
name3 = data[2]["name"]
name4 = data[3]["name"]

place1 = data[0]["route"]
place2 = data[1]["route"]
place3 = data[2]["route"]
place4 = data[3]["route"]

ticket_tours = []
no_tour = []

top_ship1 = []
top_ship2 = []
top_ship3 = []
top_ship4 = []
n_ship1 = len(top_ship1)
n_ship2 = len(top_ship2)
n_ship3 = len(top_ship3)
n_ship4 = len(top_ship4)

top_coca = []
top_pizza = []
top_hamburguesa = []
top_hambirguesa_refresco = []
top_ron = []
top_pasta = []
top_donas = []
top_cerveza = []
top_cotufas_refresco = []
top_cotufa = []
coca = len(top_coca)
pizza = len(top_pizza)
hamburguesa = len(top_hamburguesa)
hamburguesa_refresco = len(top_hambirguesa_refresco)
ron = len(top_ron)
pasta = len(top_pasta)
donas = len(top_donas)
cerveza = len(top_cerveza)
cotufas_refresco = len(top_cotufas_refresco)
cotufa = len(top_cotufa)

def statistics(): # Funcion de estadisticas
    top_ships = []
    top_ships.append(n_ship1)
    top_ships.append(n_ship2)
    top_ships.append(n_ship3)
    top_ships.append(n_ship4)
    top_food = []
    top_food.append(coca)
    top_food.append(pizza)
    top_food.append(hamburguesa)
    top_food.append(hamburguesa_refresco)
    top_food.append(ron)
    top_food.append(pasta)
    top_food.append(donas)
    top_food.append(cerveza)
    top_food.append(cotufas_refresco)
    top_food.append(cotufa)

    statistics1 = (sum(ticket_tours)) / len(ticket_tours) 
    print(f"Promedio de gasto de un cliente en el crucero (Ticket + tours) : {statistics1}")
    statistics2 = (((sum(ticket_tours)) - len(no_tour)) / (sum(ticket_tours))) * 100
    print(f"Porcentaje de clientes que no compran tour : {statistics2}")
    def statistics3(top_ships):
        for i in range(len(top_ships)):
            for j in range(len(top_ships) - 1):
                if top_ships[j] > top_ships[j+1]:
                    top_ships[j], top_ships[j+1] = top_ships[j+1], top_ships[j]
    statistics3(top_ships)
    print(top_ships)
    print("Top 3 cruceros con más ventas en tickets")
    if top_ships[-1] == n_ship1:
        print("1. El Dios de los Mares")
    if top_ships[-1] == n_ship2:
        print("1. La Reina Isabel")
    if top_ships[-1] == n_ship3:
        print("1. El Libertador del Océano")
    if top_ships[-1] == n_ship4:
        print("1. Sabas Nieves")
    if top_ships[-2] == n_ship1:
        print("2. El Dios de los Mares")
    if top_ships[-2] == n_ship2:
        print("2. La Reina Isabel")
    if top_ships[-2] == n_ship3:
        print("2. El Libertador del Océano")
    if top_ships[-2] == n_ship4:
        print("2. Sabas Nieves")
    if top_ships[-3] == n_ship1:
        print("3. El Dios de los Mares")
    if top_ships[-3] == n_ship2:
        print("3. La Reina Isabel")
    if top_ships[-3] == n_ship3:
        print("3. El Libertador del Océano")
    if top_ships[-3] == n_ship4:
        print("3. Sabas Nieves")
    
    def statistics4(top_food):
        for i in range(len(top_food)):
            for j in range(len(top_food) - 1):
                if top_food[j] > top_food[j+1]:
                    top_food[j], top_food[j+1] = top_food[j+1], top_food[j]
    statistics4(top_food)
    print(top_food)
    print("Top 5 productos más vendidos en el restaurante")

    if top_ships[-1] == coca:
        print("1. Coca Cola")
    if top_ships[-1] == pizza:
        print("1. Pizza")
    if top_ships[-1] == hamburguesa:
        print("1. Hamburguesa")
    if top_ships[-1] == hamburguesa_refresco:
        print("1. Hamburguesa y Refresco")
    if top_ships[-1] == ron:
        print("1. Ron")
    if top_ships[-1] == pasta:
        print("1. Pasta")
    if top_ships[-1] == donas:
        print("1. Donas")
    if top_ships[-1] == cerveza:
        print("1. Cerveza")
    if top_ships[-1] == cotufas_refresco:
        print("1. Cotufas y Refresco")
    if top_ships[-1] == cotufa:
        print("1. Cotufas")
    if top_ships[-2] == coca:
        print("2. Coca Cola")
    if top_ships[-2] == pizza:
        print("2. Pizza")
    if top_ships[-2] == hamburguesa:
        print("2. Hamburguesa")
    if top_ships[-2] == hamburguesa_refresco:
        print("2. Hamburguesa y Refresco")
    if top_ships[-2] == ron:
        print("2. Ron")
    if top_ships[-2] == pasta:
        print("2. Pasta")
    if top_ships[-2] == donas:
        print("2. Donas")
    if top_ships[-2] == cerveza:
        print("2. Cerveza")
    if top_ships[-2] == cotufas_refresco:
        print("2. Cotufas y Refresco")
    if top_ships[-2] == cotufa:
        print("2. Cotufas")
    if top_ships[-3] == coca:
        print("3. Coca Cola")
    if top_ships[-3] == pizza:
        print("3. Pizza")
    if top_ships[-3] == hamburguesa:
        print("3. Hamburguesa")
    if top_ships[-3] == hamburguesa_refresco:
        print("3. Hamburguesa y Refresco")
    if top_ships[-3] == ron:
        print("3. Ron")
    if top_ships[-3] == pasta:
        print("3. Pasta")
    if top_ships[-3] == donas:
        print("3. Donas")
    if top_ships[-3] == cerveza:
        print("3. Cerveza")
    if top_ships[-3] == cotufas_refresco:
        print("3. Cotufas y Refresco")
    if top_ships[-3] == cotufa:
        print("3. Cotufas")
    if top_ships[-4] == coca:
        print("4. Coca Cola")
    if top_ships[-4] == pizza:
        print("4. Pizza")
    if top_ships[-4] == hamburguesa:
        print("4. Hamburguesa")
    if top_ships[-4] == hamburguesa_refresco:
        print("4. Hamburguesa y Refresco")
    if top_ships[-4] == ron:
        print("4. Ron")
    if top_ships[-4] == pasta:
        print("4. Pasta")
    if top_ships[-4] == donas:
        print("4. Donas")
    if top_ships[-4] == cerveza:
        print("4. Cerveza")
    if top_ships[-4] == cotufas_refresco:
        print("4. Cotufas y Refresco")
    if top_ships[-4] == cotufa:
        print("4. Cotufas")
    if top_ships[-5] == coca:
        print("5. Coca Cola")
    if top_ships[-5] == pizza:
        print("5. Pizza")
    if top_ships[-5] == hamburguesa:
        print("5. Hamburguesa")
    if top_ships[-5] == hamburguesa_refresco:
        print("5. Hamburguesa y Refresco")
    if top_ships[-5] == ron:
        print("5. Ron")
    if top_ships[-5] == pasta:
        print("5. Pasta")
    if top_ships[-5] == donas:
        print("5. Donas")
    if top_ships[-5] == cerveza:
        print("5. Cerveza")
    if top_ships[-5] == cotufas_refresco:
        print("5. Cotufas y Refresco")
    if top_ships[-5] == cotufa:
        print("5. Cotufas")

    
def sell_room(): # Funcion base del sistema para elegir las opciones del programa
    print("\n")
    choice = int(input("""

Introduzca el numero segun la operacion que desea realizar : 
1. Comprar habitacion
2. Desocupar habitacion 
3. Venta de tours 
4. Restaurante
5. Estadisticas
--> """))
    if choice == 1:    
        selection = int(input("Introduzca (1) si desea comprar en base al barco o (2) si desea comprar en base al detino : "))
        if selection == 1:
            ship_selection = int(input(f"""
Que barco desea elegir : 
1.{name1}
2.{name2}
3.{name3}
4.{name4}
--> """
                ))
            room_type = int(input(f"""
Que tipo de habitacion desea elegir : 
1. Simple
2. Premium 
3. Vip
--> """))
            if ship_selection == 1 and room_type == 1:
                top_ship1.append(1)
                people_quantity1 = int(input("Cantidad de personas que van a viajar : "))
                n_veces1 = (people_quantity1 / 2)
                n_veces1 = math.ceil(n_veces1)
                for i in range(n_veces1):
                    ship_a_1()
                for i in range(people_quantity1):
                    ship_a_1_register()
            if ship_selection == 1 and room_type == 2:
                people_quantity2 = int(input("Cantidad de personas que van a viajar : "))
                n_veces2 = (people_quantity2 / 4)
                n_veces2 = math.ceil(n_veces2)
                for i in range(n_veces2):
                    ship_a_2()
                for i in range(people_quantity2):
                    ship_a_2_register()
            if ship_selection == 1 and room_type == 3:
                people_quantity3 = int(input("Cantidad de personas que van a viajar : "))
                n_veces3 = (people_quantity3 / 8)
                n_veces3 = math.ceil(n_veces3)
                for i in range(n_veces3):
                    ship_a_3()
                for i in range(people_quantity3):
                    ship_a_3_register()
            if ship_selection == 2 and room_type == 1:
                top_ship2.append(1)
                people_quantity4 = int(input("Cantidad de personas que van a viajar : "))
                n_veces4 = (people_quantity4 / 2)
                n_veces4 = math.ceil(n_veces4)
                for i in range(n_veces4):
                    ship_b_1()
                for i in range(people_quantity4):
                    ship_b_1_register()
            if ship_selection == 2 and room_type == 2:
                people_quantity5 = int(input("Cantidad de personas que van a viajar : "))
                n_veces5 = (people_quantity5 / 4)
                n_veces5 = math.ceil(n_veces5)
                for i in range(n_veces5):
                    ship_b_2()
                for i in range(people_quantity5):
                    ship_b_2_register()
            if ship_selection == 2 and room_type == 3:
                people_quantity6 = int(input("Cantidad de personas que van a viajar : "))
                n_veces6 = (people_quantity6 / 8)
                n_veces6 = math.ceil(n_veces6)
                for i in range(n_veces6):
                    ship_b_3()
                for i in range(people_quantity6):
                    ship_b_3_register()
            if ship_selection == 3 and room_type == 1:
                top_ship3.append(1)
                people_quantity7 = int(input("Cantidad de personas que van a viajar : "))
                n_veces7 = (people_quantity7 / 3)
                n_veces7 = math.ceil(n_veces7)
                for i in range(n_veces7):
                    ship_c_1()
                for i in range(people_quantity7):
                    ship_c_1_register()
            if ship_selection == 3 and room_type == 2:
                people_quantity8 = int(input("Cantidad de personas que van a viajar : "))
                n_veces8 = (people_quantity8 / 5)
                n_veces8 = math.ceil(n_veces8)
                for i in range(n_veces8):
                    ship_c_2()
                for i in range(people_quantity8):
                    ship_c_2_register()
            if ship_selection == 3 and room_type == 3:
                people_quantity9 = int(input("Cantidad de personas que van a viajar : "))
                n_veces9 = (people_quantity9 / 12)
                n_veces9 = math.ceil(n_veces9)
                for i in range(n_veces9):
                    ship_c_3()
                for i in range(people_quantity9):
                    ship_c_3_register()
            if ship_selection == 4 and room_type == 1:
                top_ship4.append(1)
                people_quantity10 = int(input("Cantidad de personas que van a viajar : "))
                n_veces10 = (people_quantity10 / 3)
                n_veces10 = math.ceil(n_veces10)
                for i in range(n_veces10):
                    ship_d_1()
                for i in range(people_quantity10):
                    ship_d_1_register()
            if ship_selection == 4 and room_type == 2:
                people_quantity11 = int(input("Cantidad de personas que van a viajar : "))
                n_veces11 = (people_quantity11 / 5)
                n_veces11 = math.ceil(n_veces11)
                for i in range(n_veces11):
                    ship_d_2()
                for i in range(people_quantity11):
                    ship_d_2_register()
            if ship_selection == 4 and room_type == 3:
                people_quantity12 = int(input("Cantidad de personas que van a viajar : "))
                n_veces12 = (people_quantity12 / 10)
                n_veces12 = math.ceil(n_veces12)
                for i in range(n_veces12):
                    ship_d_3()
                for i in range(people_quantity12):
                    ship_d_3_register()
        if selection == 2:
            place_selection = int(input(f"""
        
Que destino desea elegir : 
1. {place1}
2. {place2}
3. {place3}
4. {place4}
--> """))     
            place_type_selection = int(input(f"""
Que tipo de habitacion desea elegir : 
1. Simple
2. Premium 
3. Vip
--> """))
            if place_selection == 1 and place_type_selection == 1:
                people_quantity1 = int(input("Cantidad de personas que van a viajar : "))
                n_veces1 = (people_quantity1 / 2)
                n_veces1 = math.ceil(n_veces1)
                for i in range(n_veces1):
                    ship_a_1()
                for i in range(people_quantity1):
                    ship_a_1_register()
            if place_selection == 1 and place_type_selection == 2:
                people_quantity2 = int(input("Cantidad de personas que van a viajar : "))
                n_veces2 = (people_quantity2 / 4)
                n_veces2 = math.ceil(n_veces2)
                for i in range(n_veces2):
                    ship_a_2()
                for i in range(people_quantity2):
                    ship_a_2_register()
            if place_selection == 1 and place_type_selection == 3:
                people_quantity3 = int(input("Cantidad de personas que van a viajar : "))
                n_veces3 = (people_quantity3 / 8)
                n_veces3 = math.ceil(n_veces3)
                for i in range(n_veces3):
                    ship_a_3()
                for i in range(people_quantity3):
                    ship_a_3_register()
            if place_selection == 2 and place_type_selection == 1:
                people_quantity4 = int(input("Cantidad de personas que van a viajar : "))
                n_veces4 = (people_quantity4 / 2)
                n_veces4 = math.ceil(n_veces4)
                for i in range(n_veces4):
                    ship_b_1()
                for i in range(people_quantity4):
                    ship_b_1_register()
            if place_selection == 2 and place_type_selection == 2:
                people_quantity5 = int(input("Cantidad de personas que van a viajar : "))
                n_veces5 = (people_quantity5 / 4)
                n_veces5 = math.ceil(n_veces5)
                for i in range(n_veces5):
                    ship_b_2()
                for i in range(people_quantity5):
                    ship_b_2_register()
            if place_selection == 2 and place_type_selection == 3:
                people_quantity6 = int(input("Cantidad de personas que van a viajar : "))
                n_veces6 = (people_quantity6 / 8)
                n_veces6 = math.ceil(n_veces6)
                for i in range(n_veces6):
                    ship_b_3()
                for i in range(people_quantity6):
                    ship_b_3_register()
            if place_selection == 3 and place_type_selection == 1:
                people_quantity7 = int(input("Cantidad de personas que van a viajar : "))
                n_veces7 = (people_quantity7 / 3)
                n_veces7 = math.ceil(n_veces7)
                for i in range(n_veces7):
                    ship_c_1()
                for i in range(people_quantity7):
                    ship_c_1_register()
            if place_selection == 3 and place_type_selection == 2:
                people_quantity8 = int(input("Cantidad de personas que van a viajar : "))
                n_veces8 = (people_quantity8 / 5)
                n_veces8 = math.ceil(n_veces8)
                for i in range(n_veces8):
                    ship_c_2()
                for i in range(people_quantity8):
                    ship_c_2_register()
            if place_selection == 3 and place_type_selection == 3:
                people_quantity9 = int(input("Cantidad de personas que van a viajar : "))
                n_veces9 = (people_quantity9 / 12)
                n_veces9 = math.ceil(n_veces9)
                for i in range(n_veces9):
                    ship_c_3()
                for i in range(people_quantity9):
                    ship_c_3_register()
            if place_selection == 4 and place_type_selection == 1:
                people_quantity10 = int(input("Cantidad de personas que van a viajar : "))
                n_veces10 = (people_quantity10 / 3)
                n_veces10 = math.ceil(n_veces10)
                for i in range(n_veces10):
                    ship_d_1()
                for i in range(people_quantity10):
                    ship_d_1_register()
            if place_selection == 4 and place_type_selection == 2:
                people_quantity11 = int(input("Cantidad de personas que van a viajar : "))
                n_veces11 = (people_quantity11 / 5)
                n_veces11 = math.ceil(n_veces11)
                for i in range(n_veces11):
                    ship_d_2()
                for i in range(people_quantity11):
                    ship_d_2_register()
            if place_selection == 4 and place_type_selection == 3:
                people_quantity12 = int(input("Cantidad de personas que van a viajar : "))
                n_veces12 = (people_quantity12 / 10)
                n_veces12 = math.ceil(n_veces12)
                for i in range(n_veces12):
                    ship_d_3()
                for i in range(people_quantity12):
                    ship_d_3_register()
            else:
                print("Invalido")
                sell_room()
        else:
            print("Invalido")
            sell_room()
    if choice == 2:
        vacate_room()
    if choice == 3:
        tour_sale()
    if choice == 4:
        menu()
    if choice == 5:
        statistics()
    else:
        print("Invalido")
        sell_room()

def main(): # Funcion main
    print("\n")
    print("ＳＡＭＡＮ _ ＣＡＲＩＢＢＥＡＮ")
    print("\n")
    print("Cruceros disponibles : ")
    print("\n")
    print(ships_info())
    sell_room()

main()