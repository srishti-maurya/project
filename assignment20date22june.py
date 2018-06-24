import pandas as pd
#solution 1
'''
data = {'name':['tom','james','ricky','vin'],
        'age':[20,21,22,23],
        'mail_id':['tom12@gmail.com','james123@yahoo.com','ricky123@gmail.com','vin123@gmail.com'],
        'phone_num':['123','456','789','521']}
df=pd.DataFrame(data)
df.loc[4]=['jim',24,'jim123@yahoo.com','951']
print(df)
'''
#solution 2
df=pd.read_csv('weather.csv',header=None)
print(df)
print(df.head(5))
print(df.head(10))
print(df['MaxTemp'].mean())
print(df.tail(5))
print(df['MinTemp'].mean())
