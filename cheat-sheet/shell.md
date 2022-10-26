### Shell 编程

```bash
# 定义变量
a = 1 
echo $varname             # 查看变量内容

# 条件语句
# 如果存在 /root 中存在 a.txt ，则返回1 ， 否则返回0 ， if的[ ] , 前后都有空格
# linux 中 0代表条件为真，1代表为假
if [ -f /root/a.txt ]; then echo 1 ; else echo 0; fi

if ["$1" == 100]; then 

# 循环语句
for i in {1..10}; do echo $i ; done 
for (( i=1; i<10 ; i++)) ; do echo $i ; done
for file in /data0/yuanbo6/* ; do echo $file ; done  # for 循环打印某目录下面的所有文件
for loop in 1 2 3 ;do  echo $loop ; done

i=1;while [ $i -le 10 ]; do echo $i; i=$(expr $i + 1); done


# 函数
function fun1 () { echo 'a' }

unset -f fun1  # 删除函数

declare -f     # 查看所有函数

if [$? -ne 0]; #  如果上一条命令成功执行
# ？表示上一条命令的返回值，成功0，失败1 -ne代表不等于， 
-eq 等于
-ne 不等于
-gt 大于
-ge 大于等于


```







```bash
# define function
function fun1(){
echo 1
}

function archive(){
	cp $1 $2
	chmod 777 $2
	rm $1
}


function alarm_file() {
#获取文件最后修改时间戳
LAST_MODIFY_TIMESTAMP=`stat -c %Y $1`
formart_date=`date '+%Y-%m-%d' -d @$LAST_MODIFY_TIMESTAMP`
echo $formart_date
if [ $formart_date = $today ];then
	echo "$1生产成功"
else
	echo "$1生产失败"
	exit 1  
fi 

if [ -s $1 ] ; then  #如果文件存在
	echo "$1文件不为空"
else
	echo "$1文件为空"
	exit 1 
}
fi

# 检测文件是否符合标准
alarm_file /data0/yuanbo6/pusou_log.txt 

# exit 0 正常退出程序 。
# exit 1 代表非正常运行导致退出程序
#程序退出后, 用户可以 echo $? 来查看是 0 还是 1, 从而达到检测程序是正常结束退出还是产生错误而退出的目的.



```





```bash
# 删除文件夹内，5天前的所有文件
sudo find /log/ -mtime +5 -name 'pusou_log*' -exec rm -f {} \;
```



https://blog.csdn.net/weixin_43274002/article/details/119256557?spm=1001.2014.3001.5502

