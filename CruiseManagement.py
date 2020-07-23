class CruiseManagement: # Clase
    def __init__(self, ship_name, ship_route, departure_date, ticket_cost, rooms_and_corridors, room_capacity):
        self.ship_name = ship_name
        self.ship_route = ship_route
        self.departure_date = departure_date
        self.ticket_cost = ticket_cost
        self.rooms_and_corridors = rooms_and_corridors
        self.room_capacity = room_capacity

class Ship1(CruiseManagement): # Clase hija
    
    def __init__(self, ship_name, ship_route, departure_date, ticket_cost, rooms_and_corridors, room_capacity):
        super().__init__(ship_name, ship_route, departure_date, ticket_cost, rooms_and_corridors, room_capacity)

class Ship2(CruiseManagement): # Clase hija
    
    def __init__(self, ship_name, ship_route, departure_date, ticket_cost, rooms_and_corridors, room_capacity):
        super().__init__(ship_name, ship_route, departure_date, ticket_cost, rooms_and_corridors, room_capacity)
    
class Ship3(CruiseManagement): # Clase hija
    
    def __init__(self, ship_name, ship_route, departure_date, ticket_cost, rooms_and_corridors, room_capacity):
        super().__init__(ship_name, ship_route, departure_date, ticket_cost, rooms_and_corridors, room_capacity)

class Ship4(CruiseManagement): # Clase hija
    
    def __init__(self, ship_name, ship_route, departure_date, ticket_cost, rooms_and_corridors, room_capacity):
        super().__init__(ship_name, ship_route, departure_date, ticket_cost, rooms_and_corridors, room_capacity)
