```
# env 

conda create --name chatglm python=3.9 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

/data0/***/conda_env/envs/chatglm/bin/python


python -m pip install llmtuner==0.1.3 



```

https://zhuanlan.zhihu.com/p/645010851

```
# run 
unset http_proxy https_proxy all_proxy # 关闭代理
python -m llmtuner.webui.interface
```



#### 指令监督微调

```


CUDA_VISIBLE_DEVICES=0 /data0/yuanbo6/conda_env/envs/chatglm/bin/python src/train_bash.py \
    --stage sft \
    --do_train \
    --model_name_or_path path_to_llama_model \
    --dataset alpaca_gpt4_zh \
    --template default \
    --finetuning_type lora \
    --lora_target q_proj,v_proj \
    --output_dir path_to_sft_checkpoint \
    --overwrite_cache \
    --per_device_train_batch_size 4 \
    --gradient_accumulation_steps 4 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_steps 1000 \
    --learning_rate 5e-5 \
    --num_train_epochs 3.0 \
    --plot_loss \
    --fp16
```





```
# 修改dataset_info.json  ， 添加自己的dataset

  "test_dataset": {
    "file_name": "/data/test.json",
    "columns": {
      "prompt": "instruction",
      "query": "input",
      "response": "output"
    }},
    

```



```
# train.sh  
# 自定义 model_path ,dataset , template , lora_target , output_dir, batch size 

CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
    --stage sft \
    --do_train \
    --model_name_or_path /data0/chatglm3-6b \
    --dataset test_dataset \
    --template chatglm3 \
    --finetuning_type lora \
    --lora_target all \
    --output_dir /data0/chatglm3_lora_0304 \
    --overwrite_cache \
    --per_device_train_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --lr_scheduler_type cosine \
    --logging_steps 10 \
    --save_strategy epoch \
    --save_only_model \
    --learning_rate 1e-4 \
    --num_train_epochs 10.0 \
    --plot_loss \
    --fp16
```

```
# infer_test.sh 
from peft import PeftModel
from transformers import AutoTokenizer, AutoModel
model_dir = "/data0/chatglm3-6b"
lora_dir = "/data0/chatglm3_lora_0302/checkpoint-10"
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
model = AutoModel.from_pretrained(model_dir, trust_remote_code=True).half().cuda()
model = PeftModel.from_pretrained(model, lora_dir)
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
```



```
# set dataset 
# dataset_info.json

```



### 4bit 量化



### lora

```
LORA_RANK : rank 秩 越低  ，参数越少， 训练越快  ， 但模型的灵活性较低，默认为8

lora_alpha : lora调整幅度 ， 越大， 对原始模型参数的调整越大， 可能会过拟合
越小： 调整越小， 泛化能力越强

lora_dropout :  防止模型过拟合， 	越高泛化能力越强， 学习效率越低


```

