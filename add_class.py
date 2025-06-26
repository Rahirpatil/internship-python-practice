class add:
    def getdata(self):
        self.num1=int(input("Enter the no."))
        self.num2=int(input("Enter the no."))
    def calculate(self):
        self.cal=self.num1+self.num2
    def display(self):
        print("addition",self.cal)

obj=add()
obj.getdata()
obj.calculate()
obj.display()