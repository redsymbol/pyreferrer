'''
Referrer source utilities

(Flames about "referer" vs. "referrer" will be sent to /dev/null.)

'''

__all__ = [
    'Referral',
    ]

import re
from urllib import unquote_plus

#: search engine recognition regexes.  (name, regex)
SE_REGEXES = [
    ('google',    re.compile(r'^http://[a-zA-Z.]*google\.\w+(\.\w+)?/.*\bq=(?P<searchphrase>[^&]*)')),
    ('bing',      re.compile(r'^http://[a-zA-Z.]*bing.com/.*\bq=(?P<searchphrase>[^&]*)')),
    ('yahoo',     re.compile(r'^http://[a-zA-Z0-9.]*yahoo\.\w+(\.\w+)?/.*\bp=(?P<searchphrase>[^&]*)')),
    ]

class Referral(object):
    '''
    Represents a request's referrer source, and information extracted from it

    You'll be interested in the following properties:
      is_search
      searchengine
      searchphrase
      referrer

    '''
    #: True or False depending on whether the referrer is a known search engine.
    is_search    = None
    #: The search engine name ('google', 'bing', etc.), or None if is_search is False
    searchengine = None
    #: The search phrase typed by the user, or None if is_search is False
    searchphrase = None
    #: The original, full referrer string
    referrer     = None

    # future:
    # is_bot
    
    def __init__(self, referrer):
        '''
        ctor
        
        @param referrer : Referrer ("referer") string
        @type  referrer : str
        
        '''
        self.referrer = referrer
        for k, v in _referral(referrer).iteritems():
            setattr(self, k, v)

def _referral(referrer):
    params = {
        'is_search' : False,
        }
    for name, regex in SE_REGEXES:
        match = regex.search(referrer)
        if match:
            params.update({
                    'is_search' : True,
                    'searchengine' : name,
                    'searchphrase' : unquote_plus(match.group('searchphrase')).strip(),
                    })
            break
    return params

