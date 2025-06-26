#Program to print the table of no. given by user
print(" Program to print the table of no. given by user")

#while
print("using while")
num=int(input("Enter the number"))
i=1
while(i<=10):
    print(num*i)
    i+=1

#for
print("Using for")
num=int(input("Enter the number"))
for i in range(1,11):
    print(num*i) 

#Program to check user given prime no.
print(" Program to check user given prime no.")
num1= int(input("Enter the no."))
cnt=2
while(cnt<=num1):
    if(num1%2==0):
        break
    cnt+=1
print(cnt)
if(cnt==num1):
    print("Number is prime")
else:
    print("Number is not prime")

#Program to print user given no.increament by 10
print(" Program to print user given no.increament by 10")
num=int(input("Enter the no."))
end=num+10
while(num<=end):
    print(num)
    num += 1

#Program to print user given no.increament by 10 by for
print(" Program to print user given no.increament by 10 by for")
num=int(input("Enter no."))
for i in range(num,num+11):
    print(i)
    

#Program to multiply 1 to 10
sum= 1
for i in range (1,11):
    sum*=i
    print(sum)