### read json 

```
import json
f = open('file_name.json')
data = json.loads(f)
f.close


with open('test.json') as f:
    line= f.readline()
    dic = eval(line)
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

