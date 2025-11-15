#listComperhension From Hackerrank
lst=[]
for i in range (10):
    lst.append(i*i)
print(lst)
lst2=[ j for j in range(10) if j%2==0]
print(lst2)
lst3=[k for k in range(10) if k%2!=0]
print(lst3)
#print word in upper case
lst4=[word.upper() for word in ["python","he","bhai"]]
print(lst4)
a=[1,2]
b=[2,5]
pairs=[]
for x in a:
    for y in b:
        pairs.append((x,y))
print(pairs)

A = [1, 2, 3]
B = [4, 5]
lst4=[]
for x in A:
    for y in B:
        lst4.append((x,y))
print(lst4)
        
#using list comperhension

lst5=[(x,y)for x in A for y in B]
print("This is list comperhension list",lst5)