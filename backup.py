#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os_proc import create_directory, change_directory
from http_method import http_get
from parse_string import parse_string
import time

def backup_website(target_website):

    """
    This is used to backup given website
    """

    time.sleep(1)
    response=http_get(target_website)
    title, text_list, href_list = parse_string(response)

    if "https" in target_website:
        directory = target_website[8:]
    elif "http" in target_website:
        directory = target_website[7:]
    directory = './backup/' + directory
    create_directory(directory)
    filename = directory + '/' + title + ".txt"
    fd = open(filename, 'w')
    print("Save %s to %s" % (target_website, filename))
    for text in text_list:
        fd.write(text + '\n')
    fd.close()

    for key in href_list:
        href = href_list[key]
        if "http" not in href:
            href = target_website + href
        backup_website(href)

if __name__ == "__main__":

    """
    This is for test purpose
    """

    backup_website("http://www.yinwang.org/blog-cn/2017/11/01/power-of-reasoning")
