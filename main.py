#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os_proc import create_directory, change_directory
from backup import backup_website
import json
import sys

def parse_argv():

    """
    This function is used to prarse input arguments
    """

    return sys.argv[1:]

def main():

    """
    this is the main entry of the project
    """

    argv_list = parse_argv()
    '''If argv_list is empty, use json file to do backup'''
    if not argv_list:
        fd = open('target_website.json', 'r', encoding="utf-8")
        config_data = json.load(fd)
        fd.close()

        for key in config_data:
            argv_list.append(config_data[key])

    for target_website in argv_list:
        backup_website(target_website)

if __name__ == "__main__":
    main()
