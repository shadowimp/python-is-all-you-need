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
```



```
# int 4 量化
model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True).quantize(4).half().cuda()

# Quantization rely on cpm_kernels. Install it by:
pip install cpm_kernels
```



```
# 参数
Maximum length  ： 输入最大长度，一般为2048
Temperature ： 	调整softmax函数的输出，调节不同类别的置信度
T=0.05 ,model倾向于选择概率最大的类别输出
T=0.95 ，model更不稳定，倾向于输出多个类别


temperature
top_p


top_k: 整数,大于1的数
越大，生成的多样性更大， 越小生成的越固定

temperature 越大，输出结果的随机性越大，

Top-k采样：限制模型在生成下一个词时只考虑概率最高的k个词，这有助于避免生成低概率的词汇，提高文本的连贯性和可读性。


Top-p采样（Nucleus Sampling）：与top-k类似，top-p采样确保所有选择的词汇的累积概率不超过一个给定的阈值（top_p），这有助于生成更加多样化的文本。


Maximum length 参数

通常用于限制输入序列的最大长度，因为 ChatGLM-6B 是 2048 长度推理的，一般这个保持默认就行，太大可能会导致性能下降。
```

