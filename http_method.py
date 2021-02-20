#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import time

def http_get(url):

    """
    request website content using http get method
    """

    content = ""
    for i in range(10):
        try:
            content =request.urlopen(url).read().decode('utf-8')
        except Exception as e:
            content = ""
            time.sleep(1)
        else:
            time.sleep(0.5)
            break

    return content

if __name__ == "__main__":

    """
    This is for test
    """

    # content = http_get("https://blog.csdn.net/imnisen1992/article/details/53165112")
    # print(content)
    # content = http_get("https://blog.csdn.net/jcjc918")
    # print(content)
    content = http_get("https://yinwang1.wordpress.com/author/yinwang0/")
    print(content)
