gpt2

```
gpt2-Chinese的train.py报错：
AttributeError: module transformers has no attribute modeling_gpt2

solution:
from transformers.modeling_gpt2 import GPT2LMHeadModel
change to :
from transformers.models.gpt2.modeling_gpt2 import GPT2LMHeadModel



AttributeError: module transformers has no attribute WarmupLinearSchedule

solution:
from transformer import get_linear_schedule_with_warmup
change to 




```

```python
from transformers import BertTokenizer, GPT2LMHeadModel, TextGenerationPipeline
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
model = GPTLMHeadModel.from_pretrained(MODEL_NAME)
text_generator = 
```

### 方法一:transformers中的TextGenerationPipeline类

```python
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
text_generator = TextGenerationPipeline(model, tokenizer)   

# 单个input
text_generator("雀巢",
               max_length=200, 
               do_sample=True,
               top_k=2)
               
# 生成多条
text_generator("雀巢",
               max_length=200, 
               do_sample=True,
               num_return_sequences=3,
               repetition_penalty=5.0,
               top_k=2)
               
               
# 多个input
text_inputs = ["原神",
                "王者荣耀",
                "炒股",
                "连衣裙",
                "蓝牙耳机",
                "口红"]
gen = text_generator(text_inputs, 
                    max_length=100, 
                    repetition_penalty=3.0, 
                    do_sample=True, 
                     num_return_sequences= 3,
                    num_beams=5,
                    top_k=10) 
                    
for sent in gen:
    gen_seq = sent[0]["generated_text"]
    print("")
    print(gen_seq.replace(" ",""))

           
           
```

### 方法2：transformers通用方法，直接加载模型
优点：由于是transformers调用模型的通用写法，和其他模型（如bert）的调用方式相似，（如tokenizer的使用），可以举一反三。

```python

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
```



### 指令微调 instruct tuning 

将下游任务变成一句话 (数据集)







### 一文整理GPT-3 + RL 全流程训练开源项目

https://mp.weixin.qq.com/s/BFGT6f7HFTYZ1VUooJqpXg



