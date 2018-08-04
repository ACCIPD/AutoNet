#!/usr/bin/env python3
"""python crawler """
# encoding:UTF-8

import requests
import datetime
# 登录地址
post_addr="http://a.suda.edu.cn/index.php/index/login"

# 构造头部信息
post_header={'Accept': 'application/json, text/javascript, */*; q=0.01',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'en-GB,en;q=0.5',
             'Connection': 'keep-alive',
             'Content-Length': '68',
             'Content-Type': 'application/x-www-form-urlencoded',
             'Cookie': '',
             'Host': '',
             'Referer': '',
             'User-Agent': '',
             'X-Requested-With': 'XMLHttpRequest'}

# 登录数据
post_data={
            'domain': '',
            'enablemacauth': '0',
            'password': 'ABCDEFGHIJK=',
            'username': '1234567890'
          }
# 发送post请求登录网页
z=requests.post(post_addr, data=post_data, headers=post_header)
print("Internet Login " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
