量化(Quantization

数据:高精度(比如float32压缩到低精度(比如4位整数)的技术。

float32 - > int 8  显存占用减少4倍

float32（4字节）

int8 （1字节） 

N=6b（对于6B模型），那么： 

int8 存储: 6B字节 ： 6G

float32 存储： 6B*4 = 24g



Adam优化器:除了参数和梯度外，它还需要为每个参数维护两个额外的状态变量：一阶矩估计和[二阶矩估计](https://www.zhihu.com/search?q=二阶矩估计&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"3534428197"})。这两个状态变量与参数的维度相同，因此Adam的内存占用约为：3×模型参数内存。

训练 yi-6b ： 显存  3*6 = 18g

