#!/usr/bin/python
# script to compare two checksum reports

import os, sys, os.path, difflib

file1 = open('2015-02-18_sdaCode_checksumList.txt', 'r')
file2 = open('2015-02-19_sdaCode_checksumList.txt', 'r')

diff = difflib.context_diff(file1.readlines(), file2.readlines())
delta = ''.join(diff)
print delta
