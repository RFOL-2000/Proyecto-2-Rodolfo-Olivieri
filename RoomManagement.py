class RoomManagment: # Clase 
    def __init__(self, hall_letter, room_number, capacity, information):
        self.hall_letter = hall_letter
        self.room_number = room_number
        self.capacity = capacity
        self.information = information

    def see_room(self): # Metodo
        print(f"""
Habitacion : {self.hall_letter}{self.room_number}
Capacidad : {self.capacity}
Informacion de la habitacion : {self.information}
""")

class Simple(RoomManagment): # Clase hija
    def __init__(self, hall_letter, room_number, capacity, information):
        super().__init__(hall_letter, room_number, capacity, "Si puede tener servicio a la habitación")

class Premium(RoomManagment): # Clase hija
    def __init__(self, hall_letter, room_number, capacity, information):
        super().__init__(hall_letter, room_number, capacity, "Si posee vista al mar")

class Vip(RoomManagment): # Clase hija
    def __init__(self, hall_letter, room_number, capacity, information):
        super().__init__(hall_letter, room_number, capacity, "Si puede albergar fiestas privadas")