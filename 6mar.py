'''
i=5
while i>=1:
    j=1
    while j<=i:
        print('',end=' ')
        j=j+1
    j=5
    while j>=i:
        print('* ',end=' ')
        j=j-1
    print()
    i=i-1
'''

#print tables from 1 to n

'''
n=int(input("Enter Number:"))
i=1
while i<=n:
    j=1
    while j<=10:
        print(i*j,end=' ')
        j=j+1
    print()
    i+=1
'''

'''
N=int(input("Enter Number:"))
i=1
while i<=N:
    n=i
    f=1
    while n>=1:
        f=f*n
        n=n-1
    print("Factorial of",i,"is",f)
    i+=1
'''
'''
N=int(input("Enter Number:"))
for i in range(1,N+1,1):
    f=1
    for n in range(i,1,-1):
        f=f*n
    print("Factorial of",i,"is",f)
'''

'''
n=int(input("Enter Number:"))
for i in range(1,n+1,1):
    for j in range(1,11,1):
        print(i*j,end=' ')
    print()
''' 

'''
l=[34,33,3.55,"aaa"]
print(l)
'''
