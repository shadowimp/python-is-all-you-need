### Terminal 快捷键

```
control + a    jump to head 
control + e    jump to tail 
control + f    cursor forward 
control + b    cursor backward 
control + l    clear 
control + h    delete 
control + w    delete word   # 删除光标左边的一个单词
control + u    delete the front of cursor 
control + k    delete the back if cursor 
control + Y              # 粘贴前面 CTRL+u/k/w 删除过的内容
control + y    paste the delete word 
control + p    the previous command
control + n    the next command 
contril + c    结束当前命令
CTRL+_              # 撤销（undo）

CTRL+D              # 同 <Delete> ，或者没有内容时，退出会话
CTRL+R              # 历史命令反向搜索，使用 CTRL+G 退出搜索
CTRL+S              # 历史命令正向搜索，使用 CTRL+G 退出搜索

CTRL+G              # 退出当前编辑（比如正在 CTRL+R 搜索历史时）

CTRL+T              # 交换前后两个字符
CTRL+O              # 类似回车，但是会显示下一行历史
```

### 常用命令

```shell
ls /usr/bin | grep python		#列出/usr/bin  目录下 ，文p名中有python 的文件 
ls | grep *.py  #筛选出当前文件夹所有的py后缀名的文件（| 是管道操作符，grep 是过滤操作符

cp # 拷贝文件
mv # 移动文件和重命名
touch # 创建新文件
mkdir   # 创建文件夹

cd #change directory
cd -                # 回到之前的目录
pwd               # 显示当前所在目录
ps  显示当前进程

df -h   查看磁盘空间
du -h   查看当前各目录大小

history 10 #查看历史10条命令


cat #显示文件内容
stat #显示文件详细信息

head + (filename)   #show the head lines of file 

tail + (filename)    # show the tail lines of file 

大文件用 more 和 less 查看, 空格翻页 , q 退出

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

man ascii                          # 显示 ascii 表


```

###  环境

```bash
exit                # 退出当前登陆
env                 # 显示环境变量
echo $SHELL         # 显示你在使用什么 SHELL
which bash          # 搜索 $PATH，查找哪个程序对应命令 bash
whereis bash        # 搜索可执行，头文件和帮助信息的位置，使用系统内建数据库
whatis bash         # 查看某个命令的解释，一句话告诉你这是干什么的
```



### cut 截取

```bash
cut -c 1-16                        # 截取每行头16个字符
cut -c 1-16 file                   # 截取指定文件中每行头 16个字符
cut -c3-                           # 截取每行从第三个字符开始到行末的内容
cut -d':' -f5                      # 截取用冒号分隔的第五列内容
cut -d';' -f2,10                   # 截取用分号分隔的第二和第十列内容
cut -d' ' -f3-7                    # 截取空格分隔的三到七列
echo "hello" | cut -c1-3           # 显示 hel
echo "hello sir" | cut -d' ' -f2   # 显示 sir
ps | tr -s " " | cut -d " " -f 2,3,4  # cut 搭配 tr 压缩字符
```

### sort

```bash
sort file                          # 排序文件
sort -r file                       # 反向排序（降序）
sort -n file                       # 使用数字而不是字符串进行比较
sort -t: -k 3n /etc/passwd         # 按 passwd 文件的第三列进行排序
sort -u file                       # 去重排序
```

### tar

```shell
tar -zcvf file.tar.gz	# 解压文件
tar -zcvf test.tar.gz test  # 压缩文件test到test.tar.hz
```

### chmod

```shell
sudo chmod 777 + 文件名	#给每个人读和写以及执行的权限

chmod 644 {fn}      # 修改文件权限为 644，可以接 -R 对目录循环改权限
chgrp group {fn}    # 修改文件所属的用户组
chown user1 {fn}    # 修改文件所有人为 user1, chown user1:group1 fn 可以修改组
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

### Git

```shell
git status #  查看当前 git状态
git add . # 添加当前所有新增的文件
git commit -m "注释"
git push # 推送到github
```

###  常用脚本

```bash
history | awk '{a[$2]++}END{for(i in a){print a[i] " " i}}' | sort -rn | head  #列出最常使用的命令
ps aux | sort -nk +4 | tail   ## 显示前十个运行的进程并按内存使用量排序
dd if=/dev/zero of=/dev/null bs=1M count=32768 # 测试内存带宽
find /data0/yuanbo6  -type f -size +500M  #  查找目录下大于 500M 的文件
find ~ -mmin 60 -type f            # 查找 $HOME 目录中，60 分钟内修改过的文件
```

### 网络

```bash
wget {url}                # 下载文件，可加 --no-check-certificate 忽略 ssl 验证
wget -qO- {url}           # 下载文件并输出到标准输出（不保存）
curl -sL {url}            # 同 wget -qO- {url} 没有 wget 的时候使用
ping + 机器名 # 测试是否连通
```



### 定义变量

```bash
a = 1 
```

### 条件语句

```bash
for i in {1..10}; do echo $i ; done 
for (( i=1; i<10 ; i++)) ; do echo $i ; done
for file in /data0/yuanbo6/* ; do echo $file ; done  # for 循环打印某目录下面的所有文件
for loop in 1 2 3 ;do  echo $loop ; done


i=1;while [ $i -le 10 ]; do echo $i; i=$(expr $i + 1); done


# 如果存在 /root 中存在 a.txt ，则返回1 ， 否则返回0 ， if的[ ] , 前后都有空格
# linux 中 0代表条件为真，1代表为假
if [ -f /root/a.txt ]; then echo 1 ; else echo 0; fi
```

### 函数

```bash
function test {
    #函数内容
}
```

