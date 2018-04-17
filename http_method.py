#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

def http_get(url):

    """
    request website content using http get method
    """

    fd = request.urlopen(url)

    return fd.read().decode('utf-8')
