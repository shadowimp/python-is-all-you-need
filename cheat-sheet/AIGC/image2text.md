```python
from PIL import Image
import numpy as np
image_path = '/Users/zhengjia/Desktop/WechatIMG8.png'
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

