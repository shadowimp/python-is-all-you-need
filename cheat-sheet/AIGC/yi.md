https://github.com/01-ai/Yi/blob/main/README_CN.md





```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
model_dir = "/data0/yuanbo6/model/yi/"
lora_dir = "/data0/yuanbo6/model/ft_model/lora_yi"
tokenizer = AutoTokenizer.from_pretrained(model_dir, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(model_dir,device_map="auto",torch_dtype='auto' ).eval()
model = PeftModel.from_pretrained(model, lora_dir)
model = model.eval()

def fun(prompt):
    messages = [{"role": "user", "content": prompt}]
    input_ids = tokenizer.apply_chat_template(conversation=messages, tokenize=True, add_generation_prompt=True, return_tensors='pt')
    output_ids = model.generate(input_ids.to('cuda'),max_new_tokens=200,num_beams=1,temperature=1.0,top_p=0.95)
    response = tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True)

    return response

if __name__ == "__main__":
    prompt =  "python�~X��~@�~H"

    print(fun(prompt))
```



```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = 'model/yi/model_6b_chat'

tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False)

# Since transformers 4.35.0, the GPT-Q/AWQ model can be loaded using AutoModelForCausalLM.
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    torch_dtype='auto'
).eval()


# Prompt content: "hi"
messages = [
    {"role": "user", "content": "我想请你扮演一个微博广告创作者，你将创作一条简短的中文微博广告,你可以参考下面的内容:连衣裙"}
]


messages = [
    {"role": "user", "content": "python是什么"}
]

messages = [
    {"role": "user", "content": "我想请你扮演一个微博创作者，请你用小红书的风格你创作一条简短的中文微博广告,你可以参考下面的内容:丝滑,自然提气色,『MISTINE奶咖唇冻/唇霜,领券立减,61,恢复,日常价,119/2支,极限,买2件,天猫"}
]


messages = [
    {"role": "user", "content": "请你扮演一个微博创作者，你将创作1条简短的中文微博，目的是为了提高APP:贝壳找房-买房装修新房二手房租房平台的下载量。请你使用轻松热情的语气。你可以参考下面的内容: 真实房源交易，整装家居服务，幸福安居让家更美好提供全面真实实时的房源动态、高效的找房工具、省心的一站式整装家居等特色服务产品亮点:  【海量房源】二手房、新房、租房、商铺办公等真实房产信息，您想要的都在这里,【家装服务】整装"}
]


#device = torch.device("cuda" if torch.cuda.is_available else "cpu")
#model.to(device)



input_ids = tokenizer.apply_chat_template(conversation=messages, tokenize=True, add_generation_prompt=True, return_tensors='pt')
output_ids = model.generate(input_ids.to('cuda'))
# print(model.chat(tokenizer, '你好', history=None)[0])
response = tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True)

# Model response: "Hello! How can I assist you today?"
print(response)
```

```python
# load lora model 
lora_dir= 'model/ft_model/yi_lora_0419'



```

```
 output = model.generate(
        **input,
        max_new_tokens=max_new_tokens,
        num_beams=1,
        do_sample=False,
        temperature=temperature,
    )[0]
```

