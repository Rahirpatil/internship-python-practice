#Print List
mylist = ["apple", "banana", "cherry"]
print(mylist)
mylist2 = [1, 5, 7, 9, 3]
print(mylist2)
mylist3 = [True, False, False]
print(mylist3)
print(type(mylist3))
thelist = ["apple", "banana", "cherry"]

#Append list
mylist.append("orange")
print(mylist)

#Extend List
mylist2.extend(mylist)
print(mylist2)

#Remove the item in the list
mylist.remove("banana")
print(mylist)

#Clear the list
print(thelist)
thelist.clear()
print(thelist)
