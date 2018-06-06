#solution for question number 1
'''
number=0
while(number<9):
	print("numbers is: ",number)
	number=number+1
print("task completed")
#alternative way if we want to take input during run time
i=0
while(i<9):
	num=input("enter a number")
	print("the number is: ",num)
	i=i+1
print("task completed")

#solution to question number 2
while True:
	print("task done")

#solution to question number 3
list1=[6,2,7,4]
print("list is: ",list1)
list2=[]
for i in list1:
	list2.append(i**2)
print("square list",list2)

#solution to question number 4

list=[1,'a',2.5,5,'b',9.4,'c',8.4,6,4.2,6,'d','e','f']
print("main list",list)
intlist=[i for i in list if isinstance(i,int)]
print("int list",intlist)
strlist=[j for j in list if isinstance(j,str)]
print("string list",strlist)
floatlist=[k for k in list if isinstance(k,float)]
print("float list",floatlist)

#solution to question number 5
i=1
while(i<101):
     j=1
     while(j<=(i/j)):
         if not (i%j):break
         j=j+1
     if(j>i/j): print(i,"is a prime number")
     i=i+1
 print("Bye")

#solution to question number 6
for i in range(0, 4):
    for j in range(0, i+1):
        print("* ",end="")
    print()

#solution to question number 7
di={}
di['pqr']=123
di['mno']=456
di['stu']=789
for value in di.keys():
	print(value,di[value])

#solution to question number 8

foods = ['applepie','orangepie','turkeycake']
pieless_foods =  [f for f in foods if 'pie' not in f]
print(pieless_foods)
'''
