from product_manager import ProductManager
from product import Product

if __name__ == "__main__":
    prod_manager= ProductManager()
    p1 = Product("p1", 10, 3)
    p2 = Product("p2", 20, 7)
    p3 = Product("p3", 30, 11)
    p4 = Product("p4", 40, 15)
    prod_manager.add_product(p1)
    prod_manager.add_product(p2)
    prod_manager.add_product(p3)
    prod_manager.add_product(p4) 
    prod_manager.print_product()
    prod_manager.total_product_price()
