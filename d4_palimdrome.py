
def palimdrome():
    num=int(input("Enter no"))
    temp=num
    rem=0
    sum=0
    while num>0:
        rem=(num %10)
        sum=(sum*10)+rem
        num=int(num/10)

    if(temp==sum):
        print("Number is palimdrome")
    else:
        print("Number is not palimdrome")

palimdrome()