```bash
# 删除文件夹内，5天前的所有文件
sudo find /data0/yuanbo6/all_pusou_log/ -mtime +5 -name 'pusou_log*' -exec rm -f {} \;
```

