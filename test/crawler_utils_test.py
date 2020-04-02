# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zhihu_simple_crawler
   Description :
   Author :       zenquan
   date：          2019/12/21
-------------------------------------------------
   Change Activity:
                   2019/12/21:
-------------------------------------------------
"""
__author__ = 'zenquan'

import requests
from lib.crawler_utils import headers_to_dict

def crawl(params=None):
    url = 'https://www.sanjieke.cn/Index/getIndexBanner'
    params = {
        'limit': 20,
        'offset': 0,
        'include': 'data[*].follower_count,gender,is_followed,is_following'
    }
    headers = """
        Host: www.sanjieke.cn
        Connection: keep-alive
        Accept: application/json, text/plain, */*
        X-Requested-With: XMLHttpRequest
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36
        Sec-Fetch-Site: same-origin
        Sec-Fetch-Mode: cors
        Referer: https://www.sanjieke.cn/
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,und;q=0.7
        Cookie: PHPSESSID=aql64nl0lsb4ibdi89v37584s3; utm_data={"c_utm_content":"","c_utm_campaign":"","c_utm_medium":"","c_utm_term":"","c_utm_source":"","d1_utm_content":"","d1_utm_campaign":"","d1_utm_medium":"","d1_utm_term":"","d1_utm_source":"","d15_utm_content":"","d15_utm_campaign":"","d15_utm_medium":"","d15_utm_term":"","d15_utm_source":"","d30_utm_content":"","d30_utm_campaign":"","d30_utm_medium":"","d30_utm_term":"","d30_utm_source":"","referrer":"https://www.sanjieke.cn/free.html"}
        
    """
    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)

if __name__ == '__main__':
    crawl()