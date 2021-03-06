# 项目简介
项目名称: pyshooter2text  
本项目是截图、ocr(图片转文字)、翻译功能三合一程序，并提供了图形化主界面、快捷查询单词、最小化到托盘、后台快捷键、多种主题配色等功能  
___
# 环境配置
## python环境准备
请确保在终端中<b>"python3"</b>为运行该项目的解释器  
如果不是，请进行如下修改：  
- 编辑项目文件夹下的 main.py  
将183、227行中的"python3"替换为要使用的解释器  
示例："python" "python3.7" "D:\Venv\myenv\Scripts\python.exe"  
- （可选）编辑启动快捷方式  
如果要使用快捷方式启动，请修改项目文件夹下的 Start.sh 、Start.bat  
将其中的"python3"替换为要使用的解释器  
## 第三方库
请根据不同系统选择  
- Windows  
```sh
/your/interpreter -m pip install -r /path/to/project/requirements-windows.txt
```
- Linux、MacOS同理使用 requirements-linux.txt 、requirements-macos.txt  
- 部分linux发行版可能需要从相应的包管理器安装tk环境  
示例：  
```sh
sudo pacman -S tk # arch
sudo yum -y install tk # centos
```
- linux使用的第三方库pyscreenshot需要python版本>=3.6  
## macOS请注意
由于xcffib在macos的测试中不能使用，导致system-hotkey模块，即快捷键功能不能使用。  
__请使用 main.py.bak 替换 main.py__
___
# 启动
## 快捷方式启动
Windows用户请启动项目文件夹下Start.vbs  
Linux/MacOS用户请启动项目文件夹下Start.sh  
## 从终端启动
```sh
cd /path/to/project
/your/interpreter ./main.py
```
___
# 基本操作
主界面如下：  
![](_v_images/20200627133856366_9516.png)  
## 截图
![](_v_images/20200627133947753_29880.png)  
点击此按钮进入截图，使用鼠标画出需要截下的矩形范围  
截图保存在./use/tmp.png（全屏）和./use/area.png（范围）  
截图时可以双击左键或<kbd>Esc</kbd>退出  
示例：红色矩形为截取的范围  
![](_v_images/20200627140534752_1396.png)  
## 识别、翻译
![](_v_images/20200627134517732_29759.png)  
点击此按钮会对最近一次的截图进行OCR识别和翻译，并且会输出结果  
左侧选择语言的下拉列表菜单<b>没有</b>作用  
OCR不支持语言选择，测试中仅对中文、英语支持较好  
翻译采用的是自动检测语言，如果要修改请自行修改 ./use/Translate.py 中的参数  
示例：  
![](_v_images/20200627140735419_24754.png)  
使用![](_v_images/20200627142530199_31400.png)可以将翻译结果复制到剪贴板  
## 查单词
![](_v_images/20200627140819421_22567.png)  
可以快捷查询单词  
示例：  
![](_v_images/20200627140656280_27158.png)  
___
# 高级设置
![](_v_images/20200627141649065_2999.png)  
进入设置面板  
![](_v_images/20200628112132614_11176.png)  
## 全局快捷键
项目默认设置了截图、查单词的全局快捷键  
<kbd>Ctrl-q</kbd>    最小化到托盘并弹出快捷查词  
![](_v_images/20200627141349636_28339.png)  
<kbd>Ctrl-p</kbd>    截图  
这些快捷键可以在setup.ini中进行修改  
## 最小化到托盘
当点击关闭按钮时可选择退出或最小化到托盘  
可以在设置中进行更改  
## 功能介绍
没有  
## 主题
提供了4种主题可更换，默认为 cold  
![](_v_images/20200628212155558_25419.png)  
![](_v_images/20200628212213550_32381.png)  
![](_v_images/20200628212245395_682.png)  
