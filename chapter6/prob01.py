a1= int(input("enter your number1: "))
a2= int(input("enter your number2: "))
a3= int(input("enter your number3: "))
a4= int(input("enter your number4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("grestest number is : ", a1)

elif(a2>a3 and a2>a1 and a1>a4):
    print("grestest number is : ", a2)

elif(a3>a2 and a3>a1 and a1>a4):
    print("grestest number is : ", a3)       

else:
    print("the gretest number is: ", a4)



