class Employee:
    comp="UPES"
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = self.fname + '.' + self.lname + '@' + self.comp + '.com'
    def getEmail(self):
        return self.email
    def getName(self):
        return self.fname + ' ' +self.lname
    def getPay(self):
        return self.pay


s1 = Employee('Mohandas', 'Gandhi', 50000)
print(s1.getEmail())
print(s1.getName())
print(s1.getPay())