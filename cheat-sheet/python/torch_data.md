### squeeze  and unsqueeze 

```
torch.squeeze()函数的作用减少数组A指定位置N的维度，如果不指定位置参数N，如果数组A的维度为（1，1，3）那么执行 torch.squeeze(A，1) 后A的维度变为 （1，3），中间的维度被删除

注：
1. 如果指定的维度大于1，那么将操作无效
2. 如果不指定维度N，那么将删除所有维度为1的维度


torch.unsqueeze(A，N)torch.unsqueeze()函数的作用增加数组A指定位置N的维度，例如两行三列的数组A维度为(2，3)，那么这个数组就有三个位置可以增加维度，分别是（ [位置0] 2，[位置1] 3 [位置2] ）或者是 （ [位置-3] 2，[位置-2] 3 [位置-1] ），如果执行 torch.unsqueeze(A，1)，数据的维度就变为了 （2，1，3）

```

```python
a=torch.randn(1,1,3)
print(a.shape)  # (1,1,3)
b=torch.squeeze(a)
print(b.shape)  # (3)
c=torch.squeeze(a,0)  
print(c.shape)   # (1,3)
d=torch.squeeze(a,1)
print(d.shape)    # (1,3)
e=torch.squeeze(a,2)#如果去掉第三维，则数不够放了，所以直接保留
print(e.shape)    #(1,1,3)



a=torch.randn(1,3)
print(a.shape)  # (1,3)
b=torch.unsqueeze(a,0)
print(b.shape)  # (1,1,3)
c=torch.unsqueeze(a,1)
print(c.shape) # (1,1,3)
d=torch.unsqueeze(a,2)
print(d.shape)    # (1,3,1)
```





### one-hot

convert label index to onehot vector and back 

```python
import torch
import numpy as np


# labels --> one-hot  5类，label为0
a = torch.tensor([0])
a_v = torch.nn.functional.one_hot(a, num_classes=5)

# labels --> one-hot 
one_hot = torch.nn.functional.one_hot(target)
# one-hot --> labels
labels_again = torch.argmax(one_hot, dim=1)

np.testing.assert_equals(labels.numpy(), labels_again.numpy())
```