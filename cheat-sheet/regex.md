## 正则表达式

### 正则表达式 regex : regular expression

```bash
\w 	匹配一个常用字符，包括字母、数字、下划线
\s  匹配空格	
\d	数字,qual to [0-9]
. 可以匹配任意字符
^ 开头
& 结尾
{10}	重复10次
{5, 10}	重复5-10次
{5, }	重复5次以上

匹配4位数字的号码：
^\d\d\d\d$

匹配1开头11位数字的手机号码：
 ^1\d{10}$
 
 数字1-9或字母a-e
 [1-9a-e]
 
 中文
 [\u4e00-\u9fa5]

将字母换成大写，就表示相反的意思。用 \d 你可以匹配一个数字，\D 则表示匹配一个非数字






去除方框内的文字
sen2 = '昨天跑路跑到高雄[偷笑]~[太阳]天气好好喔！'
sen2 = re.sub('\[.*?\]', '', sen2)


+ 表示 至少匹配出现一次的字符。它等价于 {1,} , "d+"  匹配任意的数字

# 去掉字符串中的某个字符
re.sub('#', '', sen2)

# 提取书名号中内容
re.findall('《(.*?)》','亚洲首部以iPhone全程拍摄的剧情长片《怪胎》| 由担任《那些年我们一起追的女孩》执行导演廖明毅执导')


## 匹配数字
import re 
text1 = '2017/08/20'
if re.match(r'\d+/\d+/\d+',text1):
    print(1)
else:
    print(0)
    
# 去掉纯数字, 只要有汉字或者英文就能返回
re_han = re.compile("([\u4E00-\u9FD5a-zA-Z]+)", re.U)
if len(re_han.findall(word)) > 0:  #不要纯英文数字
	print(word.lower())



    

```



```python
re.findall(regex, str)
# 匹配文本中所有满足regex的str， 输出一个list

re.search(regex,str)
# 找到一个满足regex的str就结束

re.match(regex, str)


```

