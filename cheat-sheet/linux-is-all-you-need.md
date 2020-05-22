### Terminal 快捷键

control + a    jump to head 

control + e    jump to tail 


control + f    cursor forward 

control + b    cursor backward 


control + l    clear 


control + h    delete 

control + w    delete word 

control + u    delete the front of cursor 

control + k    delete the back if cursor 

control + y    paste the delete word 


control + p    the previous command

control + n    the next command 

```shell
ls /usr/bin | grep python		#列出/usr/bin  目录下 ，文件名中有python 的文件 
ls | grep *.py  #筛选出当前文件夹所有的py后缀名的文件（| 是管道操作符，grep 是过滤操作符

cd #change directory
ps  显示当前进程

df -h   查看磁盘空间
du -h   查看当前各目录大小

history 10 #查看历史10条命令

head + (filename)   #show the head lines of file 

tail + (filename)    # show the tail lines of file 

ll -h   # 查看文件大小,代表human 以人类的方式看内存

wc log.txt          # log文件的统计信息  
>> 3 92 598 testfile       # log文件的行数为3、单词数92、字节数598

>  # 覆盖，如果文件存在，将原来文件的内容覆盖；原文件不存在则创建文件，再添加信息
>> # 追加在后面

sed -n '16900,17900p' log.txt   # 查看log文件的16900行到17900行
sed -n '16900,17900p' log.txt >> log1.txt # 将log文件的16900行到17900行保存到log1.txt文件

nvidia-smi	# 查看GPU使用率

cat eval.log | grep '\[dev' | sort # 查找日志中包含 '\[dev'的行 并排序

cat train.tsv | cut -f 4,5,6 > train.tsv.cut # 将训练文件的4，5，6列提出来，并且存储

paste file1.txt file2.txt # 横向拼接两个文件

sort train.tsv.cut | uniq | shuf > train.tsv # 训练数据的去重和shuffle
```

### tar

```shell
tar -zcvf file.tar.gz	# 解压文件
tar -zcvf test.tar.gz test  # 压缩文件test到test.tar.hz
```

### chmod

```shell
sudo chmod 777 + 文件名	#给每个人读和写以及执行的权限
```

### tmux 

cntrol + B +D    退出tmux界面

```shell
tmux new -s zyb      #新建名为zyb的tmux
tmux at -t zyb    # 进入名为zyb的tmux
```

### date

```shell
date -d "-1days" +%Y-%m-%d  #显示日期 形式 ： 2020-04-02
```

### ssh

```bash
#ssh 不掉线,服务器切换到root账户，在/etc/ssh/ssh_config里加入
ServerAliveInterval 30
ServerAliveCountMax 720
# 客户端每隔 30 秒向服务端发送消息保持会话连接，累积 720 次以后服务端依然没有回应，就断开连接。这样配置可以使连接保持 6 小时（720 * 30 = 21600 秒）
```

### crontab

```shell
0 11 * * *   # 每天11点执行
sudo service crond restart 	#重启crontab服务
```

### docker

```shell
docer run -it -v $PWD:/work centos: latest /bin/bash     #docker启动centos
```

### mysql

```shell
brew services start mysql		# 启动mysql
mysql -uroot -p	#以root方式进入mysql
```

### rsync

```shell
vi /etc/rsyncd.conf

rsync -av test.py 10.41.24.195::yuanbo6
#rsync -av 源目录 目的地目录
```



