### self attention

$$V = Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_k}})*V$$

```python
from math import sqrt 
import torch
import torch.nn as nn
```

```python
def clones(module, N):
  return nn.ModuleList([copy.deepcopy(module) for i in range(N)])

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

### multi-head attention

```python
from math import sqrt
import torch 
import torch.nn as nn 

class MultiHeadedAttention(nn.Module):
    def __init__(self, h, d_model, dropout = 0.1):
        super(MultiHeadedAttention,self).__init__()
        assert d_model %h == 0 
        self.d_k = d_model
        self.h = h
        self.linears = clones(nn.Linear(d_model,d_model),4)
        self.attn = None 
        self.dropout = nn.Dropout(p=dropout)

    def forword(self, q,k,v, mask =None):
        if mask is not None:
            mask = mask.unsqueeze(1)
        n_batch = q.size(0)

        q,k,v = [l(x).view(n_batch, -1, self.h,self.d_k).transpose(1,2) for l,x in zip(self.linears,(q,k,v))]

        x, self.attn = attention(q,k,v ,mask = mask, dropout=self.dropout)
        x = x.transpose(1,2).contiguous().view(n_batch, -1 , self.h*self.d_k)
        return self.linears[-1](x)
```

