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













