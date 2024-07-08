ft-data

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

