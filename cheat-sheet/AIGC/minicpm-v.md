```
conda create -n MiniCPM-V python=3.10 -y
conda activate MiniCPM-V
# install
Pillow==10.1.0
torch==2.1.2
torchvision==0.16.2
transformers==4.40.0
sentencepiece==0.1.99
```



```python
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer


model_path = 'openbmb/MiniCPM-Llama3-V-2_5'
model = AutoModel.from_pretrained(model_path, trust_remote_code=True, torch_dtype=torch.float16)

model = model.to(device='cuda')

tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True)
model.eval()

image_path = ''
image = Image.open(image_path).convert('RGB')



question = '识别图中的文字'
question = '根据图片中的内容，创作一个小红书文案风格的广告'
question = '识别图中的实体'
question = '识别图中的广告类型'
question = '给图片分类： 1.食品生鲜 2.婚恋交友  3.文化娱乐 4.婚庆摄影 5.医疗保健'
msgs = [{'role': 'user', 'content': question}]
res = model.chat(
    image=image,
    msgs=msgs,
    tokenizer=tokenizer,
    sampling=True, # if sampling=False, beam_search will be used by default
    temperature=0.7,
    # system_prompt='' # pass system_prompt if needed
)
print(res)



```

