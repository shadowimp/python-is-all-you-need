自动化生成web交互界面



https://gradio.app/quickstart/

```
pip install gradio

```

```python
import gradio ad gr 
import cv2

def to_black(image):
  output = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
  return output 

interface = gr.Interface(fn=to_black, inputs='image', outputs='image')
# fn : function

interface.launch()


```

```python
demo = gr.Interface(title="太乙中文 stable diffusion 模型",
                        css="",
                        fn=generate,
                        inputs=[gr.Textbox(lines=3, placeholder="输入你想生成的图片描述", label="prompt"), gr.Slider(0, 100)],
                        outputs=[gr.outputs.Image(label="图片")])。
```

```
demo = gr.Interface(fn=greet, inputs="text", outputs="text")
```

