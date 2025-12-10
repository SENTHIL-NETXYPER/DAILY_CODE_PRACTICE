class emp:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager (emp):
    def __init__(self,name,dept,salary):
        super().__init__(name,salary)
        self.dept=dept
    def display(self):
        print(self.name,self.salary,self.dept)
a=manager("fcuk","my name ",10000)
a.display()







print(len([1,2,3,4,5]))
