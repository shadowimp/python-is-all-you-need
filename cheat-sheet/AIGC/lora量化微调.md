### 量化(Quantization

数据:高精度(比如float32压缩到低精度(比如4位整数)的技术。

float32 - > int 8  显存占用减少4倍

float32（4字节）

int8 （1字节） 

N=6b（对于6B模型），那么： 

int8 存储: 6B字节 ： 6G

float32 存储： 6B*4 = 24g



Adam优化器:除了参数和梯度外，它还需要为每个参数维护两个额外的状态变量：一阶矩估计和[二阶矩估计](https://www.zhihu.com/search?q=二阶矩估计&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"3534428197"})。这两个状态变量与参数的维度相同，因此Adam的内存占用约为：3×模型参数内存。

训练 yi-6b ： 显存  3*6 = 18g







## 模型： 

LLama2 ，Chatglm , Qwen ,  Yi 

广告创意领域综合测试采用Yi-6B模型

int8 量化下，模型存储: 6B字节 ： 6G。  ( 如果 int4 量化，则需要3g存储 )

训练 yi-6b ： 显存  3*6 = 18g 。 使用单卡24g显存的4090

## 数据： 

构建领域的高质量sft数据， 

使用高转化广告创意。 

清洗得到关键词包含在广告创意中的。 



## lora-SFT阶段

##### 框架 ：  LLama factory

[https://github.com/hiyouga/LLaMA-Factory/]

1.  sft数据转变成llama -factory 形式 ， https://github.com/hiyouga/LLaMA-Factory/blob/main/data/dataset_info.json)
2.  修改dataset_info.json , 添加自己的dataset
3.  修改train.sh ， 自定义 model_path（提前将模型下载到本地） ,dataset , template , lora_target , output_dir, batch size 
4.  开始loar微调

调整超参数:

LORA_RANK : rank 秩 越低  ，参数越少， 训练越快  ， 但模型的灵活性较低，默认为8

lora_alpha : lora调整幅度 ， 越大， 对原始模型参数的调整越大， 可能会过拟合
越小： 调整越小， 泛化能力越强

lora_dropout :  防止模型过拟合， 越高泛化能力越强， 学习效率越低

