class Employee:
    @classmethod
    def from_string(cls,emp_str):
        fname,lname,pay = emp_str.split('-')
        return cls(fname,lname,pay)

    def __init__(self,first,last,pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        
    def display(self):
        print(self.firstname + ' '+self.lastname + ' '+ self.pay)

emp_1_str = 'John-Abraham-50000'
emp_1 = Employee.from_string(emp_1_str) #stmt1
emp_1.display()