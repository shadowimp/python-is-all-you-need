## SQL 

### 操作数据库

```mysql
Create 创建数据库或表
# 建db
create database shop; # 创建名为shop的数据库

Drop 删除
Alter 修改

# 修改表名
ALTER TABLE name RENAME TO new_name  

truncate 清空一张表

# 删除表
DROP TABLE ads_lv3_hash

# TRUNCATE TABLE 快速清空一个表m,数据无法找回
TRUNCATE TABLE table_name


show databases;   #显示数据库列表 
use database d1;  #进入数据库
show tables;  		#显示数据库中所有的表
desc tabl_name;		#描述表结构


GRANT 授权

ROLLBACK 回滚


# 授予权限
grant select on table table_name_1 to user user_name;

# 撤回权限
revoke select on table table_name_1 to user user_name;


```

### 操作表

```mysql
Select 查询
Insert 插入
Update 更新
Delete 删除

delete 是一行一行删的，可以恢复，无法释放磁盘空间

update table_name set 

product_id CHAR(4) NOT NULL ;
```

### 建表

```mysql
CREATE TABLE table_name1  (word string comment '名字', hash_number string comment 'hash值'）  
# comment 添加注释                          

double # 小数
                           
# 建表 设置partition 和 列间的分隔符                           
create table if not exists table_name1 (word string, hash_number string, class string) PARTITIONED BY (dt string) row format delimited fields terminated by '\t';                           
```

```mysql
CREATE TABLE table1 (ID INTEGER primary key, number int,data char(32)）
建立表格名为table1的表格，
含有ID，这个ID是唯一的关键字(primary key)，类型为整形(INTEGER )，
含有属性name，类型为整形(int)，
含有属性data，类型为32为char型
create table if not exists customers (id int, name varchar(255))

create table test2 as select * from test1;	# 用表test2中的数据创建一个新表test1
```

### Insert

```mysql
insert into test1 values(16 , 25 , 'car' ) ; #向表test1中插入数据
insert into test1 (ID,number,data) values (16,25,'car')

插入两行：
insert into test1 values(16 , 25 , 'car' ) ,(15 , 25, 'bus');

### 从其他表插入数据
Insert into table1(number,bno,data) select * from table2
插入从table2读出的所有数据插入table1。
ID是唯一关键字，会自己增加，无需插入。但是如果删除记录,则会从当前记录的ID最大值+1继续记录.


insert into：直接向表或静态分区中插入数据。您可以在insert语句中直接指定分区值，将数据插入指定的分区。如果您需要插入少量测试数据，可以配合VALUES使用。
insert overwrite：先清空表中的原有数据，再向表或静态分区中插入数据。

```

### Select 

```mysql
select * from city where population >100000 and countrycode = 'USA' 

select name from employee order by name   #按名字的字母顺序排序

select * from test1 order by id, name ;	# 先按id的顺序显示,后按name

select name from employee where salary > 2000 and months <10 order by employee_id asc 
# 按employee_id排序 ，  desc 降序

ROUND(price,1) # price 保留一位小数
ROUND(price,-1) # price 舍弃个位

LEFT(name,2)  # 返回name 的前两个字符

<> # !=

# 统计行数
select count(*) from ads_lv3_hash where dt = '20201204';

# 求和
select sum(population) from world where continent='Europe'

# 查找时去重  DISTINCT
select DISTINCT continent from world	

CONCAT_WS(separator, str1, str2,...) 
# 第一个参数剩余参数间的分隔符
select CONCAT_WS(name,age) 

select 嵌套 用as设定新表名
select name from (select * from student where age=16) as t1 where score >90;

# as 
SELECT a.created_at AS time from table1 a;

```

### GROUP BY

-   GROUP BY 对 SELECT 语句的输出进行分组， 分组中是匹配值的数据行。 Group BY 子句支持任意表达式， 包括指定列名或列序号（从1开始）。

-   GROUP BY 常与COUNT连用，用于统计每组的个数

-   GROUP BY的结果是无序的

-   #### group by 必须出现在where之后 order by 之前

```mysql
SELECT type, COUNT(*) FROM Product GROUP BY type

如何对分组后的结果进行查询？
关键字：group_concat()
select department,group_concat(name),count(*) from employee group by department;

Hive不允许直接访问非group by字段,对于非group by字段，可以用Hive的collect_set函数收集这些字段，返回一个数组；.使用数字下标，可以直接访问数组中的元素；

Hive中collect相关的函数有collect_list和collect_set。
它们都是将分组中的某列转为一个数组返回，不同的是collect_list不去重而collect_set去重。

```

### Having

WHERE是对数据表直接查询，只有having能对聚合的数据指定条件, having 在group by 后面使用,

使用HAVING的时候，只用在跟GROUP BY相关结果的处理上。

HAVING从筛选的结果再筛选，WHERE直接筛选

```mysql
SELECT type,AVG(price) FROM Product GROUP BY type HAVING AVG(price) > 200
# avg 计算每种type的平均价格
```

### Like

```mysql
# 找以Y开头的名字
SELECT name FROM world WHERE name LIKE 'Y%'
```



### 建立索引和视图

```mysql
create index dtin_aicode on table1(name1) #在表table上建立以name1字段的索引,索引名为dtin_aicode

create view  test_view as select * from test1;	#用test1中的数据创建一个视图 test_view
视图是一个逻辑表， 可以在将来的查询中使用。视图不包含任何数据。
每当视图被其他查询语句使用时， 存储在视图中的查询语句都会被执行
```

### 修改

```mysql
ALTER TABLE name RENAME TO new_name
```



### nvl

```mysql
NVL（表达式1，表达式2）
如果表达式1为空值，NVL返回值为表达式2的值，否则返回表达式1的值

NVL2(表达式1，表达式2，表达式3）
如果表达式1为空，返回值为表达式3的值。如果表达式1不为空，返回值为表达式2的值。
     
     
if (a is not null, 1, 0) as label 
```







## mysql_tutorial

### 创建一个person表： 包括个人id，姓，名
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



### mysql

```shell
brew services start mysql		# 启动mysql
mysql -uroot -p	#以root方式进入mysql
```



### Hive

```bash
hive -e 'select * from  ods_dim_tblog_obj_info_adv where dt=20200520;' > hot_lv3_20200520.txt
```

### Hadoop

```bash
hadoop fs -ls # 列出指定目录下的内容
hadoop fs -lsr  # 递归列出该路径下所有子目录信息
hadoop fs -copyFromLoca /opt/test/xx.zip  /user/data #从本地系统拷贝文件到dfs中
hadoop fs -cat  /user/wcinput/wc.input # 显示文件内容
hadoop fs -copyToLocal /user/input/小王子.txt /opt/download/tonghua.txt #从hdfs拷贝到本地
hadoop fs -df -h  # 统计文件系统的可用空间信息
hadoop fs -du -s -h # 统计文件夹的大小信息


hadoop fs -get
```



### 向hive表中插入数据，从文件中导入

```mysql
load data local inpath 'data_path' overwrite into table table_name1 partition (dt = '20201204');  

# 多 partition
load data local inpath 'data_path' overwrite into table table_name1  partition ( dt = '2018-05-27',hour = '14' );

# 定义行分割方式
load data local inpath 'data_path' overwrite into table table_name1 row format delimited fields terminated by '\t';                           
                         
```



## redis

```python
import redis

redis_conn = redis.Redis(host='127.0.0.1', port= 6379, password= 'your pw', db= 0)
```



### 常用函数

```mysql
ROUND(data) # 数据限制小数位数
CONCAT(data,'%')  # 连接 % 在data后

```



### 事务 Transaction

是需要在同一个处理单元中执行的一系列更新处理的集合

```mysql
start transaction;
dml_1
dml_2
commit;
```

### date

```mysql
select curdate()  # 当天日期  
select CURRENT_DATE
>>2021-07-17

select DATE_SUB(curdate(),INTERVAL 1 DAY)  # 昨天
>> 2021-07-16 


select CURRENT_TIME  # 当前时间
>> 17:10:11 

select CURRENT_TIMESTAMP # 当前日期和时间
2021-07-17 17:17:12

select CAST('20091214' AS DATE) # 字符串类型转换为日期类型




```

