lst=["banana","apple","cherry"]
for i in lst:
    print(i)
lst.insert(1,"onion")
for i in lst:
    print(i)
lst.remove("banana")
print(lst)
print(len(lst))
if "cherry" in lst:

    print(True)
lst2=[10,20,30,25,40,5,35]
small=lst2[0]
for i in lst2:
    if i>small:
        small=i
print(small)
print("this line was coded from the Android device")

