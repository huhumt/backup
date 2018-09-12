#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

def create_directory(directory):

    """
    Create a new directory if no exist
    """

    if os.path.exists(directory):
        print("%s already exists" % (directory))
    else:
        os.makedirs(directory)

def change_directory(directory):

    """
    Change directory
    """

    if os.path.exists(directory):
        os.chdir(directory)
    else:
        print("%s does not exist" % (directory))

def remove_directory(directory):

    """
    Remove directory recursively
    """

    if os.path.exists(directory):
        shutil.rmtree(directory)
    else:
        print("%s does not exist" % (directory))

if __name__ == "__main__":

    """
    This is for test
    """

    create_directory("./test_dir")
    create_directory("./test_dir")
    change_directory("./test_dir")
    create_directory("./test_dir")
    change_directory("../")
    remove_directory("./test_dir")
    change_directory("./test_dir")
