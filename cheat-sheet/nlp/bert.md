### Bert (Bidirectional Encoder Representions form Transformers )

### 参数量

词表长度3w， embeding 维度 768 。

[BERT-base](https://zhida.zhihu.com/search?content_id=195736300&content_type=Article&match_order=1&q=BERT-base&zhida_source=entity)的参数量是110M，[BERT-large](https://zhida.zhihu.com/search?content_id=195736300&content_type=Article&match_order=1&q=BERT-large&zhida_source=entity)的参数量是340M。

BERT-BASE (L=12, H=768, A=12, Total Parameters=110M)



**embedding 层：** 

Bert采用的词表长度 |V| 为30522

hidden_size即[embedding长度](https://zhida.zhihu.com/search?content_id=195736300&content_type=Article&match_order=1&q=embedding长度&zhida_source=entity) E 为768（论文中的 H)

S： 块向量（Segment Embeddings），

N：序列最大长度 N 为512（They are sampled such that the combined length is ≤ 512 tokens）；

 参数量 = V * E  + S *E + N * E = （30522 + 2 + 512) * 768



**multi-head attention layer** 

$$Attention(Q,K,V) = softmax(\frac {QK^T} {\sqrt{d_k}})V$$

Bert采用了12头self-attention. 

论文中 dmodel 即hidden_size，768。

768*768/ 

Q ,K,V的参数维度相同:  e*d_k  均为    (64,768 )

12个head拼接后 ： 12 * 64 * 768





FFN ， feed forward network 

包括两个全连接层。

 feed-forward/filter size to be 4H = 4*768 = 3072

$$ FFN(x)=max(0,xW_1+b_1)W_2+b_2$$



```
768*3072 + 3072 + 3072*768 + 768
```













### BertClient

Bert-serving可以直接调用谷歌训练好的字向量，然后很轻松就可以生成我们需要的词向量

```python
from bert_serving.client import BertClient
bc = BertClient()
bc.encode(['First do it', 'then do it right', 'then do it better'])
```









### bert 与 gpt的不同:

1、训练任务不同：

bert ： mlm任务 随机mask词 做预测，nsp任务 判断两个句子是否连续

gpt: 单向自回归预训练，仅依赖于已生成的文本上下文来预测下一个词

2、架构不同，

bert ： 双向encoder，model同时考虑上下文信息  ， sft时通常将cls向量送入分类器，

gpt:  单向decoder  only， 没有encoder， 依赖单向信息。 每个词的生成只依赖于它之前的词。



### T5和gpt的区别：

T5： encoder + decoder架构，可以接收双向的上下文信息 ，而解码器在生成过程中虽然不能直接看到未来的信息（通过掩码机制避免），但因为有编码器的输入，间接地利用了双向信息。

多种任务预训练，能够适应多种任务。

T5的推理过程可能在某些情况下更高效，因为它只需要对输入进行一次编码，而生成时的解码过程可以更聚焦。

GPT ： decoder only 。去除了编码器部分，简化了模型结构，使得模型更易于训练和理解。GPT-3 通过其 Decoder 层处理输入序列。输入数据（如一段文本）首先被转换为[词嵌入](https://www.zhihu.com/search?q=词嵌入&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A3379518716})，然后加上[位置编码](https://www.zhihu.com/search?q=位置编码&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A3379518716})，之后通过多个 Decoder 层进行处理。在每个 Decoder 层中，GPT-3 使用掩蔽（masked）的自注意力机制，这确保在生成每个词时，模型只能考虑到之前的词（即保持自回归性质）。

GPT-3 在大量多语言文本上进行预训练，这使得它能够理解和生成多种语言。即使它没有专门的编码器来处理输入语言，它仍然能够通过其大规模的训练数据理解不同语言之间的关联。

GPT每次生成新词时都要处理到目前为止生成的所有词，这在计算上可能更昂贵







### bert 先验技术分享



**Masked Language Modeling（MLM）**和**Next Sentence Prediction （NSP）**

MRPC [11] is a corpus of sentence pairs with artificial an- notations automatically extracted from online news sources

### 全词掩码（Whole Word Masking

将随机掩码词汇替换成全词掩码，可以有效提高预训练模型效果，即**如果有一个汉字被掩蔽，属于同一个汉字的其他汉字都被掩蔽在一起**。



[Pre-Training with Whole Word Masking for Chinese BERT](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/1906.08101)



华为Noah’s Ark Lab
NEZHA: NEURAL CONTEXTUALIZED REPRESENTATION FOR CHINESE LANGUAGE UNDERSTANDING

https://arxiv.org/pdf/1909.00204.pdf



wobert （Word-based BERT）追一科技 苏剑林

https://huggingface.co/junnyu/wobert_chinese_plus_base

https://kexue.fm/archives/7758/comment-page-2#comments

BERT自带的Tokenizer会强行把中文字符用空格隔开，因此就算你把词加入到字典中，也不会分出中文词来。此外，BERT做英文word piece的分词的时候，使用的是最大匹配法，这对中文分词来说精度也不够。

为了分出词来，我们修改了一下BERT的Tokenizer，**加入了一个“前分词（pre_tokenize）”操作**，这样我们就可以分出中文词来，具体操作如下：

>   1、把中文词加入到vocab.txt； 
>   2、输入一个句子![[公式]](https://www.zhihu.com/equation?tex=s)，用pre_tokenize先分一次词，得到![[公式]](https://www.zhihu.com/equation?tex=%5Bw_1%2Cw_2%2C%5Cdots%2Cw_l%5D)；
>   3、遍历各个![[公式]](https://www.zhihu.com/equation?tex=w_i)，如果![[公式]](https://www.zhihu.com/equation?tex=w_i)在词表中则保留，否则将![[公式]](https://www.zhihu.com/equation?tex=w_i)用BERT自带的tokenize函数再分一次；
>   4、将每个![[公式]](https://www.zhihu.com/equation?tex=w_i)的tokenize结果有序拼接起来，作为最后的tokenize结果。

目前开源的WoBERT是Base版本，在哈工大开源的[RoBERTa-wwm-ext](https://github.com/ymcui/Chinese-BERT-wwm)基础上进行继续预训练，预训练任务为MLM。初始化阶段，将每个词用BERT自带的Tokenizer切分为字，然后用字embedding的平均作为词embedding的初始化。模型使用单张24G的RTX训练了100万步（大概训练了10天），序列长度为512，学习率为5e-6，batch_size为16，累积梯度16步，相当于batch_size=256训练了6万步左右。训练语料大概是30多G的通用型语料。速度和精度相对于bert都有提升.





### BERT微调效果不佳？不如试试这种大规模预训练模型新范式

https://mp.weixin.qq.com/s/YSyRUyhhq4N2T6iUuOmgDg

在pretraining + finetuning  中间加入一个阶段：

在特定领域进行pre-training



### bert sim模型究竟要解决的什么问题



bert优势： 能学到上下文的语义信息。

0，1，2

解决目前按行业召回无法解决的问题，

其他行业的广告中有语义信息和query高度匹配的广告





bert pretrain ：

http://haokailong.top/2020/12/21/利用预训练语言模型计算句子相似度/

https://zhuanlan.zhihu.com/p/414384344



http://haokailong.top/2020/12/21/利用预训练语言模型计算句子相似度/







Bert句[向量空间](https://www.zhihu.com/search?q=向量空间&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A"444346578"})的各向异性:

原生的bert不适合句向量的生成。

Bert 词向量， 在向量空间分布不均匀，词之间的距离不能很好的表征相关性。



 sentence bert：







### bert快速搭框架

```python
import re
import numpy as np
import pandas as pd
import transformers
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader, RandomSampler, SequentialSampler
from transformers import BertTokenizer, BertModel, BertConfig, AutoTokenizer
from transformers import AdamW
from transformers import get_linear_schedule_with_warmup
from tqdm import tqdm
import gc
from torch import cuda
import datetime
import time
import argparse
import os
import torch.optim as optim

from transformers import logging

logging.set_verbosity_warning()
logging.set_verbosity_error()

MAX_LEN = 256
TRAIN_BATCH_SIZE = 16
VALID_BATCH_SIZE = 16
LEARNING_RATE = 0.00001
EPOCHS = 10

MODEL_NAME = "hfl/chinese-roberta-wwm-ext"
os.environ["CUDA_VISIBLE_DEVICES"]="2"
device = 'cuda' if cuda.is_available() else 'cpu'
device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
device

```

```python
class Classifier(torch.nn.Module):
    def __init__(self):
        super(Classifier, self).__init__()
        self.dense1 = torch.nn.Linear(768, 256)
        self.dense2 = torch.nn.Linear(256, 1)
        self.activation = torch.nn.Tanh()
        self.dropout = torch.nn.Dropout(0.1)
        
        
    def forward(self, x):
        x = self.dropout(x)
        x = self.dense1(x)
        x = self.activation(x)
        x = self.dropout(x)
        x = self.dense2(x)
        return x

class BertSim(torch.nn.Module):
    def __init__(self):
        super(BertSim, self).__init__()
        self.bert = transformers.BertModel.from_pretrained(MODEL_NAME)
        self.classifier = Classifier()
        
    def forward(self, input_ids, attention_mask, token_type_ids):
        _, output_1= self.bert(input_ids=input_ids, attention_mask = attention_mask, token_type_ids = token_type_ids, return_dict=False)
        output = self.classifier(output_1)
        return output
```



```python
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = BertSim()
model.to(device)
optim = AdamW([
    {'params': model.bert.parameters()},
    {'params':model.classifier.parameters(), 'lr':LEARNING_RATE*10}],
    lr=LEARNING_RATE)
criterion = nn.MSELoss()


```



```python
class CustomDataset(Dataset):

    def __init__(self, data, tokenizer, max_len, with_labels=True):
        self.tokenizer = tokenizer
        self.data = data
        self.max_len = max_len
        self.with_labels = with_labels

    def __len__(self):
        return len(self.data)
    
    def text_normal_l1(self, text):
        rule_url = re.compile('(https?://)?(www\\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b([-a-zA-Z0-9()@:%_+.~#?&/=]*)')
        rule_legal = re.compile('[^\\[\\]@#a-zA-Z0-9\u4e00-\u9fa5]')
        rule_space = re.compile('\\s+')
        text = str(text).replace('\\n', ' ').replace('\n', ' ').strip()
        text = rule_url.sub(' ', text)
        text = rule_legal.sub(' ', text)
        text = rule_space.sub(' ', text)
        return text.strip()

    def __getitem__(self, index):
        sent1 = self.text_normal_l1(str(self.data.loc[index,'query1']))
        sent2 = self.text_normal_l1(str(self.data.loc[index,'query2']))
        
        encoded_pair = self.tokenizer(sent1, sent2, 
                                      padding='max_length',  # Pad to max_length
                                      truncation=True,  # Truncate to max_length
                                      max_length=self.max_len,  
                                      return_tensors='pt') 
        token_ids = encoded_pair['input_ids'].squeeze(0) 
        attn_masks = encoded_pair['attention_mask'].squeeze(0)
        token_type_ids = encoded_pair['token_type_ids'].squeeze(0)
        
        if self.with_labels:  # True if the dataset has labels
            sim_score = float(self.data.loc[index,'sim_score'])
            return token_ids, attn_masks, token_type_ids, sim_score
        else:
            return token_ids, attn_masks, token_type_ids
```











