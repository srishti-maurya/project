#solution 1

class Circle():
  def __init__(self,radius):
    self.radius = radius
  def  getArea(self):
    return 3.14*self.radius*self.radius
  def getCircumference(self):
    return self.radius*2*3.14
x=Circle(5)

#solution 2
class Student():
  def __init__(self,name,roll):
    self.name = name
    self.roll= roll
  def display(self):
    print(self.name)
    print(self.roll)
x=Student("srishti",15)

#solution 3
class Temprature():
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)


#solution 4
class MovieDetails():
    def __init__(self,moviename,artistname,yearofrelease,rating):
        self.moviename=moviename
        self.artistname=artistname
        self.yearofrelease=yearofrelease
        self.rating=rating
    def Display(self):
        print(self.moviename)
        print(self.artistname)
        print(self.yearofrelease)
        print(self.rating)
    def Update(self):
        print(self.moviename)
        print(self.artistname)
        print(self.yearofrelease)
        print(self.rating)
x=MovieDetails("student of the year","varun dhawan",2012,3)
print(x.Display())
y=MovieDetails("I","vikram",2015,4)
print(y.Update())


#solution 5
class Expenditure():
    def __init__(self,expense,savings):
        self.expense=expense
        self.savings=savings
    def Display(self):
        print(self.expense)
        print(self.savings)
        salary=self.expense+self.savings
        return salary
x=Expenditure(15000,15000)
print(x.Display())
