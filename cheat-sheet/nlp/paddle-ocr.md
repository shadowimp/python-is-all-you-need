```
conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

conda activate paddle_env

python3 -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple

python3 -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple

pip install paddleocr
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

