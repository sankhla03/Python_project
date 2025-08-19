x1 = int(input("enter number number x1: "))

x2 = int(input("enter number number x2: "))

op = input("enter operater(+,-,*,/,%) : ")

if(op =='+'):
    print(x1+x2)

elif(op=='-'):
    print(x1-x2)
elif(op=='*'):
    print(x1*x2)
elif(op=='/'):
    print(x1/x2)

else:
    print(x1%x2)
