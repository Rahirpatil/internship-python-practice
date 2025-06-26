#function with parameter with return
def prime(num):
    cnt=2
    while(num>=cnt):
        if(num%2==0):
            break
        cnt+=1
    if(cnt==num):
            return "Number is prime"
    else:
            return "Number not is prime"
        
num=int(input("Enter no."))
prime1=prime(num)
print(prime1)