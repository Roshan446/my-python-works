class Cusine:
    name:str
    def __init__(self, c_name):
        self.c_name= c_name
    def __str__(self):
        return self.c_name
class Dish(Cusine):
    dish_name: str
    ingredients: str
    price: int
    def __init__(self, c_name, dish_name, ingredients, price):
        super().__init__(c_name)
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.price = price
d1 = Dish("French", "croisant", "wheat", 120000)
print(d1)

     
