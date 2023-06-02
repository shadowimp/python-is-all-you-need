### openai  gpt编码 token

https://platform.openai.com/tokenizer

openai使用BPE（byte pair encoding）算法进行编码（对空格,标点符号，emoji都有编码）

常用的词占的token较少。

一个汉字可能对应2-3个token

```
from transformers import GPT2Tokenizer 
tokenizer = GPT2Tokenizer.from_pretrain('gp2')
text = "Hello, how are you?"
tokens = tokenizer.encode(text)
num_tokens = len(token)
```



### 多轮对话

https://www.bilibili.com/read/cv22159513/



```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


# 单轮对话调用
# model可选"gpt-3.5-turbo"与"gpt-3.5-turbo-0301"
def generate_answer(messages):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    res_msg = completion.choices[0].message
    return res_msg["content"].strip()


if __name__ == '__main__':
    # 维护一个列表用于存储多轮对话的信息
    messages = [{"role": "system", "content": "你现在是很有用的助手！"}]
    while True:
        prompt = input("请输入你的问题:")
        messages.append({"role": "user", "content": prompt})
        res_msg = generate_answer(messages)
        messages.append({"role": "assistant", "content": res_msg})
        print(res_msg) 作者：Saber家的妹抖 https://www.bilibili.com/read/cv22159513/ 出处：bilibili
```







```
q： 大模型应用到垂直领域。

chatglm + 私域数据
需要足够的硬件 ，a100， H100.
显存足够大， 
高质量的数据

微软框架
deep speed chat

gpt finetune 开放到3.0 ， 达芬奇
finetune效果一般，
选择性遗忘，

利用大模型的上下推理能力+垂直领域知识库

在知识库中去检索，相关背景知识， 再喂给gpt， 结合prompt ， 得到输出。
构建简单，没法保证每次学习都能达到很好的效果。





```

![image-20230531151550940](/Users/yuanbo6/Library/Application Support/typora-user-images/image-20230531151550940.png)





网页版memory能力， 

把前面几轮的对话都放入到prompt。



langchain and semantic kernel。

langchain： memory 的能力， 提供记忆能力，变成有状态的。

finetune服务器在海外， 注意数据出镜的能力。



知识库的搭建： 



3.5 ： 4k  token 