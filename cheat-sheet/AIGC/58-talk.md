s - lora 节省机器资源

公开数据集：mt-bench， OpenCompass



yi和 qwen都是llama结构的， 

baichuan，与llama结构有区别，需要调整.

最好使qwen 或者yi 。



输出的重复可能是因为训练的epoch过多导致过拟合， 除了调节参数，还可以降低epoch





moe ： 共享 expert





垂类信息输入：固定lr ， 调整bz







用base版本做指令微调





