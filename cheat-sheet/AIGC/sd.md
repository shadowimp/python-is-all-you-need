### control net

指令修图，

```

# 加载ControlNet模型
checkpoint = "lllyasviel/control_v11e_sd15_ip2p"
controlnet = ControlNetModel.from_pretrained(checkpoint, torch_dtype=torch.float16)

# 创建StableDiffusionControlNetPipeline管道
pipe = StableDiffusionControlNetPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", controlnet=controlnet, torch_dtype=torch.float16) 

# 启用CPU卸载加速
pipe.enable_model_cpu_offload()  

# 定义prompt
prompt = "make it spring"
prompt = "make it summer" 
prompt = "make it autumn"
prompt = "make it winter"

# 设置随机种子
generator = torch.manual_seed(0)

# 生成图像  
image_style1 = pipe(prompt, num_inference_steps=30, generator=generator, image=original_image).images[0]
```



### palyground

```python
from diffusers import DiffusionPipeline
import torch

sd_model = DiffusionPipeline.from_pretrained(
    "playgroundai/playground-v2-1024px-aesthetic",
    torch_dtype=torch.float16,
    use_safetensors=True,
    add_watermarker=False,
    variant="fp16"
)
sd_model.to("cuda")


sd_model = DiffusionPipeline.from_pretrained(
    "playgroundai/playground-v2-512px-base",
    torch_dtype=torch.float16,
    use_safetensors=True,
    add_watermarker=False,
    variant="fp16",
)

# 节省显存， 模型卸载（Model offloading）
sd_model.enable_model_cpu_offload() 



```







stabilityai/sdxl-turbo



```python
from io import BytesIO
import torch
from diffusers import AutoPipelineForText2Image
import os
from diffusers import DiffusionPipeline
model_path = '/data0/yuanbo6/sdxl-turbo/'
sd_model = DiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16, variant="fp16")
sd_model.to("cuda")
image = sd_model(prompt='cat', num_inference_steps=20, guidance_scale=3).images[0]
image.save('./cat.png', format='png')
```



```python
import torch
from diffusers import AutoPipelineForText2Image

pipe_text2img = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
if torch.cuda.is_available():
  pipe.to("cuda")
text = 'a cat'
image = pipe_text2img(prompt=text, num_inference_steps=1, guidance_scale=0.0).images[0]
save_path = './test.jpg'
image.save(save_path)


```





### playground



```python
from diffusers import DiffusionPipeline
import torch 
pipe_text2img_v2 = DiffusionPipeline.from_pretrained("playgroundai/playground-v2-1024px-aesthetic",torch_dtype=torch.float16,use_safetensors=True,add_watermarker=False,variant="fp16")
text = 'a cat'
image =pipe_text2img_v2(prompt=text,guidance_scale=3.0).images[0]

```

```python
from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained(
    "playgroundai/playground-v2-1024px-aesthetic",
    torch_dtype=torch.float16,
    use_safetensors=True,
    add_watermarker=False,
    variant="fp16"
)
pipe.to("cuda")

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image  = pipe(prompt=prompt, guidance_scale=3.0).images[0]
image.save('xx.png')
```





```
docker run  -d -it --name sdw -p 7860:7860 --gpus all -v $(pwd)/models:/app/stable-diffusion-webui/models -v $(pwd)/outputs:/app/stable-diffusion-webui/outputs -v


```

