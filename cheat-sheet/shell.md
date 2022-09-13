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

