# 深度学习平台模拟器

## 安装要求

```
pip install pyyaml
```

##  [深度学习调度算法实验与模拟研究](https://github.com/microsoft/AI-System)

## 深度学习调度算法实验与模拟研究

此开源数据集[philly-traces](https://github.com/msr-fiddle/philly-traces) 包含 Microsoft 内部 Philly集群上第一方 (first-party) DNN 训练工作负载的代表性子集。 数据是 ATC’19 中“Analysis of large-scale multi-tenant GPU clusters for DNN training workloads”中描述的工作负载的一个脱敏数据子集。 这项工作是作为 Microsoft Research 的 Project Fiddle 的一部分完成的。

### 1 数据读取
读者可以参考库中提供的脚本读取数据并了解数据模式。
### 2 评测指标设定
读者可以根据本章开始介绍的指标设计优化目标。
### 3 算法实现与评测
读者可以选用以上介绍的经典算法作为基准测试，设计新的算法，并通过真实平台数据模拟，看能否提升当前目标，超越基准算法，并进行结果分析，形成分析报告或论文。

### Download data

```
wget https://github.com/msr-fiddle/philly-traces/raw/master/trace-data.tar.gz
tar -xvf trace-data.tar.gz
ls -lh
total 6.6G
-rw-rw-r-- 1 testcluster testcluster 1.6G Jun  2  2019 cluster_cpu_util
-rw-rw-r-- 1 testcluster testcluster 2.9G Jun  2  2019 cluster_gpu_util
-rw-rw-r-- 1 testcluster testcluster  38M Jul  2  2019 cluster_job_log
-rw-rw-r-- 1 testcluster testcluster 7.0K Jun 24  2019 cluster_machine_list
-rw-rw-r-- 1 testcluster testcluster 2.2G Jun 28  2019 cluster_mem_util
```

### 启动模拟器

```
python simulator.py --trace_path ../../philly-traces/trace-data-sample
```


