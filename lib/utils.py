# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     utils
   Description :
   Author :       zenquan
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""
__author__ = 'zenquan'

import datetime
import json

#差集函数
def diff(listA,listB):
    #求交集的两种方式
    retD = list(set(listB).difference(set(listA)))
    return retD

#json格式文件生成
def json_generate(ps_pers, num, filename='/home/weike/jx_ps_%s_%s.json'):
    all_len = len(ps_pers)
    cur = int(all_len // num)
    flag = filename == '/home/weike/jx_ps_%s_%s.json'
    for i in range(num):
        byte_ls = ps_pers[i * cur: (i + 1) * cur]
        ls = [str(l, encoding='utf-8') for l in byte_ls] \
            if flag else byte_ls
        now = datetime.datetime.now().strftime('%Y%m')
        file_name = filename % (now, num)\
            if flag else filename
        with open(file_name, 'w') as wf:
            wf.write(json.dumps(ls))