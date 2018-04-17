#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from backup import backup_website

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
    '''If argv_list is empty, no target website to backup'''
    if not argv_list:
        print("Usage: python3 main.py target1 target2 ...")
        return

    for target_website in argv_list:
        backup_website(target_website)

if __name__ == "__main__":
    main()
