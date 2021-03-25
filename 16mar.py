'''
l=[1,2,3,4,5,6,7,8,9,10]
print(l)
print(l[1:4])
print(l[:5])
print(l[5:])
print(l[-1])
print(l[-2])
'''

'''
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(mat)
print(mat[0])
print(mat[1:2])
'''

#Tuple:It is same as list,but it is immutable.It is written within parentheses.

'''
t=()
print(t)
'''
#t.append(5) #error


'''
t=(1,2,3,4,5)
print(t)
print(t[0])
print(t[1:3])
print(sum(t))
print(len(t))
print(sum(t)/len(t))
print(max(t))
print(min(t))
'''

'''
a=10
print(a)
del a
print(a)
'''

'''
l=[1,2,3,4,5]
print(l)
del l[3]
print(l)
del l
print(l)
'''

'''
t=(1,2,3,4,5)
print(t)
#del t[3] #not possible
del t
print(t)
'''

#Dictionary:It is the advanced form of list where we have two things:keys and values.It is written within curly braces.

'''
d={"rol":100,"name":"Amit","per":55.55}
print(d)
print(d.keys())
print(d.values())
print(d["rol"])
'''

'''
d={}
size=int(input("Enter Size:"))
for i in range(size):
    key=input("Enter Key:")
    value=input("Enter Value:")
    d[key]=value
    print(d)
print(d)
'''
'''
d={}
temp=True
while temp:
    key=input("Enter Key:")
    value=input("Enter Value:")
    d[key]=value
    op=int(input("Do u want to insert more record...1.Yes 2.No"))
    if(op==1):
        temp=True
    else:
        temp=False
print(d)
'''
