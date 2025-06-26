#Function without parameter without return
print("Function without parameter without return-")
def add():
    num1=int(input("Enter the no."))
    num2=int(input("Enter the no."))
    result=num1+num2
    print(result)
result1=add()

#Function without parameter with return
print("Function without parameter with return-")
def add2():
    n1=int(input("Enter the no."))
    n2=int(input("Enter the no."))
    res=n1+n2
    return res
res=add2()
print(res)

#Function with parameter without return
print("Function with parameter without return")
def add(a,b):
    a=int(input("Enter the no."))
    b=int(input("Enter the no."))
    r=a+b
    print(r)
r=add(12,10)

#Function with parameter with return
print("#Function with parameter with return")
def add4(x,y):
    res=x+y
    return res
result=add4(12,18)
print(result)
