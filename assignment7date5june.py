#solution to question number 1
'''
def area(r):
    ar = 4*3.14*r*r
    return ar
r = int(input("enter the radius"))
print("The area of square is:",area(r))


#solution to question number 2
def div(x):
    return [y for y in range(1, int(x / 2) + 1) if x % y == 0]
def perfect(a, b):
    return [x for x in range(a, b + 1) if sum(div(x)) == x]
print(perfect(1, 1000))


#solution to question number 3
def mul(n, i=1):
    print (n*i)
    if i != 10:
        mul(n,i+1)
mul(12)


#solution to question number 4
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))
'''

#solution to question number 5
Dict={}
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
Dict.update({n:factorial(n)})
print(Dict)
