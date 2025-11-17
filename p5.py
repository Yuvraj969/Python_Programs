#LISTCOMPERHENSION IN PYTHON
#TAKE 3 INPUT FROM THE USER AND PRINT THE ALL POSSIBLE OUTCOMES 
a=int(input())
b=int(input())
c=int(input())
lst=[(x,y,z) for x in range(a+1) for y in range(b+1) for z in range(c+1)]
print(lst)
