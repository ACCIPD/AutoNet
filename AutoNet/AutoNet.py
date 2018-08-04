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
             'Cookie': 'think_language=en-GB; PHPSESSID=mkhjrb2eqigihasd5tfnalv4i1; sunriseUsername=20175227033; sunriseDomain=campus',
             'Host': 'a.suda.edu.cn',
             'Referer': 'http://a.suda.edu.cn/',
             'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
             'X-Requested-With': 'XMLHttpRequest'}

# 构造登录数据
post_data={
            'domain': '',
            'enablemacauth': '0',
            'password': 'MDQyODY5NTQ=',
            'username': '20175227033'
          }
# 发送post请求登录网页
z=requests.post(post_addr, data=post_data, headers=post_header)
print("Internet Login" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
