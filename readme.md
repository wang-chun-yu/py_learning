# 安装Miniforge（包含mamba）:
```
// 下载安装包
cd ~/Downloads
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
// 执行安装脚本
sudo chmod +x Miniforge3-Linux-x86_64.sh
./Miniforge3-Linux-x86_64.sh
// 初始化环境
eval "$(/home/chunyu/hdd1/miniforge3/bin/conda shell.bash hook)"
conda init 
conda config --set auto_activate_base false // 设置不自动进入base环境
// 验证
mamba --version
conda --version
```

# 创建环境
```
// 
mamba create -n py3_learning python=3.10.14
mamba activate py3_learning
pip install -r requirements.txt
// 启动
eval "$(mamba shell hook --shell bash)"
mamba activate py3_learning
```


