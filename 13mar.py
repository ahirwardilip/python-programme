                        #list,tuple,dictionary and set

#list:It is same as array , but it is a collection of heterogenous data items.It is dynamic in nature.
#It is written within square brackets.



'''
l1=[]
print(l1)
'''

'''
l2=[1,2,3]
print(l2)
'''

'''
l3=[100,"Amit",55.55]
print(l3)
'''

'''
l=[]
i=1
while i<=5:
    data=int(input("Enter Value:"))
    l.append(data)
    i=i+1
    print(i)
print("Complete list:",l)
'''

'''
l=[]
for i in range(5):
    data=int(input("Enter Value:"))
    l.append(data)
    print(i)
print("Complete list:",l)
'''

'''
l=[]
size=int(input("Enter Size:"))
i=1
while i<=size:
    data=int(input("Enter Value:"))
    l.append(data)
    i=i+1
    print(i)
print("Complete list:",l)
'''

'''
l=[]
size=int(input("Enter Size:"))
for i in range(size):
    data=int(input("Enter Value:"))
    l.append(data)
    print(i)
print("Complete list:",l)

'''

'''
l=[1,2,3,4,5]
print("Sum of elements is",sum(l))
print("Length of array is",len(l))
print("Average of elements is",sum(l)/len(l))
'''

'''
be1=[1,2,3,4,5]
be2=[1,2,3,4]
be3=[1,2,4]
be4=[2]
print(be1)
print(be2)
print(be3)
print(be4)
BE=[be1,be2,be3,be4]
print(BE)
'''

'''
BE=[]
temp1=True
while temp1:
    temp=True
    be=[]
    while temp:
        rol=int(input("Enter Roll Number:"))
        be.append(rol)
        op=int(input("Do you want to insert more Roll Number ... Press 1.Yes 2.No"))
        if op==1:
            temp=True
        else:
            temp=False
    print(be)
    BE.append(be)
    print(BE)
    op1=int(input("Do you want to insert more Data ... Press 1.Yes 2.No"))
    if op1==1:
        temp1=True
    else:
        temp1=False
print(BE)
'''list_student
