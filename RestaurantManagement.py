class RestauranteManagement: #Clase
    def __init__ (self, product1, price1, amount1, product2, price2, amount2, product3, price3, amount3, product4, price4 , amount4, product5, price5, amount5):
        self.product1 = product1
        self.price1 = price1
        self.amount1 = amount1
        self.product2 = product2
        self.price2 = price2
        self.amount2 = amount2
        self.product3 = product3
        self.price3 = price3
        self.amount3 = amount3
        self.product4 = product4
        self.price4 = price4
        self.amount4 = amount4
        self.product5 = product5
        self.price5 = price5
        self.amount5 = amount5

    def see_menu1(self): #Metodos
        print(f"""
    PRODUCTOS               
    PRECIO     
    CANTIDAD

1.  {self.product1}
    {self.price1}         
    {self.amount1}
2.  {self.product2}          
    {self.price2}            
    {self.amount2}
3.  {self.product3}   
    {self.price3}      
    {self.amount3}
4.  {self.product4}  
    {self.price4}  
    {self.amount4}
5.  {self.product5} 
    {self.price5}  
    {self.amount5}
""")

