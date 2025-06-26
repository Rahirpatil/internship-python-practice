class add:
    def getdata(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def calculate(self):
        self.cal=self.num1+self.num2
    def display(self):
        print("addition",self.cal)

obj=add()
obj.getdata(12,18)
obj.calculate()
obj.display()