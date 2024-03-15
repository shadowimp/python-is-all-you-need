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

```

