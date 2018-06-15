
#solution to question number 1

with open("file.txt") as f:
    n=int(input("entere the value of n"))
    lastnlines=f.readlines()[n::]
print(lastnlines)

#solution to question number 2

file=open("file.txt","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print (k, v)


#solution to question number 3

with open("file.txt") as f:
    with open("copy.txt", "w") as f1:
        for line in f:
            f1.write(line)

#solution to question number 4

with open('file.txt') as fh1, open('copy.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)


#solution to question number 5
f1=open("copy.txt",'a')
import random
res = []
def Rand(start, end, num):
    for j in range(num):
        res.append(random.randint(start, end))
    return res
num = 10
start = 1
end = 100
print(Rand(start, end, num))
for item in res:
    item=int(item)
res.sort()
print (res)
f1.writelines(["%s\n" % i for i in res])

