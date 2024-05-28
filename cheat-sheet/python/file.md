###  json 

```python
import json
f = open('file_name.json')
data = json.loads(f)
f.close


with open('test.json') as f:
    line= f.readline()
    dic = eval(line)
    
with open('dev.json') as f:
    data = json.loads(f.read())
    print(data)
    
### json
# json.dumps: convert python type to json   ,json.dump : save json to file 
# json.loads: convert json to python type 

### wirte 
import json
data = {'name':'z'}
json_str=json.dumps(data)

import json
dump_data = json.dumps(tag_dic)  # dumps 将字典变成json类型
with open('test_json.txt','w+') as f:
    f.write(dump_data)
    
```

### os

```python
import os 
dir_path = '/data0/test'
# 当前目录下的文件
os.listdir(dir_path)

# 显示目前所处的目录
os.getcwd()



```





### 获得文件夹下的最新文件

```python
import os
file_path = '/data0/yuanbo6/pusou_query_count/'
files = os.listdir(file_path)
files_path =[os.path.join(file_path,file_name) for file_name in files]
files_path.sort(key=lambda fp: os.path.getctime(fp),reverse=True)
latest_file = files_path[0]

```

```python
import os
file_list =  os.listdir(file_dir)
file_list =  [os.join_path(file_name,file_dir) for file_name in file_list]
print(file_list)
```



### write csv

```python
# importing the csv module
import csv
	
# my data rows as dictionary objects
mydict =[{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
		{'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
		{'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
		{'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
		{'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
		{'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}]
	
# field names
fields = ['name', 'branch', 'year', 'cgpa']
	
# name of csv file
filename = "university_records.csv"
	
# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames = fields)
		
	# writing headers (field names)
	writer.writeheader()
		
	# writing data rows
	writer.writerows(mydict)


```

### save image 保存图片

```python
# save image
import requests
url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
img_data = requests.get(url).content
with open('./image_name.jpg', 'wb') as handler:
    handler.write(img_data)
```

### gif to jpg

```python
from PIL import Image

im = Image.open('Fighter-Front.gif')
im.convert("RGBA")
im.save('test1.png')
```

