'''
Referrer source utilities

(Flames about "referer" vs. "referrer" will be sent to /dev/null.)

'''

__all__ = [
    'Referrer',
    ]

import re
from urllib import unquote_plus

#: search engine recognition regexes.  (name, regex)
SE_REGEXES = [
    ('google',    re.compile(r'^http://[a-zA-Z.]*google\.\w+(\.\w+)?/.*\bq=(?P<searchphrase>[^&]*)')),
    ('bing',      re.compile(r'^http://[a-zA-Z.]*bing.com/.*\bq=(?P<searchphrase>[^&]*)')),
    ('yahoo',     re.compile(r'^http://[a-zA-Z0-9.]*yahoo\.\w+(\.\w+)?/.*\bp=(?P<searchphrase>[^&]*)')),
    ('duckduckgo', re.compile(r'^http://duckduckgo.com/.*\bq=(?P<searchphrase>[^&]*)')),
    ('ask',       re.compile(r'^http://[a-zA-Z.]*ask.com/.*\bq=(?P<searchphrase>[^&]*)')),
    ('yandex',    re.compile(r'^http://yandex.ru/.*\btext=(?P<searchphrase>[^&]*)')),
    ]

class Referrer(object):
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

    def __init__(self, referrer):
        '''
        ctor
        
        @param referrer : Referrer ("referer") string
        @type  referrer : str
        
        '''
        self.referrer = referrer
        for k, v in referrer_info(referrer).iteritems():
            setattr(self, k, v)

def referrer_info(referrer):
    '''
    Referrer information dictionary

    This is essentially an alternative interface to getting the
    information from the Referrer class.  In most Python
    implementations, such as CPython, object creation is slow compared
    to dictionary creation by a factor of 3 or so.  In performance
    sensitive applications, you can use this instead of creating the
    Referrer class.

    The returned dictionary will at least contain an is_search key,
    valued True or False.  If True, the dict will also contain the
    following other keys:

      searchengine
      searchphrase

    See the documentation of the Referrer class for their meaning.

    @param referrer : Referrer ("referer") string
    @type  referrer : str
        
    @return : referrer information
    @rtype  : dict
    
    '''
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

