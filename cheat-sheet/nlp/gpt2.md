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

