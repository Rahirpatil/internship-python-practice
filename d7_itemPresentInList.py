#item Present in the list0
mylist=["apple","banana","cherry","mango"]
userchoice=input("Enter the fruit name")
if userchoice in mylist:
    print("Present")
else:
    print("Not present")

#Add a specific index no.
#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)