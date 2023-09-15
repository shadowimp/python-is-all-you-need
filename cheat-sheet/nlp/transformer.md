### self attention

$$V = Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_k}})*V$$

```python
from math import sqrt 
import torch
import torch.nn as nn

```



```python
def attention(query:Tensor , key:Tensor ,value:Tensor, mask,dropout ):
  k_dim = query.size(-1)
  scores = torch.matmul(query, key.transpose(-2,-1))/math.sqrt(k_dim)
  if mask is not None :
    scores = scores.masked_fill(mask == 0 , -1e10)
  attention_score = F.softmax(score, dim=-1)
  
  if dropout if not None :
    attention_score = dropout(attention)
  out = 

```