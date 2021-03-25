'''
P=int(input("Enter Principal:"))
R=float(input("Enter Rate:"))
T=int(input("Enter Time:"))
SI=(P*R*T)/100
print("Simple Interest is:",SI)
'''

#Control statements:-

# 1.Conditional statements:-
#        (1)If statements   (2)If...else statements     (3)If...elif...else statements      (4)Nested if statements
# 2.Looping statememts:-
#        (1)While statements    (2)For statements
# 3.Branching statements:-
#        (1)Break statements    (2)Continue statements      (3)Pass statements

#If statements(syntax):-
#        if <exp>:
#             ===
#             ===

#If...else statements(syntax):-
#        if <exp>:
#            ===
#            ===
#        else:
#            ===
#            ===

#If...elif...else statements:-
#        if <exp>:
#            ===
#            ===
#        elif <exp>:
#            ===
#            ===
#        elif <exp>:
#            ===
#            ===
#        ===
#        ===
#        ===
#        else:
#            ===
#            ===

#Nested if satements:-
#        if <exp>:
#            ===
#            ===
#            if <exp>:
#                ===
#            else:
#                ===
#        else:
#            ===
#            ===
#            if <exp>:
#                ===
#            else:
#                ===

#Write a program to find out greater number from two numbers.
                
'''
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
if a>b:
    print("Greater number is:",a)
else:
    print("Greater number is:",b)
'''

#&&=and         ||=or           !=not

#Write a program to find out greater number from three numbers.

'''
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
if a>b and a>c:
    print("Greatest number is:",a)
elif b>a and b>c:
    print("Greatest number is:",b)
else:
    print("Greatest number is:",c)
'''

'''
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
if a>b and a>c:
    print("a is greatest.....")
elif b>c:
    print("b is greatest....")
else:
    print("c is greatest....")
'''

#Write a program to find out greater number from three numbers using nested if statements.

'''
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
if a>b and a>c:
    print("a is greatest....")
else:
    if b>c:
        print("b is greatest....")
    else:
        print("c is greatest....")
'''

#Write a program to find out total marks and percentage of any student and also find out their division according to
# as follows:-
# 60 to 100 I       45 to 59.99 II      35 to 44.99 III         00 to 34.99 Fail        rest invalid

'''
H=int(input("Enter Hindi marks:"))
E=int(input("Enter English Marks:"))
M=int(input("Enter Maths Marks:"))
TM=H+E+M
P=TM/3.0
print("Total Marks:",TM)
print("Percentage:",P)
if P>=60 and P<=100:
    print("First Division")
elif P>=45 and P<60:
    print("Second Division")
elif P>=35 and P<45:
    print("Third Division")
elif P>=0 and P<35:
    print("Fail")
else:
    print("Invalid")
'''
