### crontab

```shell
0 11 * * *   # 每天11点执行
sudo service crond restart 	#重启crontab服务


## crontab 误删恢复
sudo cat /var/log/cron*|grep "(yuanbo6) CMD"| awk -F '(' '{print $3}'|awk -F ')' '{print $1}'|sort|uniq > crontab_temp.txt


sudo cat /var/log/cron*|grep "(yuanbo6) CMD"|sort|uniq
```

### 