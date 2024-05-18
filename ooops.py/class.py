class Employe:
    id:int
    name:str
    department:str
    salary:int
    def set_emp(self, id, sal, dep, name):
        self.id = id
        self.salary = sal
        self.department = dep
        self.name = name
    def display_emp(self):
        print(self.id, self.salary, self.department, self.name)

emp1 = Employe()
emp1.set_emp(489085, 500000, "it", "Roshan")
emp2 = Employe()
emp2.set_emp(489086, 500000, "it", "mobin")
emp1.display_emp()
emp2.display_emp()


