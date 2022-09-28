```python
from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'hello world!'

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8888, debug=True)  
# 定义机器号和端口号
# debug=True :调试模式 , 出现错误能够显示错误信息，并且在代码发生变化时，能够自动的重启程序。



# request.json 将json数据 -> python数据类型
# jsonify 函数
from flask import jsonify, request

@app.route('/add',methods=['POST'])
def add():
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
  
```

