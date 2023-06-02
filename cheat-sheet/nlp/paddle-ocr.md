```bash
# 本地安装
conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda activate paddle_env

python3 -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple

python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple

pip install paddleocr

# docker 安装
https://hub.docker.com/r/paddlecloud/paddleocr/tags

docker run --name ppocr --runtime=nvidia -v $PWD:/mnt -p 8888:8888 -it --shm-size=32g paddlecloud/paddleocr:2.5-gpu-cuda10.2-cudnn7-latest /bin/bash
```



```python
from paddleocr import PaddleOCR,draw_ocr


ocr = PaddleOCR(use_angle_cls=True, 
                lang="ch",
                use_gpu=False,
                rec_model_dir='/data/ch_ppocr_server_v2.0_rec_infer/',
                det_model_dir='/data/ch_ppocr_server_v2.0_det_infer/',
                det_db_box_thresh=0.8
               )

img_path='https://img.alicdn.com/imgextra/i2/2080028774/O1CN012326nf2EgXonnhFtG_!!2080028774.jpg'
result = ocr.ocr(img_path, cls=True)
print(result)
```

