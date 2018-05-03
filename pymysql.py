import pymysql
# Connect to the database
con = pymysql.connect(host='localhost',user='root',password='12345',db='mydata')
cur = con.cursor()
# 构建Mysql : >> Create table If Not Exists Custormers(Id int, Name varchar(255))
sql = 'insert into Customers(Id,Name) values ('1','joe')'.
cur.execute(sql)
data = cur.fetchone() # 取查询结果的一行
print(data)
conn.close()


#四部：连接，游标数据库，执行，取数


