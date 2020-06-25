#!/bin/python3
import sys
import os

def createWorkSpace(Name):
    os.mkdir(Name)
    os.mkdir(Name+"/Tools")


def install():
    print("Getting tools from github...")
    print("You may need to manually set them up")
    print("They are in /opt")
    a = 'git clone '
    os.system(a + '')
    os.system(a + '')
    os.system(a + '')
    os.system(a + '')
    os.system(a + '')
    os.system(a + '')
    os.system(a + '')
    os.system(a + '')
    print("Done")


