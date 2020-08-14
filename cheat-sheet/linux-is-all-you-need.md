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


i # 进入编辑模式
x #删除一个字符
r #替换一个字符

```

### 常用命令

```shell
ls /usr/bin | grep python		#列出/usr/bin  目录下 ，文p名中有python 的文件 
ls | grep *.py  #筛选出当前文件夹所有的py后缀名的文件（| 是管道操作符，grep 是过滤操作符
ll -t 	# 按修改时间排序

cp # 拷贝文件
mv # 移动文件和重命名
touch # 创建新文件
mkdir   # 创建文件夹
mkdir -p  #递归创建目录，即使上级目录不存在，会按目录层级自动创建目录

cd #change directory
cd -                # 回到之前的目录
pwd               # 显示当前所在目录
ps  显示当前进程

df -h   查看磁盘空间
du -h   查看当前各目录大小

history 10 #查看历史10条命令


cat #显示文件内容
cat -n	# 打印内容的同时，打印行号

# 文件去重
cat keywords_pusou.txt |sort|uniq >  keywords_pusou1.txt

# 当前目录下的所有文件合并
cat * > log.txt
cat data/* > log.txt  # 将data0目录下的所有文件合并

stat #显示文件详细信息
file {fn}           # 检测文件的类型和编码

head + (filename)   #show the head lines of file 

tail + (filename)    # show the tail lines of file 

大文件用 more 和 less 查看, 空格翻页 , q 退出

ll -h   # 查看文件大小,代表human 以人类的方式看内存

wc log.txt          # log文件的统计信息  
>> 3 92 598 testfile       # log文件的行数为3、单词数92、字节数598
wc -l # 只显示行数

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

# 建立文件的软连接 , 都要写绝对路径
ln -s 源文件 目标文件
ls -al user.dict.utf8 # 查看软连接的真实源文件



sleep 3 #睡眠3秒
```

###  环境

```bash
exit                # 退出当前登陆
env                 # 显示环境变量
echo $SHELL         # 显示你在使用什么 SHELL
which bash          # 搜索 $PATH，查找哪个程序对应命令 bash
whereis bash        # 搜索可执行，头文件和帮助信息的位置，使用系统内建数据库
whatis bash         # 查看某个命令的解释，一句话告诉你这是干什么的
uname -a                  # 查看内核版本等信息

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
tmux ls	# 查看目前开启的tmux
tmux kill-session -t session-name # 关闭session
tmux rename-session -t old-name new-name # session 重命名
```

### date

```shell
date -d "-1days" +%Y-%m-%d  #显示日期 形式 ： 2020-04-02

date                      # 显示日期
date +%Y%m%d							# 20200716
date +%Y_%m_%d%t%H:%M:%S	# 2020_07_16	17:10:15
date -d 'last day' #昨天
date -d 'next day' #明天
date -d '-2 day ago' #两天后
DT=`date -d 'last day' +%Y%m%d`
DT2=`date -d '-2 days' +%Y%m%d` # 两天前

DT7 = `date -d '-7 days' +%Y%m%d` #七天前

cal                       # 显示日历
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

git的工作流

工作区：即自己当前分支所修改的代码，git add xx 之前的！不包括 git add xx 和 git commit xxx 之后的。

暂存区：已经 git add xxx 进去，且未 git commit xxx 的。

本地分支：已经git commit -m xxx 提交到本地分支的。

```shell
git status #  查看当前 git状态
git add . # 添加当前所有新增的文件
git commit -m "注释"
git push # 推送到github


git config --list #  显示当前的Git配置

git log # 查看所有提交历史
git log –p my_file # 查看某文件的提交历史

git branch yuanbo6	#创建分支yuanbo6
git checkout yuanbo6	#切换到分支yuanbo6
git push origin branchname	#将分支yuanbo6上的代码push上去

git push origin master

# 撤销，代码回滚
# 代码还未add
git checkout -- a.txt   # 丢弃某个文件， 撤销修改
git checkout -- .   #丢弃全部文件，新增的文件会被删除、删除的文件会恢复回来、修改的文件会回去。

# 文件git add到缓存区，并未commit提交
git reset HEAD a.txt	# 取消暂存 
git reset HEAD .   # 这个命令仅改变暂存区，并不改变工作区，

# git commit到本地分支、但没有git push到远程
git reset --hard	# 重置暂存区与工作区，与上一次 commit 保持一致
git reset --hard commit_id 	# 将代码回滚到当前commit_id的版本
git reset --hard HEAD^  # 回到最新的一次提交

# 已经用 git push把修改提交到远程仓库
git reset --hard <commit_id>
git push origin HEAD --force # 强制提交一次，之前错误的提交就从远程仓库删除



git stash	# 将目前改动的代码暂存起来
git pull origin master	# 从master拉代码
git stash pop	# 将之前的暂存改动与master上的代码合并， 并删除暂存的stash内容
git stash apply# 恢复，恢复后，stash内容并不删除，你要使用命令git stash drop来删除


git revert # 放弃指定提交的修改，但是会生成一次新的提交，需要填写提交注释，以前的历史记录都在；
```

###  常用脚本

```bash
history | awk '{a[$2]++}END{for(i in a){print a[i] " " i}}' | sort -rn | head  #列出最常使用的命令
ps aux | sort -nk +4 | tail   ## 显示前十个运行的进程并按内存使用量排序
dd if=/dev/zero of=/dev/null bs=1M count=32768 # 测试内存带宽
find /data0/yuanbo6  -type f -size +500M  #  查找目录下大于 500M 的文件
find ~ -mmin 60 -type f            # 查找 $HOME 目录中，60 分钟内修改过的文件
find . -type f -newermt "2020-05-01"  #按日期范围查找文件
```

### 网络

```bash
wget {url}                # 下载文件，可加 --no-check-certificate 忽略 ssl 验证
wget -qO- {url}           # 下载文件并输出到标准输出（不保存）
curl -sL {url}            # 同 wget -qO- {url} 没有 wget 的时候使用
ping + 机器名 # 测试是否连通

ssh user@host             # 以用户 user 登陆到远程主机 host
ssh -p {port} user@host   # 指定端口登陆主机
ssh-copy-id user@host     # 拷贝你的 ssh key 到远程主机，避免重复输入密码
scp {fn} user@host:path   # 拷贝文件到远程主机
scp user@host:path dest   # 从远程主机拷贝文件回来
scp -P {port} ...         # 指定端口远程拷贝文件

sz {file}                 # 发送文件到终端，zmodem 协议
rz                        # 接收终端发送过来的文件


#ssh 不掉线,服务器切换到root账户，在/etc/ssh/ssh_config里加入
ServerAliveInterval 30
ServerAliveCountMax 720
# 客户端每隔 30 秒向服务端发送消息保持会话连接，累积 720 次以后服务端依然没有回应，就断开连接。这样配置可以使连接保持 6 小时（720 * 30 = 21600 秒）


curl 不带有任何参数时，curl 就是发出 GET 请求，服务器返回的内容会在命令行输出。
http://www.ruanyifeng.com/blog/2019/09/curl-reference.html

-H参数直接指定标头，更改User-Agent
curl -H 'User-Agent: php/1.0' https://google.com

curl -d '{"login": "emma", "pass": "123"}' -H 'Content-Type: application/json' https://google.com/login
# HTTP 请求的标头是Content-Type: application/json，然后用-d参数发送 JSON 数据
# 并且会自动将请求转为 POST 方法，因此可以省略-X POST

curl -b 'foo=bar' https://google.com 	#-b 参数 发送 Cookie到服务器	
curl -b cookies.txt https://www.google.com

curl -c cookies.txt https://www.google.com	#-c参数 cookie写入文件

curl -X POST https://google.com/login -d 'login=emma＆password=123' 	
# -d 参数发送 POST 请求的数据体，-X 参数指定 HTTP 请求的方法

-u参数用来设置服务器认证的用户名和密码
curl -u 'bob:12345' https://google.com/login
```

### 定义变量

```bash
a = 1 
echo $varname             # 查看变量内容
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
function fun1 () { echo 'a' }

unset -f fun1  # 删除函数

declare -f                # 查看所有函数
```

### 进程



```bash
ps                        # 查看当前会话进程
ps -e                  # 查看所有进程

ps -u {user}              # 查看某用户进程

ps aux | grep httpd       # 查看名为 httpd 的所有进程

ps -ef | grep search_ad.go	#查看名为search_ad.go 的所有进程

pstree                    # 树形列出所有进程，pstree 默认一般不带，需安装

kill {pid}                # 结束进程

top                       # 查看最活跃的进程
top -u {user}             # 查看某用户最活跃的进程


# 后台运行 
nohup go run search_ad.go & 
nohup 加在一个命令的最前面，表示不挂断的运行命令
&  # 表示放在后台执行，即使terminal（终端）关闭，或者电脑死机程序依然运行

 jobs  #查看后台运行的命令

ps -ef|grep test.sh  # 查找名为test.sh的进程
 
 2>&1 # 这个意思是把标准错误（2）重定向到标准输出中（1）而标准输出又导入文件output里面，所以结果是标准错误和标准输出都导入文件output里面了 。可以很好的将错误信息保存，帮助我们定位问题。
 
  
 test.sh  > log.txt 2>&1 	#  将test.sh的输出重定向到log.txt文件中，同时将标准错误也重定向到log.txt文件中
 
 0：标准输入流 stdin
1：标准输出流 stdout
2：标准错误流 stderr

```

### 用户管理

```bash
vmstat                    # 显示内存和 CPU 使用情况
free                      # 显示内存和交换区使用情况
df                        # 显示磁盘使用情况
uname                     # 显示系统版本号
hostname                  # 显示主机名称
whoami              # 显示我的用户名
who                 # 显示已登陆用户信息，w / who / users 内容略有不同
su                  # 切换到 root 用户
sudo {command}      # 以 root 权限执行某命令
```

### 文本处理 - awk / sed

```bash	
awk '{pattern + action}' {filenames}
# 默认以空格为分隔， 自定义分割符加 -F 参数

awk '{a+=$2}END{print a}'	#对文件的第二列求和

awk -F,  '{sum += $3};END {print sum}' test	#求文件test第三列的和

head lol.txt | awk '{print $1}'		# 打印 lol.txt head的第一列 
awk '{print $5}' file              # 打印文件中以空格分隔的第五列 ,从1开始而不是0

awk -F ',' '{print $5}' file       # 打印文件中以逗号分隔的第五列
awk -F ',' '{print $NF}' file      # 打印逗号分隔的文件中的每行最后一列

awk '/str/ {print $2}' file        # 打印文件中包含 str 的所有行的第二列
awk '{s+=$1} END {print s}' file   # 计算所有第一列的合
awk 'NR%3==1' file                 # 从第一行开始，每隔三行打印一行


sed -n '2p' file                   # 打印文件第二行
sed -n '2,5p' file                 # 打印文件第二到第五行

sed 's/find/replace/' file         # 替换文件中首次出现的字符串并输出结果
sed '10s/find/replace/' file       # 替换文件第 10 行内容
sed '10,20s/find/replace/' file    # 替换文件中 10-20 行内容
sed -r 's/regex/replace/g' file    # 替换文件中所有出现的字符串
sed -i 's/find/replace/g' file     # 替换文件中所有出现的字符并且覆盖文件
sed '/line/s/find/replace/' file   # 先搜索行特征再执行替换
sed -e 's/f/r/' -e 's/f/r' file    # 执行多次替换
sed 's#find#replace#' file         # 使用 # 替换 / 来避免 pattern 中有斜杆
sed -i -r 's/^\s+//g' file         # 删除文件每行头部空格
sed '/^$/d' file                   # 删除文件空行并打印
sed -i 's/\s\+$//' file            # 删除文件每行末尾多余空格

```

```bash
# 统计词频
cat words.txt | tr -s ' ' '\n'|sort|uniq -c |sort -r|awk '{print $2" "$1}'

cat ——浏览文件
tr -s ——替换字符串（空格换为换行）保证了一行一个单词
sort ——默认ASCII值排序，排序号后还会有重复
uniq —— 去重，-c再输出重复次数。结果就是 ”4 abc“ abc出现了4次
sort -r —— 反向排序，也就是从大到小。得到按频率高低的结果
awk ——格式化输出，规定输出是先字符串再重复次数，所以先$2再$1，中间空格分隔
```

### wrk2 压测工具

```bash
git clone https://github.com/giltene/wrk2.git
cd wrk2 && make
./wrk -t2 -c100 -d30s -R2000 http://www.baidu.com

```

### 正则表达式

```bash
\w 	匹配一个常用字符，包括字母、数字、下划线
\s  匹配空格	
\d	数字,qual to [0-9]
. 可以匹配任意字符
^ 开头
& 结尾
{10}	重复10次
{5, 10}	重复5-10次
{5, }	重复5次以上

匹配4位数字的号码：
^\d\d\d\d$

匹配1开头11位数字的手机号码：
 ^1\d{10}$
 
 数字1-9或字母a-e
 [1-9a-e]

将字母换成大写，就表示相反的意思。用 \d 你可以匹配一个数字，\D 则表示匹配一个非数字


+ 表示 至少匹配出现一次的字符。它等价于 {1,} , "d+"  匹配任意的数字
```

### shell处理json

```bash
sudo yum install -y jq	#下载安装jq
echo '{"key": "syw"}' | jq '.key'
echo '{"key": {"key2": "val"}}' | jq '.key.key2'
echo '{"key": {"key2": ["val1", "val2"]}}' | jq '.key.key2[1]'
```



