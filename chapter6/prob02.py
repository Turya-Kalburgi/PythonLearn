marks1 = int(input("enter your marks of 1: "))
marks2 = int(input("enter your marks of 2: "))
marks3 = int(input("enter your marks of 3: "))

#percentages
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("congrates you are pass/TRAPED", total_percentage)

else:
    print("you are safe!!", total_percentage)    