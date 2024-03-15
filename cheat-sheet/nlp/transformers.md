###  国内镜像站 

https://hf-mirror.com

```
export HF_ENDPOINT=https://hf-mirror.com
```





### 保存模型

需要保存3个文件，才能加载finetune后的model

1.  model  pytorch_model.bin

2.配置文件configuration。 json类型 config.json

3.tokenizer词汇表 vocab.txt 

都有from_pretrained()  和 save_pretrained() 方法



```python
# save model 
torch.save(model_to_save.state_dict(), output_model_file)
model_to_save.config.to_json_file(output_config_file)
tokenizer.save_vocabulary(output_vocab_file)

# load model

```





```
bugs : 
多线程时报错：RuntimeError : Already borrowed
adding "tokenizer_args": {"use_fast": false} to sentence_bert_config.json
```

