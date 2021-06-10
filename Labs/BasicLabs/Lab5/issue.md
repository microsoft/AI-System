# 常见问题
## 1. 构建部署PyTorch训练程序时出现 "BADSIG F60F4B3D7FA2AF80" 错误
### 运行的命令
`docker build -f Dockerfile.gpu -t train_dl .`
### 错误日志
```bash
W: GPG error: https://developer.download.nvidia.cn/compute/machine-learning/repos/ubuntu1804/x86_64  Release: The following signatures were invalid: BADSIG F60F4B3D7FA2AF80 cudatools <cudatools@nvidia.com>
E: The repository 'https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release' is not signed.
```
### 原因
NVIDIA 的 CDN 更新了新的 GPG 签名缓存 `Release.gpg`，但对应的本体 `Release` 并未更新，这会造成上述错误。
### 解决方法
解除 `Dockerfile.gpu` 内 `# 解决网络问题` 下命令的注释，令其运行将下载源换为 Aliyun 源，可以解决问题。
