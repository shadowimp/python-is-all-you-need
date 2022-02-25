### warmup

训练初期使用较小的学习率，从0开始慢慢增加，避免模型过早进入局部最优从而过拟合.

训练后期慢慢降低学习率，避免后期训练参数较大变化,帮助模型收敛。

```
TYPE_TO_SCHEDULER_FUNCTION = {
    SchedulerType.LINEAR: get_linear_schedule_with_warmup,
    SchedulerType.COSINE: get_cosine_schedule_with_warmup,
    SchedulerType.COSINE_WITH_RESTARTS: get_cosine_with_hard_restarts_schedule_with_warmup,
    SchedulerType.POLYNOMIAL: get_polynomial_decay_schedule_with_warmup,
    SchedulerType.CONSTANT: get_constant_schedule,
    SchedulerType.CONSTANT_WITH_WARMUP: get_constant_schedule_with_warmup,
}

get_linear_scheduler_with_warmup:
COSINE：和两段式调整类似，只不过采用的是三角函数式的曲线调整；
```

```python
lr_scheduler = get_linear_schedule_with_warmup(optimizer=opti, num_warmup_steps=num_warmup_steps, num_training_steps=t_total)
```



### 梯度累计

batch size小会导致较少的样本会造成loss的波动，影响模型收敛

梯度累计： 多个batch后，统一回传梯度，达到同大batch size的效果

```python
iters_to_accumulate = 2  # the gradient accumulation adds gradients over an effective batch of size : bs * iters_to_accumulate. If set to "1", you get the usual batch size

loss.backward()
if (it + 1) % iters_to_accumulate == 0:
  optim.zero_grad()
  optim.step()
  lr_scheduler.step()
  
  
```





### model.eval()

model.eval( ) 能够在模型验证（evaluation）和预测阶段将Dropout 和BN层设置到预测模式

```python
def evaluate_loss(net, device, criterion, dataloader):
    model.eval()

    mean_loss = 0
    count = 0

    with torch.no_grad():
        for it, (seq, attn_masks, token_type_ids, labels) in enumerate(tqdm(dataloader)):
            seq, attn_masks, token_type_ids, labels = \
                seq.to(device), attn_masks.to(device), token_type_ids.to(device), labels.to(device)
            logits = net(seq, attn_masks, token_type_ids)
            mean_loss += criterion(logits.squeeze(-1), labels.float()).item()
            count += 1

    return mean_loss / count
```



### Dropout

我们在前向传播的时候，让某个神经元的激活值以一定的概率p停止工作，这样可以使模型泛化性更强，因为它不会太依赖某些局部的特征，相当于输入每次走过不同的“模型”。

比如，有1000个神经元，p=0.4，我们dropout比率选择0.4，在训练的时候，这一层神经元经过dropout后，1000个神经元中会有大约400个的值被置为0。

测试时，应该用整个训练好的模型，因此不需要dropout。

在测试中，对每个神经元的输出乘以p，能够将output的训练值和预测值rescale到同一维度。



### Batch Normalization

BN是对数据的规范化，使每层的数据输入都保持在相近的范围内。

在训练时，由于是一个batch一个batch的给模型投喂数据，模型只能计算当前batch的均值和方差，当所有的batch都投喂完成，模型对每个batch上的均值和方差做指数平均，来得到整个样本上的均值和方差的近似值。

训练是基于batch的，而预测是单个单个预测，预测是不存在batch的概念。因此会直接拿训练过程中对整个样本空间估算的均值和方差直接来用。



### shuf data

train_loader = DataLoader(train_set, batch_size=16, shuffle=False,num_workers=2) 



### fassi

```
Faiss 相似度搜索使用余弦相似性:
https://www.cxyzjd.com/article/flyfish1986/108012151
```



```python
# tensor to list
data = torch.zeros(3,3)
data = data.tolist()
```



