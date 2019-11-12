# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         mini_frame
# Description:  
# Author:       Dell
# Date:         2019/11/12
# -------------------------------------------------------------------------------
import time


def index():
    with open("./H1153/index.html") as f:
        content = f.read()
    return content


def login():
    return "这是登录页面"


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])

    file_name = env['PATH_INFO']
    if file_name == '/index.py':
        return index()
    elif file_name == '/login.py':
        return login()
    else:
        return 'Hello World! 我爱你中国。'
