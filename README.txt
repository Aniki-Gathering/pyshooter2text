# 项目简介

项目名称: pyshooter2text  
本项目是由李泽凯、汪文涛、杨涛共同开发的截图、ocr(图片转文字)、翻译功能三合一程序，并提供了图形化界面、最小化到托盘、后台快捷键等功能  
请尽量看同名md文件，图文并茂  


# 环境配置

## python环境准备

请确保在终端中 "python" 为运行该项目的解释器  
如果不是，请进行如下修改：  
- 编辑项目文件夹下的 main.py  
将181、225行中的"python"替换为要使用的解释器  
示例："python3" "python3.7" "D:\Venv\myenv\Scripts\python.exe"
- （可选）编辑启动快捷方式  
如果要使用快捷方式启动，请修改项目文件夹下的 Start.sh 、Start.bat  
将其中的"python"替换为要使用的解释器  

## 第三方库

请根据不同系统选择  
- Windows
/your/interpreter -m pip install -r /path/to/project/requirements-windows.txt
- Linux、MacOS同理使用 requirements-linux.txt 、requirements-macos.txt
## macOS请注意
由于xcffib在macos的测试中不能使用，导致system-hotkey，即快捷键功能不能使用。  
请使用 main.py.bak 替换 main.py


# 启动

## 快捷方式启动

Windows用户请启动项目文件夹下Start.vbs  
Linux/MacOS用户请启动项目文件夹下Start.sh  

## 从终端启动

cd /path/to/project
/your/interpreter ./main.py


# 基本操作

点击相机样式按钮进入截图，使用鼠标画出需要截下的矩形范围  
截图时可以双击左键或Esc退出  

点击翻译按钮会对最近一次的截图进行OCR识别和翻译，并且会输出结果  
使用右下剪切板样式按钮可以将翻译结果复制到剪贴板  

使用右上快捷快捷查询单词  


# 高级设置

项目默认设置了截图、查单词的全局快捷键  
这些快捷键可以在setup.ini中进行修改  
当点击关闭按钮时可选择退出或最小化到托盘  
可以在设置中进行更改  
提供了4种主题可更换  
