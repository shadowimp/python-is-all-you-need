







```
https://huggingface.co/THUDM/chatglm3-6b
https://github.com/THUDM/ChatGLM3

git clone https://github.com/THUDM/ChatGLM3.git
```

```
# huggingface 国内镜像站， https://hf-mirror.com
vim ~/.bashrc
export HF_ENDPOINT="https://hf-mirror.com"
```





```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True).half().cuda()
# 
response = model.chat(tokenizer, "你好")
response, history = model.chat(tokenizer, "你好", history=history)


from transformers import AutoTokenizer , AutoModel
tokenizer = AutoTokenizer.from_pretrained('THUDM/chatglm-6b',trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b",trust_remote_code=True).half().cuda()
model = model.eval()
response,history  = model.chat(tokenizer ,'hello',histroy=[])
print(response)
response,history  = model.chat(tokenizer ,'晚上睡不着应该怎么办',histroy=history)
print(response)
```



```python
# int 4 量化
model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True).quantize(4).half().cuda()

# Quantization rely on cpm_kernels. Install it by:
pip install cpm_kernels


# 4 bit quantize 
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
quantize_config = BaseQuantizeConfig(bits=4, group_size=128,desc_act=False,)
model =   AutoGPTQForCausalLM.from_pretrained(model_dir,quantize_config)
# infer
output_ids = self.yi_model.generate(input_ids=input_ids.to('cuda'),max_new_tokens=200)
```





```
# 参数
Maximum length  ： 输入最大长度，一般为2048
Maximum length 参数
通常用于限制输入序列的最大长度，因为 ChatGLM-6B 是 2048 长度推理的，一般这个保持默认就行，太大可能会导致性能下降。


Temperature ： 	调整softmax函数的输出，调节不同类别的置信度
T=0.05 ,model倾向于选择概率最大的类别输出
T=0.95 ，model更不稳定，倾向于输出多个类别
temperature 越大，输出结果的随机性越大，


Top-k采样：限制模型在生成下一个词时只考虑概率最高的k个词，这有助于避免生成低概率的词汇，提高文本的连贯性和可读性。
top_k: 整数,大于1的数
越大，生成的多样性更大， 越小生成的越固定


Top-p采样（Nucleus Sampling）：与top-k类似，top-p采样确保所有选择的词汇的累积概率不超过一个给定的阈值（top_p），这有助于生成更加多样化的文本。
top_p: 0-1:
将 top-p 设定为 0.15，即选择前 15% 概率的 tokens 作为候选。如下图所示，United 和 Netherlands 的概率加起来为 15% ，所以候选词就是这俩，最后再从这些候选词里，根据概率分数，选择 united 这个词。
Top-p is usually set to a high value (like 0.75) with the purpose of limiting the long tail of low-probability tokens that may be sampled. We can use both top-k and top-p together. If both k and p are enabled, p acts after k.






unk_token: 不存在词典里的字符.
```

```
model.chat(tokenizer, prompt, history=[],do_sample=True, max_length=300, top_k=30,top_p=0.95)
```

https://zhuanlan.zhihu.com/p/648074941?utm_id=0



hf-mirror:

https://hf-mirror.com/THUDM/chatglm3-6b