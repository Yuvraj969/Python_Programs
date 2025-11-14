#number greater that 50
n = int(input("enter the input?"))

lst = []

for i in range(n):
    value = int(input("enter the number="))
    lst.append(value)

print(lst)
abc=0
for j in lst:
    if j > 50:
        print(j)
        abc=abc+1
print(abc)