# Setup Environment

## 实验环境要求

### 操作系统

`Ubuntu 18.04 LTS x86_64`

### 编程语言

`python3.7.6` (`Anaconda3`环境)

### 学习框架

`PyTorch==1.7.0`

### 硬件环境

单GPU（with CUDA 10.1）


## 实验环境搭建

### 安装anaconda3

安装教程：https://docs.anaconda.com/anaconda/install/linux/#installation

下载地址：https://www.anaconda.com/distribution/#linux

1.	下载命令：(注意：$ 为linux系统下的命令提示符，不属于命令部分)
    ```
    $ wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
    $ bash Anaconda3-2020.02-Linux-x86_64.sh
    ```
    **注：** 请按照命令行提示安装anaconda，所有选项输入yes)

2.	激活conda环境：
    ```
    $ source ~/.bashrc
    ```

3.	测试是否安装成功：
    ```
    $ conda -V
    ```
    若安装成功，则会显示：  conda 4.8.2

### 安装python3.7.6（若使用Anaconda3的base环境，默认是python3.7.6，则不需额外安装）

1.	创建新的conda环境：
    ```
    $ conda create -n py37 python=3.7.6
    ```
2.	激活python3.7:
    ```
    $ conda activate py37
    ```

### 安装gcc（如果机器已经安装gcc，请忽略）
```
$ sudo apt-get update
$ sudo apt-get install build-essential
```

### 安装pytorch (version 1.7.0)

GPU（CUDA10.1）版本：
```
conda install pytorch==1.7.0 torchvision==0.8.0 torchaudio==0.7.0 cudatoolkit=10.1 -c pytorch
```

Download issue:
```
from six.moves import urllib
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)
```


Steps:
```
git clone https://github.com/microsoft/AI-System.git
cd AI-System/Labs/BasicLabs/Lab2/

#execute basic version
python3 mnist_basic.py

#execute custom version
python3 mnist_custom_linear.py

#execute custom c++ version
cd mylinear_cpp_extension/
python3 setup.py install
cd ../
python3 mnist_custom_linear_cpp.py

#execute custom cuda version
cd ../Lab3/mylinear_cuda_extension
python3 setup.py install
cd ..
python3 mnist_custom_linear_cuda.py
```


