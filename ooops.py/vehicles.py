class Parent:
    def  properties(self):
        self.vehilcles= ["bikes", "splendor"]
        return self.vehilcles
class Child(Parent):
    def properties(self):
        self.context = super().properties() 
        self.context.append("baleno")
        return self.context
ch = Child()
print(ch.properties())