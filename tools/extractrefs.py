#!/usr/bin/env python2.6
'''
Extract user agent strings from a text file of Apache "combined" log records

This tool is used to get test data.

usage:

  extractref.py < raw-logs.txt > refs.txt
  
You may want to pipe the output through "| sort | uniq".

Records with referrer '-' (meaning unknown referrer) are omitted.

This is a quick-n-dirty, mostly but not totally accurate script.
  
'''

def referrer(logline):
    '''
    Extracts the referrer string from an Apache web server "combined" log file record

    '''
    parts = logline.split('"')
    return parts[3]

if '__main__' == __name__:
    import sys
    for line in sys.stdin:
        if '-' != line:
            print referrer(line)
