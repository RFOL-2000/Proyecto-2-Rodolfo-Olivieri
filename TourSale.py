class TourSale: #Clase
    def __init__(self, price, top_quantity, time, limit):
        self.price = price
        self.top_quantity = top_quantity
        self.time = time
        self.limit = limit

    def see_tour(self): # Metodo
        print(f"""
Precio : {self.price}
Hora : {self.time}
""")

class Port(TourSale): #Clase hija
    def __init__(self, price, top_quantity, time, limit):
        super().__init__(30, 4, "12 PM", 10)

    def see_tour1(self): # Metodo
        print(f"""
Precio : {self.price}
Hora : {self.time}
""")
class Tasting(TourSale): #Clase hija
    def __init__(self, price, top_quantity, time, limit):
        super().__init__(100, 2, "12 PM", 100)

    def see_tour2(self): # Metodo
        print(f"""
Precio : {self.price}
Hora : {self.time}
""")
class Jogging(TourSale): #Clase hija
    def __init__(self, price, top_quantity, time, limit):
        super().__init__(0, "Ilimitado", "6 AM", "Ilimitado")
    def see_tour3(self): # Metodo
        print(f"""
Precio : {self.price}
Hora : {self.time}
""")
class History(TourSale): #Clase hija
    def __init__(self, price, top_quantity, time, limit):
        super().__init__(40, 4, "10 AM", 15)
    def see_tour4(self): # Metodo
        print(f"""
Precio : {self.price}
Hora : {self.time}
""")