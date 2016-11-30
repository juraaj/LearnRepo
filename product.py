class Product:
    'Product class'

    static_attr = "static"

    def __init__(self):
        print("Product Constructor")
        super().__init__()
        self.name = "DefaultProductName"

    def doMyJob(self):
        print("I am not working this is parent method. Should be overriden!!!")
