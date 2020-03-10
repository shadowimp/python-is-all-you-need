import sqlite3 as sq 
con = sq.connect('test.db') 
cur = con.cursor()
sql_1 = "Create table If Not Exists Student(id int ,name varchar(255),age int) " 
cur.execute(sql_1) 
sql_2 = "insert into Student(id , name , age) values (1,'jobs',45)"
cur.execute(sql_2)
print(cur.rowcount) 
cur.close()
con.commit()
con.close() 

con2 = sq.connect('test.db')
cur2 = con2.cursor() 
sql_3 = 'select * from Student' 
cur2.execute(sql_3) 
data = cur2.fetchall()
print(data) 
cur2.close() 
con2.close() 

