#solution to question number 1

n = int(input("enter the year"))
if (n % 4) == 0:
   if (n % 100) == 0:
       if (n % 400) == 0:
           print("it is a leap year")
       else:
           print("it is not a leap year")
   else:
       print("it is a leap year")
else:
   print("it is not a leap year")

#solution to question number 2

len = int(input("enter the length"))
bre = int(input("enter the breadth"))
if(len==bre):
    print("it is a square")
else:
    print("it is a rectangle")

#solution for question number3


p1 = int(input("enter the age of person one "))
p2 = int(input("enter the age of person two "))
p3 = int(input("enter the age of person three "))
if(p1>p2 and p1>p3):
    print("person one is oldest")
elif(p2>p1 and p2>p3):
    print("person two is oldest")
else:
    print("person three is oldest")
if(p1<p2 and p1<p3):
    print("person one is youngest")
elif (p2<p1 and p2<p3):
    print("person two is youngest")
else:
    print("person three is youngest")


#solution for question number 4


age = int(input("enter the age"))
gen = input("enter the gender: M or F")
mar = input("enter the marital status: Y or N")
if(gen=='f'):
    print("she will work only in urban areas")
elif(gen=='m'):
    if(age>=20 and age<=40):
        print("he may work in anywhere")
    elif(age>40 and age<=60):
        print("he will work in urban areas only")
    else:
        print("ERROR")
else:
    print("ERROR")



#solution to question number 5


q = int(input("enter the quantity"))
cost = q*100
if(cost>=1000):
    tot_cost = cost-(cost *0.10)
    print("Total cost is",tot_cost)
else:
    print("total cost is",cost)
