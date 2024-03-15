### docker

docker hub  拉镜像

https://hub.docker.com/



```bash
# install docker 
# https://docs.docker.com/engine/install/centos/
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# start docker 
sudo systemctl start docker

# 

```

```bash
# docker pull image  
docker image pull nvidia/cuda:10.1-devel-ubuntu18.04	

docker pull continuumio/miniconda3
docker run -t -i continuumio/miniconda3 /bin/bash
```





```shell
#docker启动centos
docer run -it -v $PWD:/work centos: latest /bin/bash     
# -i : access the interactive model  
# -t : allocate a vitual terminal sessions
	


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

