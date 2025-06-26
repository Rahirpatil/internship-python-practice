print("Print dict with pair using for loop")
mydict={"brand":"Ford","model":"mustang","year":1964}
for i in mydict:
    print(i,"-",mydict[i])

print("Print dict_values loop-")
for i in mydict.values():
    print(i)

print("Print dict_keys loop-")
for i in mydict.keys():
    print(i)

print("Print dict_key-value using loop")
for a,b in mydict.items():
    print(a,'-',b)
    