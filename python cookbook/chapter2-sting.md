### re.split(规则，字符串） , 用正则表达式分隔字符串

import re 

line = 'a,b;c d' 

re.split(r'[,; ]',line) 

['a','b','c','d'] 

re.split(r'([,; ])',line) 

['a',',','b',';','c',' ','d']

- 如果没有加括号，返回的就是正则表达式匹配的元素。
- 加了括号，分隔符也会被当做元素返回。 


### 
filename = '123.py' 

filename.startswith('123') 

返回：True 

filename.endswith('.py') 

返回：True 


import os 

filenames = os.listdir() 

os.listdir()可以列出所有的**文件名**


files = [file for file in filenames if file.endswith('.py') 

找出所有的 .py 文件
 


