class Evenodd():
    def __init__(self,num):
        self.num=num
    def display(self):
        if self.num%2==0:
            print("Even")
        else:
            print("odd")
num=int(input("Enter no."))
obj=Evenodd(num)
obj.display()