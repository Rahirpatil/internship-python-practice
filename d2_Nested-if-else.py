#Program to check greater no.
num1=int(input("Enter no1"))
num2=int(input("Enter no2"))

if(num1>num2):
    print("no.1 is greater")
else:
    print("no.2 is greater")


#Program to check no. is +ve or -ve
print("Program to check no. is +ve or -ve")
num=int (input("Enter no."))

if(num>0):
    print("Number is +ve")
elif(num<0):
    print("Number is -ve")
else:
    print("Number is neutral")


#Program to check the grade
per=float(input("Enter the percentage"))
if(per>=80):
    print("A grade")
elif(per>=60):
    print("B grade")
elif(per>=40):
    print("C grade")
else:
    print("Fail")


#program to check greater no. among 3
print("program to check greater no. among 3")
n1=int(input("Enter the no.1"))
n2=int(input("Enter the no.2"))
n3=int(input("Enter the no.3"))

if(n1>n2 and n1>n3):
    print("no.1 is greater")
elif(n2>n1 and n2>n3):
    print("no.2 is greater")
else:
    print("no.3 is greater")
    