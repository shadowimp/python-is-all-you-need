```bash
# 本地安装
conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda activate paddle_env

python3 -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple

python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple

pip install paddleocr -i https://mirror.baidu.com/pypi/simple

pip install paddleocr

pip3 install opencv-python-headless==4.5.3.56

# docker 安装
https://hub.docker.com/r/paddlecloud/paddleocr/tags

docker run --name ppocr --runtime=nvidia -v $PWD:/mnt -p 8888:8888 -it --shm-size=32g paddlecloud/paddleocr:2.5-gpu-cuda10.2-cudnn7-latest /bin/bash


# 报错；CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
source /data0/user/conda/etc/profile.d/conda.sh



```



```python
from paddleocr import PaddleOCR,draw_ocr


ocr = PaddleOCR(use_angle_cls=True, 
                lang="ch",
                use_gpu=False,
                rec_model_dir='ch_PP-OCRv3_rec_infer/',
                det_model_dir='ch_PP-OCRv3_det_infer/',
                det_db_box_thresh=0.8
               )

ocr = PaddleOCR(use_angle_cls=True, 
                lang="ch",
                use_gpu=True,
                rec_model_dir='models/ch_PP-OCRv3_rec_infer/',
                det_model_dir='models/ch_PP-OCRv3_det_infer/',
                det_db_box_thresh=0.8
               )

img_path='https://img.alicdn.com/imgextra/i2/2080028774/O1CN012326nf2EgXonnhFtG_!!2080028774.jpg'
result = ocr.ocr(img_path, cls=True)
print(result)
```





```python
# use gup 
from paddleocr import PaddleOCR,draw_ocr


ocr = PaddleOCR(use_angle_cls=True, 
                lang="ch",
                use_gpu=True,
                rec_model_dir='ch_PP-OCRv3_rec_infer/',
                det_model_dir='ch_PP-OCRv3_det_infer',
                det_db_box_thresh=0.8
               )

img_path='https://img.alicdn.com/imgextra/i2/2080028774/O1CN012326nf2EgXonnhFtG_!!2080028774.jpg'
result = ocr.ocr(img_path, cls=True)
print(result)



# 并行处理


img_path=['https://img.alicdn.com/imgextra/i2/2080028774/O1CN012326nf2EgXonnhFtG_!!2080028774.jpg','https://img.alicdn.com/imgextra/i2/2080028774/O1CN012326nf2EgXonnhFtG_!!2080028774.jpg']
result = ocr.ocr(img_path, cls=True)
print(result)

```

