import random


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)
    
    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio >= 0.5 and ratio < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"
    
    def explode(self):
        pass  # TODO - implement


class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)
    
    def explode(self):
        pass  # TODO - implement

    def punch(self):
        pass  # TODO - implement
