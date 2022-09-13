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



### bert pretrain

-   `output_dir`: *The output directory where the model predictions and checkpoints will be written. I set it up to `pretrained_bert_model` where the model and will be saved.*
-   `overwrite_output_dir`: *Overwrite the content of the output directory. I set it to `True` in case I run the notebook multiple times I only care about the last run.*
-   `do_train`: *Whether to run training or not. I set this parameter to `True` because I want to train the model on my custom dataset.*
-   `do_eval`: *Whether to run evaluation on the evaluation files or not. I set it to `True` since I have test data file and I want to evaluate how well the model trains.*
-   `per_device_train_batch_size`: *Batch size GPU/TPU core/CPU training. I set it to `2` for this example. I recommend setting it up as high as your GPU memory allows you.*
-   `per_device_eval_batch_size`: *Batch size GPU/TPU core/CPU for evaluation.I set this value to `100` since it's not dealing with gradients.*
-   `evaluation_strategy`: *Evaluation strategy to adopt during training: `no`: No evaluation during training; `steps`: Evaluate every `eval_steps;`epoch`: Evaluate every end of epoch. I set it to 'steps' since I want to evaluate model more often.*
-   `logging_steps`: *How often to show logs. I will se this to plot history loss and calculate perplexity. I set this to `20` just as an example. If your evaluate data is large you might not want to run it that often because it will significantly slow down training time.*
-   `eval_steps`: *Number of update steps between two evaluations if evaluation_strategy="steps". Will default to the same value as logging_steps if not set. Since I want to evaluate model ever`logging_steps` I will set this to `None` since it will inherit same value as `logging_steps`.*
-   `prediction_loss_only`: *Set prediction loss to `True` in order to return loss for perplexity calculation. Since I want to calculate perplexity I set this to `True` since I want to monitor loss and perplexity (which is exp(loss)).*
-   `learning_rate`: *The initial learning rate for Adam. Defaults is set to `5e-5`.*
-   `weight_decay`: *The weight decay to apply (if not zero)Defaults is set to `0`.*
-   `adam_epsilon`: *Epsilon for the Adam optimizer. Defaults to `1e-8`.*
-   `max_grad_norm`: *Maximum gradient norm (for gradient clipping). Defaults to `0`.*
-   `num_train_epochs`: *Total number of training epochs to perform (if not an integer, will perform the decimal part percents of the last epoch before stopping training). I set it to `2` at most. Since the custom dataset will be a lot smaller than the original dataset the model was trained on we don't want to overfit.*
-   `save_steps`: *Number of updates steps before two checkpoint saves. Defaults to `500`.*

```
http://haokailong.top/2020/12/21/利用预训练语言模型计算句子相似度/
```





```python
net = ResNet()
loss = MSE()
optimizer = torch.optim.SGD(net.parameters(), lr=0.001)
""" 中断后，加载权重继续训练 """ 
checkpoint = torch.load("model_path/model.pth") 
current_epoch = checkpoint["epoch"] 
net.load_state_dict(checkpoint['net']) 
optimizer.load_state_dict(checkpoint['optimizer']) 
net.train()
for epoch in range(current_epoch , total_epochs):
   ...
   for x, y in dataloader:
       ...
       loss = ...
       loss.backward()
       optimizer.step()
   state_dict = {"net": net.state_dict(), "optimizer": optimizer.state_dict(), "epoch": epoch}
   torch.save(state_dict, "model_path/model.pth")
    
```





加载transformer预训练模型

```python
下载bert-base-chinese的
config.josn，vocab.txt，pytorch_model.bin三个文件后，
放在bert-base-chinese文件夹下，
此例中该文件夹放在目下下。


import numpy as np
import torch 
from transformers import BertTokenizer, BertConfig, BertForMaskedLM, BertForNextSentencePrediction
from transformers import BertModel

model_name = 'bert-base-chinese'
MODEL_PATH = './bert-base-chinese/'

# 加载分词器
tokenizer = BertTokenizer.from_pretrained(model_name)
# 导入配置文件
model_config = BertConfig.from_pretrained(model_name)
# 修改配置
model_config.output_hidden_states = True
model_config.output_attentions = True
# 通过配置和路径导入模型
bert_model = BertModel.from_pretrained(MODEL_PATH, config = model_config)


```



tokenizer

```python
# encode仅返回input_ids
tokenizer.encode('手机')

>> [101, 2797, 3322, 102]

# encode_plus 返回 input_ids(词典编码位置) , token_type_ids(上句为0，下句为1), attention_mask ：对哪些词进行self-attention

tokenizer.encode_plus('手机')

>> {'input_ids': [101, 2797, 3322, 102], 
    'token_type_ids': [0, 0, 0, 0], 
    'attention_mask': [1, 1, 1, 1]}

tokenizer.encode_plus('手机','电脑')
>> {'input_ids': [101, 2797, 3322, 102, 4510, 5554, 102], 
    'token_type_ids': [0, 0, 0, 0, 1, 1, 1], 
    'attention_mask': [1, 1, 1, 1, 1, 1, 1]}

#  convert_ids_to_tokens 将 编码变回文字
tokenizer.convert_ids_to_tokens(sen_code['input_ids'])
```



### hfl/chinese-roberta-wwm-ext

```python


from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("hfl/chinese-roberta-wwm-ext")

model = AutoModelForMaskedLM.from_pretrained("hfl/chinese-roberta-wwm-ext")


```



```
# 特殊token
{"unk_token": "[UNK]", # 未知字符
"sep_token": "[SEP]",  # 分隔两个句子
"pad_token": "[PAD]",   
"cls_token": "[CLS]", # 
"mask_token": "[MASK]"}




```

0421: 918/2000 = 0.459

0422:905/2000 =0.452



### torch pth 文件转pt

Pytorch的模型文件一般会保存为.pth文件，C++接口一般读取的是.pt文件，利用pytorch提供的函数torch.jit.trace进行转换

```python
import torch
example = (torch.tensor(torch.ones(1, 128), dtype=torch.long).to(device), torch.tensor(torch.ones(1, 128), dtype=torch.long).to(device),torch.tensor(torch.ones(1, 128), dtype=torch.long).to(device))
traced_script_module = torch.jit.trace(model, example)
traced_script_module.save('rbt3_model.pt')
```





RuntimeError: xxx.pth is a zip archive(did you mean to use torch.jit.load()?)



`xxx.pth`来自pytorch1.6或更高的版本。1.6之后pytorch默认使用zip文件格式来保存权重文件，导致这些权重文件无法直接被1.5及以下的pytorch加载。



state_dict = torch.load("xxx.pth") 

torch.save(state_dict, "xxx.pth", _use_new_zipfile_serialization=False)



### 加速



使用半精度，将pytorch默认的float32 改成 float16  ，加快推理速度， 减少显存占用

model.half()  

model.cuda()

model.eval()



输入也应改为半精度

img = torch.from_numpy(image).float()

img = img.cuda()

img = img.half()







###  no_grad







