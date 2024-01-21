from typing import List

# Clase que simula una fábrica de pasteles y realiza diferentes funciones. Estos incluyen elegir diferentes tamaños y 
# sabores de pastel, incluidos pequeños, medianos y grandes, y de chocolate o vainilla. Además, 
# la clase simple permite a los desarrolladores agregar chispas o cerezas al pastel, devolver una lista de ingredientes 
# y devolver el precio del pastel según el tamaño y los ingredientes
class CakeFactory:
    def __init__(self, cake_type: str, size: str):
        self.cake_type = cake_type
        self.size = size
        self.toppings = []
    
        # Precio según tipo y tamaño de pastel
        self.price = 10 if self.cake_type == "chocolate" else 0
        self.price += 2 if self.size == "medium" else 4 if self.size == "large" else 0
        
    def add_topping(self, topping: str):
        self.toppings.append(topping)
        # Adding 1 to the price for each topping
        self.price += 1

    def check_ingredients(self) -> List[str]:
        ingredients = ['flour', 'sugar', 'eggs']
        ingredients.append('cocoa') if self.cake_type == "chocolate" else ingredients.append('vanilla extract')
        ingredients += self.toppings
        return ingredients

    def check_price(self) -> float:
        return self.price
    
# Ejemplo de cómo crear un pastel y agregarle aderezos
cake = CakeFactory("chocolate", "medium")
cake.add_topping("sprinkles")
cake.add_topping("cherries")
cake_ingredients = cake.check_ingredients()
cake_price = cake.check_price()


print(cake_ingredients, cake_price)