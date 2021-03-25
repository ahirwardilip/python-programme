'''
li=[]
print(li)
'''

'''
li=[34,2,34,23,4]
print(li)
'''

'''
li=[100,66.66,"amit"]
print(li)
'''

'''
li=[100,66.66,"amit"]
i=0
while i<=2:
    print(li[i])
    i+=1
'''

'''
li=[100,66.66,"amit"]
for da in li:
    print(da)
'''

#input data into list and print it

'''
li=[]
i=0
while i<5:
    data=input("Enter value:")
    li.append(data)
    i+=1
print(li)
'''

'''
li=[]
num=int(input("Enter array size:"))
i=0
while i<num:
    data=input("Enter Value:")
    li.append(data)
    i+=1
    print(li)
'''

'''
li=[]
temp=True
while temp:
    data=input("Enter value:")
    li.append(data)
    print(li)
    op=int(input("Do you want to insert more records.... 1.Yes 2.No"))
    if op==1:
        temp=True
    else:
        temp=False
print(li)
'''


#write a program to find out sum and average of n values using array

'''
li=[]
num=int(input("Enter array size:"))
i=0
while i<num:
    data=int(input("Enter Value:"))
    li.append(data)
    i+=1
    print(li)
    
sum=0
for i in li:
    sum+=i
    i+=1
print("Sum is",sum)    
print("Avg is",sum/num)
'''

'''
li=[]
temp=True
c=0
while temp:
    c=c+1
    data=int(input("Enter Value:"))
    li.append(data)
    print(li)
    op=int(input("Do you want to insert more records.... 1.Yes 2.No"))
    if op==1:
        temp=True
    else:
        temp=False
print(li)
s=0
for d in li:
    s=s+d
print("Sum is:"+str(s))
print("Avg is:"+str(s/c))
'''

'''
li=[]
temp=True
while temp:
    data=int(input("Enter value:"))
    li.append(data)
    print(li)
    op=int(input("Do you want to insert more records.... 1.Yes 2.No"))
    if op==1:
        temp=True
    else:
        temp=False
print(li)
sum=0
for i in li:
    sum+=i
    i+=1
print("Sum is",sum)    
print("Avg is",sum/len(li))
'''
