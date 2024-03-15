### convert bytes to string

```
>>> b"abcde".decode("utf-8")
```



### hash

```python
import hashlib

hash_obj = hashlib.md5()

hash_obj.update("string".encode('utf-8'))

res_hash=hash_obj.hexdigest()

```



### json

```
import json
data = {'name':'z'}
json_str=json.dumps(data)


# json.dumps: convert python type to json   ,json.dump : save json to file 
# json.loads: convert json to python type 
```



```

```











```python
# assert 
def fun_div(a,b):
		assert b != 0 , "被除数不得为0"
    return a/b 
```





```python	
集合set
交集 &
并集 |
差集 -

# sort dic 
sorted_query_dic = sorted(query_dic.items(), key = lambda query_dic:query_dic[1], reverse=True)


# 注意lambda返回值是一个元祖
sorted(person,key=lambda x: (x.age, x.height)) 


对于一个三元组的list用默认的sorted，结果是先按照第一个字段升序，在第一个字段相同的情况下按照第二个字段升序，在前两个字段都相同的情况下按照第三个字段升序。

key=lambda x: (-x[0], x[1]) # 优先对x[0] 降序排列，然后对x[1] 进行升序排列

a = ['ab:1','ad:90','ac:8','d:2.2']
sorted(a, key = lambda x:x.split(':')[1], reverse=True)
>> ['ad:90', 'ac:8', 'd:2.2', 'ab:1']


res_dic = {}
for res_line in res:
    res_line = str(res_line)
    res_dic[res_line] = res_dic.get(res_line,0) + 1 
    
    
res_uniq = []
for item in res_dic.keys():
    item = eval(item)
    res_uniq.append(item)
    
    
    
# os 检测是否有目录下有    
if not os.path.exists(output_home):
    logger.info('Output path does not exists and created.')
    os.makedirs(output_home)
    
在python中运行linux脚本
os.system('go run hash_code.go >> word_hash.txt')
返回0表示执行成功,返回其他代表失败

        
# python 全局变量
在函数内使用 global


保留两位小数
n = 3.14159
print('%.2f'%n)
>> 3.14

word = "apple"
print(f"word:{word}")


# -*- coding:utf-8 -*-


import os
os.remove(temporary_filepath)

import io
# 限定读的字符数
size = 100
with open('brandname.csv','r') as f:
    lines_100 = io.StringIO(f.read(size))
for line in lines_100:
    print(line)
    
    
    
import json
dump_data = json.dumps(tag_dic)  # dumps 将字典变成json类型
with open('test_json.txt','w+') as f:
    f.write(dump_data)
    
    
def is_english(s):
    '全是英文的返回TRUE'
    for c in s:
        if '\u4e00' <= c <= '\u9fa5':
            return False
    return True  
  
  
# jieba 
import jieba

def Sent2Word(sentence):
    words = jieba.cut_for_search(sentence)
    # words = [w for w in words if w not in stop_words]
    return list(words)
  

import time
time.sleep(5) 

## 深拷贝
import copy
b = copy.deepcopy(a)
```



WSGI（Python Web Server Gateway Interface）





### flask

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/index')
def index():
    return jsonify(msg='hello world')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    
## example 2
import flask
from flask import request 

app = Flask(__name__)

@app.route("/api/sum")
def get():
  a,b = request.args['a'] + request.args['b']
  return str(int(a) + int(b))
if __name__ == '__main__':
  app.run()
# 访问浏览器查看效果 http://127.0.0.1:5000/api/sum?a=1&b=3  
```

### gunicorn

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!
   
```

#### 使用gunicorn运行flask: 

conda3/bin/gunicorn -w 2 -b 1.2.3.4:1234 flask_server:app 

flask_server : 为py文件名

-w : worker 数量

-b : 指定端口号

ps -ef | grep gunicorn









#### python get ip 地址

```python
import socket 
hostname = socket.gethostname()
ip = socket.gethostbyname()
```





```
which python #查看当前的python环境

pip show numpy #查看python库信息




```



Non-ASCII character '\xe5' in file word2vec_api.py on line 1, but no encoding declared 报错

```python
首行附加：
#!/usr/bin/python
# -*- coding: utf-8 -*-


```

which python #看目前使用的什么python环境



### pip

```shell
pip ``install` `numpy --upgrade --ignore-installed
```



### subprocess

```python
## 在python 中运行shell脚本
import os
os.system('cd /usr/local')

import subprocess as sp
cmd1 = 'pwd'
ret = sp.run(cmd1, shell=True)


```

### argv

```python
import sys
a, b,c = sys.argv[0] , sys.argv[1], sys.argv[2]
print(a,b,c)

>> python test.py 1 2 
>> test.py 1 2


import sys
a = sys.argv[1:]
print(a)
>> python test.py 1 2 3 a
>> ['1', '2', '3', 'a']

```





pyinotify

监控文件变动

加上我们三个的数据，准确率能到多少



### 获得路径下的最新文件

```python
import os
file_path = '/usr/home/xiaolu10/xiaolu4/query_get_blog/data'
files = os.listdir(file_path)
files_path =[os.path.join(file_path,file_name) for file_name in files]
files_path.sort(key=lambda fp: os.path.getctime(fp),reverse=True)
latest_file = files_path[:2]
print(latest_file) # 绝对路径
```



### 版本查看

```python
import torch
import numpy as np
import transformers
print(torch.__version__)  # 1.7.1
print(transformers.__version__)
```



### bytes 转换为 str

str(b, encoding = "utf-8") 





isinstance

判断变量是不是指定类型

```python
a = 2 
isinstance(a,int) 
>> True

isinstance (a,(str,int,list)) #是其中任一就为True


```





getctime : 最后修改时间

getmtime 创建时间

getatime  访问时间





```python
import re
def text_normal_l1(text):
    # 对数据进行简单清洗
    rule_url = re.compile(
        '(http?://)?(www\\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_+.~#?&/=]*)'
    )

    rule_legal = re.compile('[^\\[\\]@#a-zA-Z0-9\u4e00-\u9fa5，。！？：《》、*]')

    rule_space = re.compile('\\s+')
    text = str(text).replace('\\n', ' ').replace('\n', ' ').strip()
    text = rule_url.sub(' ', text)
    text = rule_legal.sub(' ', text)
    text = rule_space.sub(' ', text)
        
    # 去除表情符号
    try:  
        rule_emoij = re.compile(u'['u'\U0001F300-\U0001F64F' u'\U0001F680-\U0001F6FF'u'\u2600-\u2B55]+')  
    except re.error:  
        rule_emoij = re.compile(u'('u'\ud83c[\udf00-\udfff]|'u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'u'[\u2600-\u2B55])+') 
        
    text = rule_emoij.sub(' ', text)
    
    text = re.sub("\[\S+?\]", " ", text)  # 取出表情符号
    return text.strip()  
```



