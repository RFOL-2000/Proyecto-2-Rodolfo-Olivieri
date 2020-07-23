class Registry: # Clase
    def __init__(self, name, dni, age, discapacity):
        self.name = name
        self.dni = dni
        self.age = age
        self.discapacity = discapacity

    def see_info(self): #Metodo
        print(f"""
Nombre : {self.name}
Dni : {self.dni}
Edad : {self.age}
Discapacidad : {self.discapacity}
        """)