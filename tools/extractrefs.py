#!/usr/bin/env python2.6
'''
Extract user agent strings from a text file of Apache "combined" log records

This tool is used to get test data.

usage:

  extractuas.py < raw-logs.txt > uas.txt
  
You may want to pipe the output through "| sort | uniq".
  
'''

import pyparsing
