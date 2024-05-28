Paraformer语音识别-中文-通用-16k-离线-large-pytorch

https://modelscope.cn/models/iic/speech_paraformer-large_asr_nat-zh-cn-16k-common-vocab8404-pytorch/summary





```
pip install funasr
pip install ffmpeg
```

```python
from funasr import AutoModel
# paraformer-zh is a multi-functional asr model
# use vad, punc, spk or not as you need
model = AutoModel(model="paraformer-zh", model_revision="v2.0.4",
...                      ad_model="fsmn-vad",
...                      vad_model_revision="v2.0.4",
...                      punc_model="ct-punc-c",
...                      punc_model_revision="v2.0.4",
...                      spk_model="cam++",
...                      spk_model_revision="v2.0.2"
                  )

model = AutoModel(model="/data0/yuanbo6/model/speech_paraformer",model_revision="v2.0.4")

res = model.generate(input=f"{model.model_path}/example/asr_example.wav", 
            batch_size_s=300, 
            hotword='魔搭')

res = model.generate(input="little_swan.wav", 
                     batch_size_s=300, 
)
print(res)
```





```
pip install moviepy

```



```python
from moviepy.editor import VideoFileClip
videos_file_path = ''
my_clip = VideoFileClip(videos_file_path)


my_clip.audio.write_audiofile(f'{videos_file_path}.mp3')

import moviepy.editor as mp
def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    my_clip.audio.write_audiofile(f'{videos_file_path}.mp3')
。



```

``

```
from moviepy.editor import VideoFileClip

# 视频文件路径
video_path = 'your_video.mp4'

# 加载视频文件
video = VideoFileClip(video_path)

# 从视频中提取音频部分
audio = video.audio

# 保存音频为临时文件
audio_path = 'temp_audio.wav'
audio.write_audiofile(audio_path)

```

