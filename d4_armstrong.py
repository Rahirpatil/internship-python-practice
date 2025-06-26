num=int(input("Enter no."))
temp=num
rem=0
sum=0
def arm():
    while(num>0):
        rem=num%10
        sum=(rem*rem*rem)
        num=int(num/10)
    if(temp==sum):
        print("Number is Armstrong")
    else:
        print("Number is not Armstrong")
arm()