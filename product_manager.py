class ProductManager:

    def __init__(self):
        self.product = []

    def add_product(self, product):
        self.product.append(product)

    def print_product(self):
        for product in self.product:
            product.print()

    def total_product_price(self):
        total_price = 0
        for product in self.product:
            total_price += product.quantity * product.price
        print("total price: " + str(total_price))
