#!/usr/bin/env python
# -*- coding: utf-8 -*-
import http.client
import hashlib
import urllib
import random
import json


def GetTranslation(text):
    appid = '20200611000492448'  # 此处为申请的百度翻译接口信息
    secretKey = 'hVKyeVjTlX6pdWjtFYuf'

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'  # 原文语种
    toLang = 'zh'  # 译文语种
    salt = random.randint(32768, 65536)
    q = ""+text
    q = q.replace('\n', ' ')  # 原文去换行
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()  # response是HTTPResponse对象
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    strx = str(result["trans_result"][0]["dst"])
    return strx
