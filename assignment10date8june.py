#solution 1
'''
class animal:
    def animal_attribute(self):
        print("this is animal attribute")
class tiger(animal):
    def tiger_attribute(self):
        print("this is tiger attribute")
tigerobj=tiger()
tigerobj.animal_attribute()
tigerobj.tiger_attribute()

#solution 2
A A
A B
'''

#solution 3
class cop:
    def __init__(self,name,age,work,experience,designation):
        self.name=name
        self.age=age
        self.work=work
        self.experience=experience
        self.designation=designation
    def display(self,name,age,work,experience,designation):
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.designation)
    def update(self,name,age,work,experience,designation):
        self.name = 'bob'
        self.age = 40
        self.work = 'ceo'
        self.experience = 6
        self.designation = 'head'
        print("updated data:")
        print(self.name)
        print(self.age)
        print(self.work)
        print(self.experience)
        print(self.designation)
class mission(cop):
    def __init(self):
        super(mission,self).__init__()
    def __init__(self,details):
        self.details=details
    def add_method_details(self,details):
        return self.details
    def display1(self,details):
        print(self.details)
obj = mission('sherlock',35,'manager',5,'design')
obj.add_method_details('secret')
obj.display1('secret')
obj.display('sherlock',35,'manager',5,'design')
obj.update()


'''
#solution 4
class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self,length,breadth):
        ar=self.length*self.breadth
        print("Area is:",ar)
    def sha(self):
        print("this is shape class")
class rectangle(shape):
    def rect(self):
        print("this is rectangle class")
class square(rectangle):
    def squ(self):
        print("this is square class")
x=rectangle(5,9)
x.rect()
x.area(5,9)
y=square(6,6)
y.squ()
y.area(6,6)
'''


