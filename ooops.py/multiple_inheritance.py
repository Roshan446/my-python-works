class P1:
    def m1(self):
        print("inside m1")
class P2:
    def m1(self):
        print("inside m2")
class Child(P1,P2):
    pass

ch = Child()
ch.m1()
