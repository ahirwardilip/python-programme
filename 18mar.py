'''
rol=[100,101]
name=["amit","sumit"]
per=[66.66,67.77]
d={}
d={"Roll No.":rol,"Name":name,"Per":per}
print(d)
'''

'''
rol=[]
name=[]
per=[]
d={}
temp=True
while temp:
    roll=int(input("Enter Roll Number:"))
    Name=input("Enter Name:")
    Per=float(input("Enter Percentage:"))
    rol.append(roll)
    name.append(Name)
    per.append(Name)
    op=int(input("Do u want to insert more records...press 1.Yes 2.No"))
    if op==1:
        temp=True
    else:
        temp=False    
d={"Roll No.":rol,"Name":name,"Per":per}
print(d)
'''

'''
rol=[]
name=[]
per=[]
d={}
temp=True
while temp:
    roll=int(input("Enter Roll Number:"))
    Name=input("Enter Name:")
    Per=float(input("Enter Percentage:"))
    rol.append(roll)
    name.append(Name)
    per.append(Name)
    op=int(input("Do u want to insert more records...press 1.Yes 2.No"))
    if op==1:
        temp=True
    else:
        temp=False    
d["ROLL"]=roll
d["NAME"]=Name
d["PER"]=Per
print(d)
'''

#Functions:It is the smallest individual sub-programs which performs specific tasks.There are two types of functions:-
# 1.Built-in Functions                 2.User defined Functions
#They have also four types:-
# 1.No argument and no return type     2.argument and no return type
# 3.No argument and return type        4.argument and return type

# Syntax: def<function_name>(<arg_list>):
#                ===
#                ===

# 1.No argument and no return type
'''
def add():
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    c=a+b
    print("Sum is:",c)
add()
'''

'''
def si():
    p=int(input("Enter Principal:"))
    r=float(input("Enter Rate:"))
    t=int(input("Enter Time:"))
    Si=((p*r*t)/100)
    print("Simple Interest is:",Si)
si()
'''

# 2.argument and no return type
'''
def add(a,b):
    c=a+b
    print("Sum is:",c)
a=int(input("Enter First Number:"))
x=int(input("Enter Second Number:"))
add(a,x)
'''

# 3.No argument and return type 
'''
def add():
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    c=a+b
    return c
r=add()
print("Sum is:",r)
print("Sum is:",add())
'''

# 4.argument and return type
'''
def add(a,b):
    c=a+b
    return c
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
r=add(a,b)
print("Sum is:",r)
'''

