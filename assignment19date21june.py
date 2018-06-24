import numpy as np
#solution 1
random_num1=np.random.rand(10,1)
print(random_num1)
mean_num=np.mean(random_num1)
print(mean_num)
#solution 2
random_num2=np.random.rand(20,1)
print(random_num2)
standard_deviation=random_num2.std()
print(standard_deviation)
variance=random_num2.var()
print(variance)
#solution 3
arrayA=np.random.random((10,20))
arrayB=np.random.random((20,25))
array_multi=np.multiply(arrayA,arrayB)
print(array_multi)
array_sum=np.add(array_multi)
print(array_sum)
#solution 4
arrayA=np.random.rand((10,1))
print(arrayA)
def func(x):
    return (1/(1+np.exp(-x)))
result=np.apply_along_axis(func,0,arrayA)
print(result)
