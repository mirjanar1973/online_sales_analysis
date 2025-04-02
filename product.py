class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def print(self):
        print("name: " + str(self.name) + ", price: " + str(self.price) + ", quantity: " + str(self.quantity))

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity
    