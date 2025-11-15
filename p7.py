#listComperhension From Hackerrank
lst=[]
for i in range (10):
    lst.append(i*i)
print(lst)
lst2=[ j for j in range(10) if j%2==0]
print(lst2)
lst3=[k for k in range(10) if k%2!=0]
print(lst3)
lst4=[word.upper() for word in ["python","he","bhai"]]
print(lst4)

