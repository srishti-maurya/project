
#solution to question number 1

a=3
try:
 if a<4:
    a=a/(a-3)
    print(a)
except ZeroDivisionError:
    print("this is a zero division error case!! try again")

#solution to question number 2
l=[1,2,3]
try:
    print(l[3])
except IndexError:
    print("out of index error")

#solution to question number 3
An exception
    raise NameError("Hi there")  # Raise Error
NameError: Hi there

#solution to question number 4

-5.0
a/b result in 0

#solution to question number 5
#value error
while True:
     try:
         x=int(input("Enter an integer:"))
         break
     except ValueError:
         print("this is a value error!!")
#index error
list=['s','m','i','l','e']
try:
    print(list[6])
except IndexError:
    print("this is a index error")

#module error
import sys
try:
    from exception import myexception
except Exception as e:
    print (e)
    print (sys.exc_type)

#solution to question number 6
class Error(Exception):
    pass
class AgeTooSmallError(Error):
    pass
age=18
while True:
    try:
         age_guess=int(input("Enter the age"))
         if age_guess < age:
             raise AgeTooSmallError
         break
    except AgeTooSmallError:
         print("The age is too small, try again")
print("Congratulations! You guessed the correct age")
