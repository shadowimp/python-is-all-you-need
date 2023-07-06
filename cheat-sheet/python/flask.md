```python
from flask import Flask 

import flask 
from flask import Flask, url_for, request, jsonify, redirect
import os
import json
import requests
import re
import time
import argparse
import os
import requests
import json
import re

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
		import socket 
    host_name = socket.gethostname()
    app.config["JSON_AS_ASCII"] = False
    app.config['JSONIFY_MIMETYPE'] = "application/json;charset=UTF-8" 
    app.run(host='0.0.0.0',port=host_name , debug=True)  
# 定义机器号和端口号
# debug=True :调试模式 , 出现错误能够显示错误信息，并且在代码发生变化时，能够自动的重启程序。



# request.json 将json数据 -> python数据类型
# jsonify 函数
from flask import jsonify, request

@app.route('/add',methods=['POST'])
def add():
  data = json.loads(request.get_data(as_text=True))
  a = data['a']
  result = {'sum': request.json['a'], + request.json['b']}
  return jsonify(result)
  
json_data = {'a':1, 'b':2}
r = requests.post(url, json=json_data)



redirect # 重定向
from flask import redirect

@app.route('/test1')
def test1():
  print('test1')
  return redirect(url_for('test2'))


flask.redirect(flask.url_for('operation'), code=307)


# test url 
import json
import requests
def image2text(img_url): 
    url = 'http://11.1.1.1./test'
    response =  requests.post(url, data=json.dumps({'url':img_url}))
    return response.json()

url = ''
  
```





``` bash
# 后台 run api

nohup python test_api.py >> test.log 	2>&1 &
```



```bash
# gunicorn start 
nohup /data0/yuanbo6/conda/bin/gunicorn -w 3 -b 10.10.10.123:1234 api:app >> api.log 2>&1 &

# kill 
ps -ef | grep gunicorn | grep 8139 | cut -c 9-15 | xargs kill -9
```





```python
# get ip
requst_ip = request.remote_addr
file_log.info('ip:'+str(requst_ip))
```





### gunicorn

```
pip install gunicorn
```

