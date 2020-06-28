#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests,re

def get_net(word):
    url="http://dict.youdao.com/w/eng/"+word+"/#keyfrom=dict2.index"
    html=requests.get(url).content.decode('utf-8')
    return html

def analysis(word_net):
    searchSuccess = re.search(r"(?s)<div class=\"trans-container\">.*?<ul>.*?</div>",word_net)
    means = re.findall(r"(?m)<li>(.*?)</li>",searchSuccess.group())
    return means
   


