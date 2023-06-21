### docker

docker hub  拉镜像

https://hub.docker.com/



```
# install docker 

install docker 
sudo apt install docker.io

```





```shell
docer run -it -v $PWD:/work centos: latest /bin/bash     #docker启动centos
	
docker pull nvidia/cuda:10.1-devel-ubuntu18.04	# doucker 拉镜像

docker save 7e66518b68a8 > nvidia.tar	#docker 导出image






sudo docker image ls # 展示出所有容器

sudo docker run -it 7293def00749  #  docker run -it + image_id  启动容器
sudo docker run -it 7293def00749 /bin/bash


可以在docker环境中安装python包
pip install flask
pip install transformers==4.5.1
pip install gunicorn==20.1.0
pip install gensim==3.8.3

sudo docker ps  # 在运行的容器

sudo docker commit 25ccccc yuanbo:v1  #将 CONTAINER ID 打包成新的 yuanbo:v1  容器

之后就可以直接run新容器

sudo docker run -it yuanbo:v1

# docker start 
systemctl start docker

# verify docker engine install success 
sudo docker run hello-world

# docker restart 
systemctl restart docker.service



# 删除镜像
sudo  docker image rm -f 32920f4aa713
```

