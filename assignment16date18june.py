#solution 1
'''
import pymysql
try:
    connection = pymysql.connect(host='localhost', database='demo', user='srishti')
    print(connection)
finally:
    connection.close()
    print('Done!!')


import pymysql as pm
try:
    con = pm.connect(host='localhost', database='demo', user='srishti')
    cursor = con.cursor()
    query1 = 'create table book(Book_ID int(5) primary key, Title_ID int(5), location varchar(10), genre varchar(10) '
    query2 = 'create table titles(Title_ID int(5) , Title varchar(15), ISBN varchar(10), publisher_id int(5), publication_year int(4), foreign key(Title_ID) references book(Book_ID)'
    query3 = 'create table publishers(publisher_ID int(5) , name varchar(10), street_address varchar(10), suite_number int(5), zip_code_id int(4), foreign key(publisher_id) references titles(Title_ID)'
    query4 = 'create table zipcodes(zip_code_ID int(5) , city varchar(15), state varchar(10), zip_code int(5), foreign key(zip_code_ID) references book(publisher_id)'
    query5 = 'create table authorstitles(authortitleid int(5) , authorid int(5), Title_id int(5), foreign key(Title_id) references titles(Book_ID)'
    query6 = 'create table authors(authorid int(5) , firstname varchar(15), middlename varchar(10), lastname varchar(10), foreign key(authorid) references authortitles(authortitleid)'
    cursor.execute(query1)
    print('Table 1 created successfully!!')
    cursor.execute(query2)
    print('Table 2 created successfully!!')
    cursor.execute(query3)
    print('Table 3 created successfully!!')
    cursor.execute(query4)
    print('Table 4 created successfully!!')
    cursor.execute(query5)
    print('Table 5 created successfully!!')
    cursor.execute(query6)
    print('Table 6 created successfully!!')
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('Done!!')

#solution 2
import pymysql as pm
try:
    con = pm.connect(host='localhost', database='demo', user='srishti')
    cursor = con.cursor()
    query1 = 'insert into book(Book_ID , Title_ID , location , genre '\
    values(%s, %s, %s, %s, %s)"
    records1 = [(1, 'abc', 23, 23000),
               (2, 'def', 24, 20000),
               (3, 'ghi', 50, 100000)]
    cursor.executemany(query1, records1)
    query2 = 'insert into titles(Title_ID , Title , ISBN , publisher_id , publication_year'\
    values(%s, %s, %s, %s, %s)"
    records2 = [(1, 'abc', 23, 23000,2000),
               (2, 'def', 24, 20000,2001),
               (3, 'ghi', 50, 100000,2002)]
    cursor.executemany(query2, records2)
    query3 = 'insert into publishers(publisher_ID , name , street_address , suite_number , zip_code_id '\
    values(%s, %s, %s, %s, %s, %s)"
    records3 = [(1, 'abc', 'xyz',23, 23000),
               (2, 'def', 'pqr',24, 20000),
               (3, 'ghi', 'stu',50, 100000)]
    cursor.executemany(query3, records3)
    query4 = 'insert into zipcodes(zip_code_ID , city, state, zip_code'\
    values(%s, %s, %s, %s)"
    records4 = [(1, 'abc', 23, 23000),
               (2, 'def', 24, 20000),
               (3, 'ghi', 50, 100000)]
    cursor.executemany(query4, records4)
    query5 = 'insert into authorstitles(authortitleid , authorid, Title_id'\
    values(%s, %s, %s)"
    records1 = [(1, 23, 23000),
                (2, 24, 20000),
                (3, 50, 100000)]
    cursor.executemany(query5, records5)
    query6 = 'insert into authors(authorid, firstname, middlename , lastname'\
    values(%s, %s, %s, %s)"
    records1 = [(1, 'abc', 'abc','abc'),
                (2, 'def', 'abc','abc'),
                (3, 'ghi', 'abc','abc')]
    cursor.executemany(query6, records6)
    con.commit()
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
finally:
     if cursor:
         cursor.close()
     if con:
         con.close()
     print('Done!!')
'''
#solution3
# import pymysql as pm
#
# try:
#     con = pm.connect(host='localhost', database='demo', \
#                      user='srishti')
#
#     cursor = con.cursor()

#     query = 'select * from book'
#
#     cursor.execute(query)
#
#     data = cursor.fetchall()
#
#     for row in data:
#         print('Book_ID: {}, Title_ID: {}, location: {}, genre: {}' \
#               .format(row[0], row[1], row[2], row[3]))
#
#     query = "update book set Book_id=15 where Title_ID = 'abc'"
#
#     cursor.execute(query)
#    cursor = con.cursor()

#     query = 'select * from book'
#
#     cursor.execute(query)
#
#     data = cursor.fetchall()
#
#     for row in data:
#         print('Book_ID: {}, Title_ID: {}, location: {}, genre: {}' \
#               .format(row[0], row[1], row[2], row[3]))
#     con.commit()
#
# except pm.DatabaseError as e:
#     if con:
#         con.rollback()
#         print('Problem occured: ', e)
#
# finally:
#     if cursor:
#         cursor.close()
#     if con:
#         con.close()
#     print('Done!!')
