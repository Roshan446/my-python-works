class Mobile:
    Brand: str
    processor: str
    model_name: str
    price: int
    def __init__(self, Brand, processor, model_name, price):
        self.Brand = Brand
        self.processor = processor
        self.model_name = model_name
        self.price = price
    def display_mobile(self):
       print(self.Brand, self.processor, self.model_name, self.price)
    def __str__(self):
        return self.Brand + self.model_name

obj1 = Mobile("samsung", "snapdragon 690","M53g", 28000)

obj1.display_mobile()
print(obj1)
