# factory.py

class Product:
    def operation(self):
        pass

class ConcreteProduct(Product):
    def operation(self):
        print("ConcreteProduct operation")

class Factory:
    def create_product(self):
        pass

class ConcreteFactory(Factory):
    def create_product(self):
        return ConcreteProduct()

# main.py

from factory import ConcreteFactory

if __name__ == "__main__":
    factory = ConcreteFactory()
    product = factory.create_product()
    product.operation()
