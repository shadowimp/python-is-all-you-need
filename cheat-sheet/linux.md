### 常用命令

```shell
# 目录
ls /usr/bin | grep python		#列出/usr/bin  目录下 ，文p名中有python 的文件 
ls | grep *.py  #筛选出当前文件夹所有的py后缀名的文件（| 是管道操作符，grep 是过滤操作符
ll -t 	# 按修改时间排序
ll -h  # 列出文件和文件大小

cd #change directory
cd -                # 回到之前的目录
pwd               # 显示当前所在目录

history 10 #查看历史10条命令



cat #显示文件内容
cat -n	# 打印内容的同时，打印行号
大文件用 more 和 less 查看, 空格翻页 , q 退出


# 创建 移动 复制 删除

cp # 拷贝文件
cp  -r # 拷贝文件夹
cp -r dir1 dir2 # 表示将dir1及其dir1下所包含的文件复制到dir2下

mv # 移动文件和重命名
touch # 创建新文件
mkdir   # 创建文件夹
mkdir -p  #递归创建目录，即使上级目录不存在，会按目录层级自动创建目录


# 查找
grep -r message ./  #递归的查找当前目录下包含字符串message 的文件




# 文件去重
cat keywords_pusou.txt |sort|uniq >  keywords_pusou1.txt
sort train.tsv.cut | uniq |  > train.tsv # 训练数据的去重
awk ' !x[$0]++'  test_file # 去重不改变顺序

# 将文件打乱
shuf input_file.txt -o output_file.txt

# 当前目录下的所有文件合并
cat * > log.txt
cat data/* > log.txt  # 将data0目录下的所有文件合并

stat #显示文件详细信息
file {fn}           # 检测文件的类型和编码

head + (filename)   #show the head lines of file 

tail + (filename)    # show the tail lines of file 
tail -f  #能显示还在更新的文件



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





# 建立文件的软连接 , 都要写绝对路径
ln -s 源文件(磁盘存储空间大的,先创建好文件夹) 目标文件(空间小的,相当与快捷方式,目前不存在)
ls -al user.dict.utf8 # 查看软连接的真实源文件
正确删除 软连接 最安全的方式是使用 命令unlink
unlink 目标文件


sleep 3 #睡眠3秒


tail /var/log/messages  # 程序被kill，查看linux 系统日志

man ascii                          # 显示 ascii 表

md5sum yuanbo.txt 	# md5校验文件的唯一性


# 查找
grep -rn "Hello" ./  #查找当前目录下包含"Hello"的文件



### shell 变量
定义shell变量，变量名和等号之间不能有空格
your_name="pony"

使用shell变量，添加美元符号，使用或不使用括号均可
echo $your_name
echo ${your_name}

# 字符串长度
string="abcd"
echo ${#string} #输出 4

# 字符串切片
string="apple"
echo ${string:0:3}
>>app


# 多行注释
:<<!
注释内容...
注释内容...
注释内容...
!

# 数组
array_name=(value0 value1 value2 value3)

${array_name[n]}

# 数组长度
${#array_name[*]}


## && , &
& 表示任务在后台执行
&&  两条命令间使用，前一条执行完后再执行后一条命令  echo '1' && echo '2'

｜ 上一条命令的输出作为下一条命令的输入 echo 'yes'|wc -l
||  上一条命令执行失败后 才会执行下一条命令


test -e #文件是否存在

dirname test.py  # 返回文件的目录名

```

###  环境

```bash
exit                # 退出当前登陆
env                 # 显示环境变量
echo $SHELL         # 显示你在使用什么 SHELL
which bash          # 搜索 $PATH，查找哪个程序对应命令 bash
whereis bash        # 搜索可执行，头文件和帮助信息的位置，使用系统内建数据库
whatis bash         # 查看某个命令的解释，一句话告诉你这是干什么的
uname -a            # 查看内核版本等信息

df -h   						# 查看磁盘空间使用情况
df -i 							# 查看文件节点数(inode文件索引占用)

sudo du -h --max-depth=1   # 查看当前目录下每个文件夹占用的大小

sudo du -h --max-depth=0 yuanbo6 # 查看yuanbo6目录的大小

sudo du -s /usr/home/* |sort -nr|head # /usr/home/ 下文件夹的大小，按顺序排列
du -sh ./*  # 获得当前文件夹下所有文件和文件夹的大小，使用
du -h   						#查看当前各目录大小 disk usage
du -s -h						# 查看当前目录总共占的存储空间
vmstat              # 显示内存和 CPU 使用情况
free                # 显示内存和交换区使用情况
uname               # 显示系统版本号
hostname            # 显示主机名称
hostname -i					# 显示机器ip
mip=$(hostname -i|awk -F '.' '{print $4}') 


whoami              # 显示我的用户名
who                 # 显示已登陆用户信息，w / who / users 内容略有不同
su                  # 切换到 root 用户
sudo {command}      # 以 root 权限执行某命令
```

### 进程

```bash
ps                        # 当前会话进程
ps -aux 									# 显示所有进程
ps -e                  		# 查看所有进程

ps -u {user}              # 查看某用户进程

ps aux | grep httpd       # 查看名为 httpd 的所有进程

ps -ef | grep search_ad.go	#查看名为search_ad.go 的所有进程
ps -ef| grep test.sh  # 查找名为test.sh的进程

pstree                    # 树形列出所有进程，pstree 默认一般不带，需安装

kill {pid}                # 结束进程

top                       # 查看最活跃的进程
top -u {user}             # 查看某用户最活跃的进程

jobs  #查看后台运行的命令


# 后台不挂断运行(no hang up) nohup 加在一个命令的最前面，表示不挂断的运行命令
nohup go run search_ad.go & 
&  # 表示放在后台执行，即使terminal（终端）关闭，或者电脑死机程序依然运行
默认会将输出保存在 nohup.out中
 
nohup sh test.sh  >> log.txt 2>&1 &	#  将test.sh的输出重定向到log.txt文件中，同时将标准错误也重定向到log.txt文件中

2>&1 # 把错误重定向保存在标准输出，而标准输出又导入文件output里面，所以结果是标准错误和标准输出都导入文件output里面了 。可以很好的将错误信息保存，帮助我们定位问题。
0：标准输入流 stdin
1：标准输出流 stdout
2：标准错误流 stderr


lsof 显示系统打开的文件 lists openfiles
yum install lsof
lsof -i:8125 	#看进程
lsof abc.txt 显示开启文件abc.txt的进程



uptime  #查看当前负载
16:58:49 up 3 days,  5:36, 20 users,  load average: 10, 11, 10
#依次则是过去1分钟、5分钟、15分钟的平均负载。

lscpu # 查看cpu个数



sudo lsof -i tcp:8889  # 根据端口号查找进程名
```



### sort

```bash
sort file                          # 排序文件
sort -r file                       # 反向排序（降序）
sort -n file                       # 使用数字而不是字符串进行比较
sort -t: -k 3n /etc/passwd         # 按 passwd 文件的第三列进行排序
sort -u file                       # 去重排序
```

### tar 压缩

```shell
tar -zcvf file.tar.gz	# 解压文件
tar -zxvf file.tar.gz -C ./test # 解压文件到test文件夹下

tar -zcvf test.tar.gz test  # 压缩文件test到test.tar.hz

```

### zip压缩

```bash
zip -q -r html.zip /home/html # 将 /home/html/ 这个目录下所有文件和文件夹打包为当前目录下的 html.zip：

unzip html.zip # 解压
```





### chmod 改权限    

### chown改所属用户 

### chgrp改所属用户组

```shell
sudo chmod 777 + 文件名	#给每个人读和写以及执行的权限
sudo chmod 775 + 文件名  # 文件所有者和所有组有读写执行权限（4+2+1）,其他人有读执行权限（4+1）
chmod 644 file      # 修改文件权限为 644，可以接 -R 对目录循环改权限
chmod 775 dir -R    # 对 dir 文件夹下的所有文件修改权限

-R 为递归处理文件夹下的所有文件

chown user1 file.txt     # 修改文件所有人为 user1
chgrp -v yuanbo file.txt  # 修改文件所属的用户组为yuanbo
```

### date

```shell
date                      # 显示日期

date -d "0 days" +%Y-%m-%d  # 今天  2020-04-02
date -d "-1 days" +%Y-%m-%d #昨天
date -d "1 days" +%Y-%m-%d # 明天
DT=`date -d "-1days" +%Y-%m-%d` 


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

### xargs 

xargs 一般是和管道一起使用,可以把多行变成一行

换行和空白将被空格取代

```bash
ps -ef | grep httpserver_cust_indus | cut -c 9-15 | xargs kill -9

# 下载多个链接
cat url-list.txt | xargs wget -c
```

###  常用脚本

```bash
history | awk '{a[$2]++}END{for(i in a){print a[i] " " i}}' | sort -rn | head  #列出最常使用的命令
ps aux | sort -nk +4 | tail   ## 显示前十个运行的进程并按内存使用量排序
dd if=/dev/zero of=/dev/null bs=1M count=32768 # 测试内存带宽
find /data0/yuanbo6  -type f -size +500M  #  查找目录下大于 500M 的文件
find ~ -mmin 60 -type f            # 查找 $HOME 目录中，60 分钟内修改过的文件
find . -type f -newermt "2020-05-01"  #按日期范围查找文件
sudo find ./ -type f -name "jieba*"  #查找当前目录下以jieba开头的文件

cat ads_type.txt|tail -n +10000|head -10 #看文件从第1w行起的10行

# 删除ads下修改时间超过7天的文件
find /ads/ -type f -mtime +7 -exec rm -f {} \;
-exec： find命令对匹配的文件执行该参数所给出的shell命令
-ctime： 创建时间
-name： 
-name ap* ： 以ap开头的文件

# 删除文件夹内，5天前的所有文件
sudo find /data0/yuanbo6/log/ -mtime +5 -name 'pusou_log*' -exec rm -f {} \;

# 将ads下超过7天内的文件合并去重
find /ads/ -type f -mtime -7 |xargs -i cat {}|sort|uniq 


# 将日志保存，清空现有日志，并删除7天前的日志
sed -n '2,$p' logger_industry/nohup_log.out > logger_industry/nohup_log.out.$(date +%Y.%m.%d.%H.%M.%S)
sudo  truncate -s 0 logger_industry/nohup_log.out
find logger_industry/ -mtime +7 -name "nohup_log.out.*" -exec rm -rf {} \;


# 重启脚本 , 找到端口号为8888的进程, 保存日志，nohup后台启动
ps -ef | grep gunicorn | grep 8888 | cut -c 9-15 | xargs kill -9
mv ./logger_industry/nohup_log.out ./logger_industry/nohup_log.out.$(date +%Y.%m.%d.%H.%M.%S)
nohup conda3/bin/gunicorn httpserver:app -b 0.0.0.0:8888 -w 2 > ./logger_industry/nohup_log.out &


# 判断文件是否为空
if test -s temp.txt;
then
    echo "生产成功"
else
    echo "生产失败"
fi 

# 查看目录下的文件数
# scan.sh
# scan.sh /home
florder=$1
dir=$(ls -l $florder |awk '/^d/ {print $NF}')
for i in $dir
do
    if [ "$i" != 'home' -a "$i" != 'proc' ];then
    f=$i
    if [ $florder != '/' ];then
        f=$florder/$i
    fi
        rs=$(ls -lR $f|grep "^-"| wc -l)
    echo $f 文件以及子文件个数 $rs
    fi
    
#获取文件的最后修改时间
LAST_MODIFY_TIMESTAMP=`stat -c %Y  file`  # ### 反引号``是命令替换，命令替换是指Shell可以先执行``中的命令，将输出结果暂时保存，在适当的地方输出。
formart_date=`date '+%Y-%m-%d' -d @$LAST_MODIFY_TIMESTAMP`
```

### 网络

```bash
# 传文件
python2 -m SimpleHTTPServer 9000	#在发送端启动 HTTPServer
wget http://机器ip:9000/yuanbo.txt	# 接收端接收，yuanbo.txt为发送端目录下的文件

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



### 文本处理 - cut/awk / sed

```bash	
${#string_name} #获得字符串长度
str="111"
echo ${#str}


# 文件中的空格 变成 tab
cat word_hash.txt | tr " " "\t" > word_hash_tab.txt
```

```bash	
cut -c 1-16                        # 截取每行头16个字符
cut -c 1-16 file                   # 截取指定文件中每行头 16个字符
cut -c3-                           # 截取每行从第三个字符开始到行末的内容
cut -d':' -f5                      # 截取用冒号分隔的第五列内容
cut -d';' -f2,10                   # 截取用分号分隔的第二和第十列内容
cut -d' ' -f3-7                    # 截取空格分隔的三到七列
echo "hello" | cut -c 1-3           # 显示 hel
echo "hello sir" | cut -d ' ' -f2   # 显示 sir
ps | tr -s " " | cut -d " " -f 2,3,4  # cut 搭配 tr 压缩字符


awk '{pattern + action}' {filenames}
# 默认以空格为分隔， 自定义分割符加 -F 参数

# 获得字符串长度
awk '{ print length($0) }' pusou_shabi.txt|head 

awk '{a+=$2}END{print a}'	#对文件的第二列求和

awk -F,  '{sum += $3};END {print sum}' test	#求文件test第三列的和

-F 可以定义分割符
awk -F '\t' '{print $1}' test.txt  #以tab为分隔

head lol.txt | awk '{print $1}'		# 打印 lol.txt head的第一列 
awk '{print $5}' file              # 打印文件中以空格分隔的第五列 ,从1开始而不是0  , ($0为所有)
awk '{print $1,$2,$3,$4}' # 四列

awk -F ',' '{print $5}' file       # 打印文件中以逗号分隔的第五列
awk -F ',' '{print $NF}' file      # 打印逗号分隔的文件中的每行最后一列

awk '/str/ {print $2}' file        # 打印文件中包含 str 的所有行的第二列
awk '{s+=$1} END {print s}' file   # 计算所有第一列的合
awk 'NR%3==1' file                 # 从第一行开始，每隔三行打印一行
awk    'NR==m {print $k}'  path/filename # 打印第m行

awk -F '\t' '($1=="光遇")' test.txt  # 打印文件中第一列是光遇的所有行

sed -n '2p' file                   # 打印文件第二行
sed -n '2,5p' file                 # 打印文件第二到第五行
sed -n '5,$ p' file    							# 第5行到最后一行

sed 's/find/replace/' file         # 替换文件中首次出现的字符串并输出结果
sed '10s/find/replace/' file       # 替换文件第 10 行内容
sed '10,20s/find/replace/' file    # 替换文件中 10-20 行内容
sed -r 's/regex/replace/g' file    # 替换文件中所有出现的字符串
sed -i 's/find/replace/g' file     # 替换文件中所有出现的字符并且覆盖文件
sed '/line/s/find/replace/' file   # 先搜索行特征再执行替换
sed -e 's/f/r/' -e 's/f/r' file    # 执行多次替换
sed 's#find#replace#' file         # 使用 # 替换 / 来避免 pattern 中有斜杆
sed -i -r 's/^\s+//g' file         # 删除文件每行头部空格
sed '/^$/d' file                   # 删除文件空行并打印 去掉空行 删除空行
sed -i 's/\s\+$//' file            # 删除文件每行末尾多余空格
sed -i '1d' file 									 # 删除第一行
sed -i '$d' file 										# 删除最后一行
sed 's/root/new/' file                          //将文件中的root替换成new，每行只替换一次
sed 's/root/new/g' file                       //将每行的所有root全部替换成new        g替换多次
sed '3,4s/root/new/g' file                 //只替换第3到第4行的root为new

cat testfile |tr a-z A-Z  #将文件testfile中的小写字母全部转换成大写字母

# tr (translate)
cat /data0/yuanbo6/pusou_log_2.txt |tr a-z A-Z  #大写变小写
cat pusou_log.txt |tr [:upper:] [:lower:] >> pusou_lower.txt  #将文件中的大写字母全部转换成小写字母

# 统计词频
cat words.txt | tr -s ' ' '\n'|sort|uniq -c |sort -nr|awk '{print $2" "$1}'


cat ——浏览文件
tr -s ——替换字符串（空格换为换行）保证了一行一个单词
sort ——默认ASCII值排序，排序号后还会有重复
uniq —— 去重，-c再输出重复次数。结果就是 ”4 abc“ abc出现了4次
sort -r —— 反向排序，也就是从大到小。得到按频率高低的结果
-n 依照数值的大小排序
awk ——格式化输出，规定输出是先字符串再重复次数，所以先$2再$1，中间空格分隔

# 同时限制词频的数量 , 只输出频次大于>10的行数
sudo cat log.txt|jq '.key'|sed 's/\"//g' |sort|uniq -c |sort -nr|awk '$1>10{print $2"\t"$1}'



```



### shell处理json

```bash
sudo yum install -y jq	#下载安装jq
echo '{"key": "syw"}' | jq '.key'
echo '{"key": {"key2": "val"}}' | jq '.key.key2'
echo '{"key": {"key2": ["val1", "val2"]}}' | jq '.key.key2[1]'

# 去掉文本中的引号
head log.txt|jq '.content'|sed 's/\"//g'
sed 's/\"//g'
```









