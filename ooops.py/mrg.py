class Parent:
    def propertie(self):
        print("10kg gold 1 cr 10 cars")
    def bride(self):
        print("nimitha")

class Child(Parent):
    def bride(self):
        print("nimmy")

ch = Child()
ch.bride()
ch.propertie()