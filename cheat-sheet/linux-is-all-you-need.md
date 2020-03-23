

```shell
ls /usr/bin | grep python		#列出/usr/bin  目录下 ，文件名中有python 的文件 

ps  显示当前进程

df -h   查看磁盘空间

ll -h   查看文件大小

nohop

nvidia-smi	# 查看GPU使用率
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
tmux new -s zyb       新建名为zyb的tmux
tmux new at -t zyb    进入名为zyb的tmux
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



