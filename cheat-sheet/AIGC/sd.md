stabilityai/sdxl-turbo

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

