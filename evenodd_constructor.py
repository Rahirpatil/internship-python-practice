class Evenodd():
    def __init__(self):
        self.num=int(input("Enter the no."))
    def display(self):
        if self.num%2==0:
            print("Even")
        else:
            print("odd")

obj=Evenodd()
obj.display()