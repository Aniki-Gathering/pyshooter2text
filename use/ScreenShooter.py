#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageTk
import tkinter
import time
import platform
import os
sys = platform.system()  # 判断系统型号
path = os.path.split(os.path.realpath(__file__))[0]
scale = 1.0
if sys == "Linux":  # 获取截图
    import pyscreenshot as ImageGrab
else:
    from PIL import ImageGrab
time.sleep(0.2)
ImageGrab.grab().save(path+"/tmp.png")

root = tkinter.Tk()  # 显示截图
width = root.winfo_screenwidth()  # 实际分辨率
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))  # 全屏大小
image = Image.open(path+"/tmp.png")
scale = image.width/width  # 获取缩放
if scale != 1.0:
    image = image.resize((width, height), Image.ANTIALIAS)  # 缩放全屏截图
img = ImageTk.PhotoImage(image)
bak = tkinter.Canvas(root, width=width, height=height)
bak.create_image(width//2, height//2, image=img)
bak.pack()
root.overrideredirect(True)  # 没有标题栏
root.resizable(0, 0)  # 大小不可变
root.wm_attributes('-topmost', True)  # 置顶

start = [0, 0]  # 鼠标事件
end = [width, height]


def WhereIsMouse(event):  # 实际分辨率
    start[0] = event.x
    start[1] = event.y


def DrawArea(event):
    try:
        bak.delete("area")
    except Exception as e:
        pass
    bak.create_rectangle(
        start[0], start[1], event.x, event.y, outline="red", tags="area")
    end[0] = event.x
    end[1] = event.y
    # print(start, end)


def EndDraw(event):
    Image.open(path+"/tmp.png").crop((min(start[0], end[0])*scale, min(start[1], end[1])*scale, max(
        start[0], end[0])*scale, max(start[1], end[1])*scale)).save(path+"/area.png")
    root.after(100, root.destroy)  # 关闭


def Quit(event):
    root.after(100, root.destroy)  # 关闭


bak.bind("<Double-Button-1>", Quit)
bak.bind("<Escape>", Quit)
bak.bind("<ButtonPress-1>", WhereIsMouse)
bak.bind("<B1-Motion>", DrawArea)
bak.bind("<ButtonRelease-1>", EndDraw)

bak.focus_set()
root.mainloop()
