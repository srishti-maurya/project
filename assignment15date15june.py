import re

#solution to question number 1
s = 'zuck26@facebook.com'
a="page33@google.com"
b="jeff42@amazon.com"
matchObj = re.match(r'(.*)@(.*).(com)', s, re.M|re.I)
matchObj1 = re.match(r'(.*)@(.*).(com)', a, re.M|re.I)
matchObj2 = re.match(r'(.*)@(.*).(com)', b, re.M|re.I)
print(matchObj.groups())
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.group(3) : ", matchObj.group(3))
else:
    print("No match!!")
if matchObj1:
    print("matchObj1.group() : ", matchObj1.group())
    print("matchObj1.group(1) : ", matchObj1.group(1))
    print("matchObj1.group(2) : ", matchObj1.group(2))
    print("matchObj1.group(3) : ", matchObj1.group(3))
else:
    print("No match!!")
if matchObj2:
    print("matchObj2.group() : ", matchObj2.group())
    print("matchObj2.group(1) : ", matchObj2.group(1))
    print("matchObj2.group(2) : ", matchObj2.group(2))
    print("matchObj2.group(3) : ", matchObj2.group(3))
else:
    print("No match!!")

#solution to question number 2

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
match = re.findall(r'[bB]+[a-zA-Z]+[a-zA-Z]+[a-zA-Z]',text)
print(match)

#solution to question number 3

to_be_removed=",;_"
s = "A, very very; irregular_sentence"
for c in to_be_removed:
    s=s.replace(c,' ')
s.split()
print(s)
