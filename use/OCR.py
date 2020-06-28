#!/usr/bin/env python
# -*- coding: utf-8 -*-
from aip import AipOcr
import os
path = os.path.split(os.path.realpath(__file__))[0]

def GetText():
    APP_ID = '20074782'  # 此处为申请的百度ocr接口信息
    API_KEY = 'vdVBOzAzYXoZZucH1koccjrW'
    SECRET_KEY = 'o7ysFphK98Mzi9AP2yb1PPXNvGGPF0jr'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    fp = open(path+"/area.png", "rb").read()
    # res = client.basicGeneral(fp)  # 普通精度
    res = client.basicAccurate(fp)  # 高精度

    strx = ""
    for tex in res["words_result"]:
        strx += tex["words"] + " \n"
    return strx
