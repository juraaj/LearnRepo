from product import Product
from price import Price
from license import License

class ConcreteProduct(Price, Product, License):
    """Concrete Product Price"""

    def __init__(self):
        print("ConcreteProduct Constructor")
        super().__init__()

