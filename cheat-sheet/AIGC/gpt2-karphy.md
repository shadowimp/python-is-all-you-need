### data 

tinyshakespeare

```
!wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
```

```python
with open('input.txt','r', encoding='utf-8') as f:
    text = f.read()
chars = sorted(list(set(text)))
vocab_size = (len(chars))
print(chars)
print(vocab_size)

>> 
['\n', ' ', '!', '$', '&', "'", ',', '-', '.', '3', ':', ';', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
65

stoi = { ch:i for i,ch in enumerate(chars) }
itos = { i:ch for i,ch in enumerate(chars) }
def encode(s):
    return [stoi[c] for c in s] # encoder: take a string, output a list of integers
def decode(l):
    return ''.join([itos[i] for i in l]) # decoder: take a list of integers, output a string
  
```

``` python
data = torch.tensor(encode(text), dtype=torch.long)
data.shape, data.dtype  ## (torch.Size([1115394]), torch.int64) 

# split data to train and val 
n = int(0.9*len(data))
train_data = data[:n]
val_data = data[n:]
 
### data block chunk and  batch 

block_size = 8
train_data[:block_size+1]
torch.manual_seed(1337)

batch_size = 4
block_size = 8


ix = torch.randint(len(data)-block_size, (batch_size,))
ix

def get_batch(split):
    data = train_data if split =='train' else val_data
    ix = torch.randint(len(data)-block_size, (batch_size,))
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+block_size+1] for i in ix])
    return x, y 
  
xb,yb = get_batch('train')

for b in range(batch_size):
    for t in range(block_size):
        context = xb[b, :t+1]
        target = yb[b,t]
        print(f"input:{context.tolist()}, output:{target} ")
>> 
input:[53], output:56 
input:[53, 56], output:1 
input:[53, 56, 1], output:61 
input:[53, 56, 1, 61], output:43 
input:[53, 56, 1, 61, 43], output:39 
input:[53, 56, 1, 61, 43, 39], output:56 
input:[53, 56, 1, 61, 43, 39, 56], output:47 
input:[53, 56, 1, 61, 43, 39, 56, 47], output:52 




```

## model

```python
import torch
import torch.nn as nn 
from torch.nn import functional as F
torch.manual_seed(1337)

class BigramLanguageModel(nn.Module):

    def __init__(self, vocab_size):
        super().__init__()
        # each token directly reads off the logits for the next token from a lookup table
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

    def forward(self, idx, targets=None):
        # idx and targets are both (B,T) tensor of integers, idx and targets are both (B,T) tensor of integers
        logits = self.token_embedding_table(idx) # (B,T,C)
        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)   # (B*T,C)
            targets = targets.view(B*T)    
            loss = F.cross_entropy(logits, targets)
        return logits, loss

    def generate(self, idx, max_new_tokens):
        # idx is (B, T) array of indices in the current context
        for _ in range(max_new_tokens):
            # get the predictions
            logits, loss = self.forward(idx)   # ：当执行model(x)的时候，底层自动调用forward方法计算结果
            # focus only on the last time step
            logits = logits[:, -1, :] # becomes (B, C)  取第二维的最后一个元素
            # print(logits.shape)
            # apply softmax to get probabilities
            probs = F.softmax(logits, dim=-1) # (B, C)
            # sample from the distribution
            idx_next = torch.multinomial(probs, num_samples=1) # (B, 1)
            # append sampled index to the running sequence
            idx = torch.cat((idx, idx_next), dim=1) # (B, T+1)
        return idx


```

```python
print(vocab_size)  # 65 
model = BigramLanguageModel(vocab_size)
logits , loss = model(xb, yb)
print(logits.shape)   # orch.Size([32, 65])
print(loss)   # tensor(4.7879, grad_fn=<NllLossBackward>)


### generate
idx = torch.zeros((1,1), dtype=torch.long)
out_idx = model.generate(idx  , max_new_tokens= 100)
decode(out_idx[0].tolist())
>> "\nt$HsPh'JaH;VtouIuAliN' Mw,DfUf:peYbv!PiVOZm!URmRmPKd?vg?sM3M?umF3obmjhdzP mBcCH KCaQm OfYVsBKBC'.&EI"
# 因为没有训练，所以推理出的是随机的str

```

## train model



```python 3
### optimizer  
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)


# train 
train_steps  = 10000
for step in range(train_steps):
    xb, yb = get_batch('train')
    logits, loss = m(xb, yb)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print(loss.item())


### generate from trained model 
idx = torch.zeros((1,1), dtype=torch.long)
out_idx = model.generate(idx  , max_new_tokens= 100)
decode(out_idx[0].tolist())
>> '\nD?PFXLTIdm'


```



以上是一个文本推理模型的最简单实现，效果较差， 接下来使用加入attention 

## self-attention



```
query text 
```

### CausalSelfAttention

这是一个[自注意力机制](https://www.zhihu.com/search?q=自注意力机制&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A3541129225})的实现，用于计算输入序列中每个位置的注意力权重，确保当前位置只关注之前的位置（因果自注意力）。



### MLP-[多层感知机]

神经网络结构，用于处理从注意力机制输出的数据



Block 

一个Transformer模块，包括一个自注意力层和一个MLP层，并且使用层归一化。



GPTConfig

定义gpt的参数， 包括 ，



```python
class CausalSelfAttention(nn.Module):
  def __init__(self,config):
    super.

```

