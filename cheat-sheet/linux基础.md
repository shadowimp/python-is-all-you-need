# 文件操作


cat {fn}            # 输出文件原始内容

head {fn}           # 显示文件头部数行，可用 head -3 abc.txt 显示头三行
tail {fn}           # 显示文件尾部数行，可用 tail -3 abc.txt 显示尾部三行
tail -f {fn}        # 持续显示文件尾部数据，可用于监控日志
diff {f1} {f2}      # 比较两个文件的内容
wc {fn}             # 统计文件有多少行，多少个单词

file {fn}           # 检测文件的类型和编码
用户管理

##############################################################################

uname -a                  # 查看内核版本等信息
man {help}                # 查看帮助
man -k {keyword}          # 查看哪些帮助文档里包含了该关键字
info {help}               # 查看 info pages，比 man 更强的帮助系统
uptime                    # 查看系统启动时间
date                      # 显示日期
cal                       # 显示日历
vmstat                    # 显示内存和 CPU 使用情况
vmstat 10                 # 每 10 秒打印一行内存和 CPU情况，CTRL+C 退出
free                      # 显示内存和交换区使用情况
df                        # 显示磁盘使用情况
du                        # 显示当前目录占用，du . --max-depth=2 可以指定深度
uname                     # 显示系统版本号
hostname                  # 显示主机名称
showkey -a                # 查看终端发送的按键编码



whoami              # 显示我的用户名
who                 # 显示已登陆用户信息，w / who / users 内容略有不同
w                   # 显示已登陆用户信息，w / who / users 内容略有不同
users               # 显示已登陆用户信息，w / who / users 内容略有不同
passwd              # 修改密码，passwd {user} 可以用于 root 修改别人密码

su                  # 切换到 root 用户
su -                # 切换到 root 用户并登陆（执行登陆脚本）
su {user}           # 切换到某用户
su -{user}          # 切换到某用户并登陆（执行登陆脚本）
id {user}           # 查看用户的 uid，gid 以及所属其他用户组
id -u {user}        # 打印用户 uid
write {user}        # 向某用户发送一句消息
last                # 显示最近用户登陆列表
last {user}         # 显示登陆记录
lastlog             # 显示所有用户的最近登陆记录
sudo {command}      # 以 root 权限执行某命令

##############################################################################

# 进程管理
##############################################################################

ps                        # 查看当前会话进程
ps ax                     # 查看所有进程，类似 ps -e
ps aux                    # 查看所有进程详细信息，类似 ps -ef
ps auxww                  # 查看所有进程，并且显示进程的完整启动命令
ps -u {user}              # 查看某用户进程
ps axjf                   # 列出进程树
ps xjf -u {user}          # 列出某用户的进程树
ps -eo pid,user,command   # 按用户指定的格式查看进程
ps aux | grep httpd       # 查看名为 httpd 的所有进程
ps --ppid {pid}           # 查看父进程为 pid 的所有进程
pstree                    # 树形列出所有进程，pstree 默认一般不带，需安装
pstree {user}             # 进程树列出某用户的进程
pstree -u                 # 树形列出所有进程以及所属用户
pgrep {procname}          # 搜索名字匹配的进程的 pid，比如 pgrep apache2

kill {pid}                # 结束进程
kill -9 {pid}             # 强制结束进程，9/SIGKILL 是强制不可捕获结束信号
kill -KILL {pid}          # 强制执行进程，kill -9 的另外一种写法
kill -l                   # 查看所有信号
kill -l TERM              # 查看 TERM 信号的编号
killall {procname}        # 按名称结束所有进程
pkill {procname}          # 按名称结束进程，除名称外还可以有其他参数

top                       # 查看最活跃的进程
top -u {user}             # 查看某用户最活跃的进程

any_command &             # 在后台运行某命令，也可用 CTRL+Z 将当前进程挂到后台
jobs                      # 查看所有后台进程（jobs）
bg                        # 查看后台进程，并切换过去
fg                        # 切换后台进程到前台
fg {job}                  # 切换特定后台进程到前台

trap cmd sig1 sig2        # 在脚本中设置信号处理命令
trap "" sig1 sig2         # 在脚本中屏蔽某信号
trap - sig1 sig2          # 恢复默认信号处理行为

nohup {command}           # 长期运行某程序，在你退出登陆都保持它运行
nohup {command} &         # 在后台长期运行某程序
disown {PID|JID}          # 将进程从后台任务列表（jobs）移除

wait                      # 等待所有后台进程任务结束


##############################################################################
# 常用命令：SSH / 网络
##############################################################################

ssh user@host             # 以用户 user 登陆到远程主机 host
ssh -p {port} user@host   # 指定端口登陆主机
ssh-copy-id user@host     # 拷贝你的 ssh key 到远程主机，避免重复输入密码
scp {fn} user@host:path   # 拷贝文件到远程主机
scp user@host:path dest   # 从远程主机拷贝文件回来
scp -P {port} ...         # 指定端口远程拷贝文件

sz {file}                 # 发送文件到终端，zmodem 协议
rz                        # 接收终端发送过来的文件


##############################################################################





# 变量操作

##############################################################################

varname=value             # 定义变量
varname=value command     # 定义子进程变量并执行子进程
echo $varname             # 查看变量内容

export VARNAME=value      # 设置环境变量（将会影响到子进程）

array[0]=valA             # 定义数组

${array[i]}               # 取得数组中的元素
${#array[@]}              # 取得数组的长度
${#array[i]}              # 取得数组中某个变量的长度

declare -a                # 查看所有数组
declare -f                # 查看所有函数
declare -F                # 查看所有函数，仅显示函数名
declare -i                # 查看所有整数
declare -r                # 查看所有只读变量
declare -x                # 查看所有被导出成环境变量的东西
declare -p varname        # 输出变量是怎么定义的（类型+值）

${varname:-word}          # 如果变量不为空则返回变量，否则返回 word
${varname:=word}          # 如果变量不为空则返回变量，否则赋值成 word 并返回
${varname:?message}       # 如果变量不为空则返回变量，否则打印错误信息并退出
${varname:+word}          # 如果变量不为空则返回 word，否则返回 null
${varname:offset:len}     # 取得字符串的子字符串

${variable#pattern}       # 如果变量头部匹配 pattern，则删除最小匹配部分返回剩下的
${variable##pattern}      # 如果变量头部匹配 pattern，则删除最大匹配部分返回剩下的
${variable%pattern}       # 如果变量尾部匹配 pattern，则删除最小匹配部分返回剩下的
${variable%%pattern}      # 如果变量尾部匹配 pattern，则删除最大匹配部分返回剩下的
${variable/pattern/str}   # 将变量中第一个匹配 pattern 的替换成 str，并返回
${variable//pattern/str}  # 将变量中所有匹配 pattern 的地方替换成 str 并返回

${#varname}               # 返回字符串长度

*(patternlist)            # 零次或者多次匹配
+(patternlist)            # 一次或者多次匹配
?(patternlist)            # 零次或者一次匹配
@(patternlist)            # 单词匹配
!(patternlist)            # 不匹配

array=($text)             # 按空格分隔 text 成数组，并赋值给变量
IFS="/" array=($text)     # 按斜杆分隔字符串 text 成数组，并赋值给变量
text="${array[*]}"        # 用空格链接数组并赋值给变量
text=$(IFS=/; echo "${array[*]}")  # 用斜杠链接数组并赋值给变量

$(UNIX command)           # 运行命令，并将标准输出内容捕获并返回
varname=$(id -u user)     # 将用户名为 user 的 uid 赋值给 varname 变量

num=$(expr 1 + 2)         # 兼容 posix sh 的计算，使用 expr 命令计算结果
num=$(expr $num + 1)      # 数字自增
expr 2 \* \( 2 + 3 \)     # 兼容 posix sh 的复杂计算，输出 10

num=$((1 + 2))            # 计算 1+2 赋值给 num，使用 bash 独有的 $((..)) 计算
num=$(($num + 1))         # 变量递增
num=$((num + 1))          # 变量递增，双括号内的 $ 可以省略
num=$((1 + (2 + 3) * 2))  # 复杂计算


##############################################################################




# 文本处理 - awk / sed
##############################################################################

awk '{print $5}' file              # 打印文件中以空格分隔的第五列
awk -F ',' '{print $5}' file       # 打印文件中以逗号分隔的第五列
awk '/str/ {print $2}' file        # 打印文件中包含 str 的所有行的第二列
awk -F ',' '{print $NF}' file      # 打印逗号分隔的文件中的每行最后一列
awk '{s+=$1} END {print s}' file   # 计算所有第一列的合
awk 'NR%3==1' file                 # 从第一行开始，每隔三行打印一行

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
sed -n '2p' file                   # 打印文件第二行
sed -n '2,5p' file                 # 打印文件第二到第五行


##############################################################################





# 下载一个网站的所有图片
wget -r -l1 --no-parent -nH -nd -P/tmp -A".gif,.jpg" http://example.com/images

# 快速创建项目目录
mkdir -p work/{project1,project2}/{src,bin,bak}

# 按日期范围查找文件
find . -type f -newermt "2010-01-01" ! -newermt "2010-06-01"



```bash
lsof -P -i -n | cut -f 1 -d " "| uniq | tail -n +2		#显示当前正在使用网络的进程
:w !sudo tee > /dev/null % # Vim 中保存一个没有权限的文件
```



在 .bashrc / .bash_profile 中加载另外一个文件（比如你保存在 github 上的配置）

source ~/github/profiles/my_bash_init.sh









