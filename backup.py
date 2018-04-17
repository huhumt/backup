#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os_proc import create_directory
from http_method import http_get

def backup_website(target_website):

    """
    This is used to backup given website
    """
    create_directory(target_website)

if __name__ == "__main__":

    """
    This is for test purpose
    """

    backup_website("www.baidu.com")
