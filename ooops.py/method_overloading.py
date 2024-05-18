class Parent:
    def mobile(self):
        print("redmi note 12")
    def vehicle(self):
        print("splendor")
class Child:
    def mobile(self):         #<---- #overiding
        print("iphone 12")

ch = Child()
ch.mobile()