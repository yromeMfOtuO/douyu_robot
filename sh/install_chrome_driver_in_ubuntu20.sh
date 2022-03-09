# 首先需要先安装chrome 

# 验证是否安装了chrome，如果安装了会输出路径，输出为空则未安装
which google-chrome

# 未安装安装
# 1. 下载chrome
cd /opt	# 这个目录可以根据需要修改
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# 2. 安装
sudo dpkg -i google-chrome-stable_current_amd64.deb

# 3. 因为依赖不完整，安装过程中可能会出现错误
# dpkg: error processing package google-chrome-stable (--install):
# dependency problems - leaving unconfigured
#
# 需要修复依赖关系
sudo apt-get update # 先对当前系统的可用更新列表进行更新
sudo apt-get install -f # 修复依赖关系

# 安装完成后查看chrome版本以安装对应的chromedriver，因为两者版本必须对应
google-chrome --version # 查看chrome版本


# 安装chromedriver
# 下载chromedriver 下载地址：https://registry.npmmirror.com/binary.html?path=chromedriver
wget https://registry.npmmirror.com/-/binary/chromedriver/99.0.4844.51/chromedriver_linux64.zip  # 下载路径可以浏览器选择对应版本获取下载链接 
# 解压缩.zip文件，获取可以执行文件
unzip chromedriver_linux64.zip
# 复制安装文件到 /usr/bin 目录，相当于加入了path
mv chromedriver /usr/bin/chromedriver
# 运行chromedriver，检查是否安装成功 
chromedriver  # 可以使用which命令先检查
