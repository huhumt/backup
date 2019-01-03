#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def parse_string(full_str, author_domain):

    """
    parse full_str with begin_str and end_str
    """

    # search title between <head>...</head> using flag of <tilte>...</title>
    # search text between <body>...</body> using flag of <p>...</p>
    search_enable_flag = 0
    title = ""
    body_text_list = []
    href_list = []
    for line in full_str.splitlines():
        if search_enable_flag == 0:
            if '<head' in line or '<body' in line:
                search_enable_flag = 1
        else:
            if '</head>' in line or '</body>' in line:
                search_enable_flag = 0
            elif '<title>' in line and '</title>' in line:
                title = re.findall(r'<title>(.*?)</title>', line)[0]
                title = title.replace("/", "\\/")
            elif '<p>' in line and '</p>' in line:
                text_line = re.findall(r'<p>(.*?)</p>', line)[0]
                body_text_list.append(text_line)
            elif '<a href="' in line:
                value = re.findall(r'<a href="(.*?)"', line)[0]
                key = value.split(author_domain, 1)[-1]
                if not key:
                    key = "HomePage"
                else:
                    key = "_".join(key.split("/"))

                if key != "HomePage":
                    if "http" not in value and '/' in value and '?' not in value and '#' not in value:
                        if value != "#":
                            href_list.append(value)
                    elif (author_domain + '/') in value and '?' not in value and '#' not in value:
                        if value != "#":
                            href_list.append(value.split(author_domain, 1)[1])
                    else:
                        body_text_list.append(key + '--->' + value)

    return title, body_text_list, href_list

if __name__ == "__main__":

    """
    this is only for test
    """

    full_str=("<head>\n"
              "    abcdefg\n"
              "    <title>haha</title>\n"
              "</head>\n"
              "adfafg\n"
              "<body>\n"
              "    <p>hehe</p>\n"
              "<body>\n"
              "dada")
    title, body_text_list = parse_string(full_str)
    print(full_str)
    print(title)
    print(body_text_list)
