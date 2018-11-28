#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http_method import http_get
from parse_string import parse_string

def backup_website(target_website, author_domain, http_type):

    """
    This is used to backup given website
    """

    response=http_get(target_website)
    title, text_list, href_list = parse_string(response, author_domain)

    if text_list:
        directory = './backup/' + author_domain
        filename = (directory + '/' + title + ".txt").encode()
        print("Save %s ---------------------------> %s" % (target_website, filename))

        fd = open(filename, 'wb')
        for text in text_list:
            write_bin_text = (text + '\n').encode()
            fd.write(write_bin_text)
        fd.close()

    for key in href_list:
        href = href_list[key]
        if href:
            href = http_type + "://" + author_domain + href
            backup_website(href, author_domain, http_type)

if __name__ == "__main__":

    """
    This is for test purpose
    """

    url = "http://www.yinwang.org"
    domain = "www.yinwang.org"
    backup_website(url, domain, "http")
