list1=[1,2,3,4,5,6,7]
list2=[1,2,3,4,5,6,7,8]
resultlist=[]
for i in list1:
    if(i%2==0):
        resultlist.append(i)
for i in list2:
    if(i%2!=0):
        resultlist.append(i)
print(resultlist)