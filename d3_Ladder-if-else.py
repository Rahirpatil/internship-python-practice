num1= int(input("Enter the no."))
num2= int(input("Enter the no."))
num3= int(input("Enter the no."))

if(num1>num2):
    if(num1>num3):
        print(str(num1)+" is greater")
    else:
        print(str(num3)+" is greater")
else:
    if(num2>num3):
        print(str(num2)+" is greater")
    else:
        print(str(num3)+" is greater")