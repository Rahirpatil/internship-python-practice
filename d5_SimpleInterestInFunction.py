#Function without parameter with return
def sum():
    p=float(input("Enter the p amount"))
    r=float(input("Enter the rate"))
    n=int(input("Enter the years"))
    amount=(p*r*n)
    return amount
amount=sum()
print(amount)

#function with parameter without return
def sum1(pr,ra,ye):
    amount1=(pr*ra*ye)/100
    return amount1
amount1=sum1(12000,12.1,3)
print(amount1)
