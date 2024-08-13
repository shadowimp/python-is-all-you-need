







### Shell 编程

```bash
for file in data_2023* ;
do
echo "$file"| sed 's/2023/2024/';
new_file=$(echo "$file"| sed 's/2023/2024/');
echo "$new_file"
mv "$file" "$new_file";
echo "Renamed $file to $new_file";
done

echo "data_20240523.txt" | sed 's/2024/2025/' 
> data_20250523.txt
```



```bash
# 定义变量
a = 1 
echo $varname             # 查看变量内容

# 文件内容存入变量
value =`cat sources.xml`

# 时间变量
time_archive=$(date "+%Y%m%d")


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

if [$? -eq 0]; #  如果上一条命令成功执行
# ？表示上一条命令的返回值，成功0，失败1 -ne代表不等于， 
-eq 等于
-ne 不等于
-gt 大于
-ge 大于等于



$0 # 程序的名字
$1 # 程序的第1个参数
$2 # 程序的第2个参数
$* # all parameter
$? # 执行上一个指令的返回值 (显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误)
$# # nums of parameter 
$$ # pid number 
$! # 上一个运行的
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

# 调用 ： 检测文件是否符合标准
alarm_file /data0/yuanbo6/pusou_log.txt 

# exit 0 正常退出程序 。
# exit 1 代表非正常运行导致退出程序
#程序退出后, 用户可以 echo $? 来查看是 0 还是 1, 从而达到检测程序是正常结束退出还是产生错误而退出的目的.



```





```bash
# 删除文件夹内，5天前的所有文件
sudo find /log/ -mtime +5 -name 'pusou_log*' -exec rm -f {} \;


# 判断程序是否在运行
RUNPID=`ps -ef|grep test.py|grep -v grep|awk '{print $3}'`
echo "$RUNPID"
if [ "$RUNPID" != "" ];
then 
echo "正在运行"
else
echo "不在运行"
fi
```



https://blog.csdn.net/weixin_43274002/article/details/119256557?spm=1001.2014.3001.5502





shell中运行python

```python
lines=open('file.txt').readlines()
items=[item.strip().split() for item in lines]
print(items)
```

```bash
python3 -c "lines=open('file.txt').readlines();items=[item.strip().split() for item in lines];print(items)
"
```





```shell
#!/bin/bash

# 指定日志文件的路径和前缀
log_directory="./"
log_prefix="combine_demo_"

# 获取当前日期
current_date=$(date +"%Y%m%d")

# 获取当前月份
current_month=$(date +"%Y%m")

# 指定汇总文件名
summary_file="log_month_${current_month}.txt"

# 创建一个空的汇总文件
touch "${summary_file}"

# 遍历日志文件
for logfile in ${log_directory}${log_prefix}*.txt; do
  # 提取日志文件的日期部分
  log_date=$(basename "${logfile}" | cut -d '_' -f 2)

  # 检查日志文件的日期是否在当前月份内
  if [[ "${log_date}" == ${current_month}* ]]; then
    # 追加当前日志文件内容到汇总文件
    cat "${logfile}" >> "${summary_file}"
  fi
done

echo "日志已汇总到 ${summary_file}"



```

