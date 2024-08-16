### ppo 

PPO (proximal policy optimization) 

基于Actor and critic 架构



### DPO

DPO :Direct Preference Optimization 



将 [RLHF](https://www.zhihu.com/search?q=RLHF&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A"671780768"}) 的 2 阶段多个模型的训练简化为了 1 阶段的 [SFT](https://www.zhihu.com/search?q=SFT&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A"671780768"}) 训练。在这里简单总结一下。

### RLHF

Reinforcement Learning from Human Feedback (RLHF).

RLHF通过收集人类反馈数据（符合人类偏好的数据），训练出奖励模型，通过奖励模型评估LLM的答案，更新LLM权重，最终得到答案符合人类偏好的LLM。具体使用的策略就是PPO算法。





### model.chat and model.genarate

https://github.com/QwenLM/Qwen/issues/604







### vllm

llm  的推理部署库， 可以提升服务的性能

算法： page attention

将连续的kv cache 存储在不连续的空间， 避免显存的浪费





### rag

llama index



### video 2 text 

https://arxiv.org/pdf/2212.14546