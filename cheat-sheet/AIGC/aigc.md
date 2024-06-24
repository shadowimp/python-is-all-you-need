### dpo ppo 

PPO (proximal policy optimization) 

Actor : 

action :



DPO :Direct Preference Optimization 



将 [RLHF](https://www.zhihu.com/search?q=RLHF&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A"671780768"}) 的 2 阶段多个模型的训练简化为了 1 阶段的 [SFT](https://www.zhihu.com/search?q=SFT&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"article"%2C"sourceId"%3A"671780768"}) 训练。在这里简单总结一下。



Reinforcement Learning from Human Feedback (RLHF).



https://github.com/QwenLM/Qwen/issues/604

model.chat and model.genarate





### vllm

llm  的推理部署库， 可以提升服务的性能

算法： page attention

将连续的kv cache 存储在不连续的空间， 避免显存的浪费





llama index