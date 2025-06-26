num=int(input("Enter the no."))
rem=0
def digit():
    while(num>0):
        rem=(num%10)
        print(rem)
        num=int(num/10) 
    print(num)
digit()