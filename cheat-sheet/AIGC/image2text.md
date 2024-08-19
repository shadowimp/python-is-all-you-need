### chatglm-4v-9b.md



```python
import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"

tokenizer = AutoTokenizer.from_pretrained("THUDM/glm-4v-9b", trust_remote_code=True)

query = '描述这张图片'
image = Image.open("your image").convert('RGB')
inputs = tokenizer.apply_chat_template([{"role": "user", "image": image, "content": query}],
                                       add_generation_prompt=True, tokenize=True, return_tensors="pt",
                                       return_dict=True)  # chat mode

inputs = inputs.to(device)
model = AutoModelForCausalLM.from_pretrained(
    "THUDM/glm-4v-9b",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True
).to(device).eval()

gen_kwargs = {"max_length": 2500, "do_sample": True, "top_k": 1}
with torch.no_grad():
    outputs = model.generate(**inputs, **gen_kwargs)
    outputs = outputs[:, inputs['input_ids'].shape[1]:]
    print(tokenizer.decode(outputs[0]))
```













```python
from PIL import Image
import numpy as np
image_path = '/WechatIMG8.png'
img1 = Image.open(image_path)
print('img1的mode为{}'.format(img1.mode))
print('img1的size为{}'.format(img1.size))
print('img1的format为{}'.format(img1.format))
print('img1的shape为{}'.format(np.array(img1).shape))


image = Image.open(requests.get(url, stream=True).raw)


```



### IDEA-CCNL/Taiyi-vit-87M-D

https://huggingface.co/IDEA-CCNL/Taiyi-vit-87M-D

```python
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import requests

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = ViTFeatureExtractor.from_pretrained('IDEA-CCNL/Taiyi-vit-87M-D')
model = ViTForImageClassification.from_pretrained('IDEA-CCNL/Taiyi-vit-87M-D')

inputs = feature_extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
# model predicts one of the 1000 ImageNet classes
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
# Predicted class: Egyptian cat

```

