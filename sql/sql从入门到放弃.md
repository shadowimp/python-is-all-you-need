# SQL 语言种类

- DDL (data definition language) 数据定义语言
Create 创建
Drop 删除
Alter 修改

- DML (data manipulation language)数据操纵语言
Select 查询
Insert 插入
Update 更新
Delete 删除


product_id CHAR(4) NOT NULL ;

GROUP BY子句

GROUP BY 子句对 SELECT 语句的输出进行分组， 分组中是匹配值的数据行。 Group BY 子句支持任意表达式， 包括指定列名或列序号（从1开始）。



### 建表

CREATE TABLE table1 (ID INTEGER primary key, number int,data char(32)）

建立表格名为table1的表格，
含有ID，这个ID是唯一的关键字(primary key)，类型为整形(INTEGER )，
含有属性name，类型为整形(int)，
含有属性data，类型为32为char型

### 用表test2中的数据创建一个新表test1
create table test2 as select * from test1;


### 从其他表插入数据

Insert into table1(number,bno,data) select * from table2
插入从table2读出的所有数据插入table1。
ID是唯一关键字，会自己增加，无需插入。但是如果删除记录,则会从当前记录的ID最大值+1继续记录.

### 建立索引

create index dtin_aicode on table1(name1)

在表table上建立以name1字段的索引,索引名为dtin_aicode


### 修改表名
ALTER TABLE name RENAME TO new_name

### 用test1中的数据创建一个视图 test_view
create view  test_view as select * from test1;
视图是一个逻辑表， 可以在将来的查询中使用。视图不包含任何数据。
每当视图被其他查询语句使用时， 存储在视图中的查询语句都会被执行

### 向表test1中插入数据
insert into test1 values(16 , 25 , 'car' ) ;

插入两行：
 insert into test1 values(16 , 25 , 'car' ) ,(15 , 25, 'bus');

### 按id的顺序显示
select * from test1 order by id ;


# mysql_tutorial

### 创建一个个人表： 个人id，姓，名
```MySQL
Create table Person (PersonId int , FirstName varchar(255) , LastName varchar(255))
```

### 创建一个地址表： 地址Id ， 个人Id ， 城市 ， 州
```MySQL
Create table Address (AddressId int, PersonId int, City varchar(255), State varchar(255))
```

### 插入数据
```MySQL
Truncate table Person
Insert into Person (PersonId,Lastname , Firstname) values ('1','Wang','Allen')
Truncate table Address
Insert into Address(AddressId ,PersonId , City , State) value ( '1', '2','New York City', 'New York' )
```
The TRUNCATE TABLE statement is used to remove all records from a table in MySQL.
It performs the same function as a DELETE statement without a WHERE clause.


### question:
Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people: FirstName, LastName, City, State

``` MySQL
Select FirstName , LastName , City ,State from Person left join Address on Person.PersonId = Address.PersonId
```

### mysql查询默认不区分大小写：
select * from some_table where str=‘abc';
select * from some_table where str='ABC';
得到的结果相同。

### 区分大小写 ： 加binary字段
select * from some_table where binary str='abc'
select * from some_table where binary str='ABC'
