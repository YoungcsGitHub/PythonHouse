# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         mini_frame
# Description:  
# Author:       Dell
# Date:         2019/11/12
# -------------------------------------------------------------------------------
import time

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


@route("/index.html")
def index():
    with open("./H1153/index.html") as f:
        content = f.read()
    return content


@route("/login.html")
def login():
    return "这是登录页面"


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8')])

    file_name = env['PATH_INFO']
    """
    if file_name == '/index.py':
        return index()
    elif file_name == '/login.py':
        return login()
    else:
        return 'Hello World! 我爱你中国。'
"""
    try:
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常： %s" % str(ret)