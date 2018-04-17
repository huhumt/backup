#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

def create_directory(directory):

    """
    Create a new direcotry if no exist
    """

    if os.path.exists(directory):
        print("%s is already exist" %(directory))
    else:
        print("make directory %s" %(directory))
        os.makedirs(directory)

def change_directory(directory):

    """
    Change directory
    """

    if os.path.exists(directory):
        print("change to %s" %(directory))
        os.chdir(directory)
    else:
        print("%s is not exist" %(directory))

def delete_directory(directory):

    """
    Delete directory
    """

    #  if os.path.exists(directory):
    #      print("delete directory %s" %(directory))
    shutil.rmtree(directory, ignore_errors=True)
    #  else:
    #      print("%s is not exist" %(directory))


if __name__ == "__main__":

    create_directory("./test_dir")
    change_directory("./test_dir")
    delete_directory('test_dir')
    delete_directory('test_file.txt')
    change_directory("./test_dir")
