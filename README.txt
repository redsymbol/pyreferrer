pyreferrer - Python library for web server referrer/origin analysis

Pyreferrer is a library to help gleen useful information from web
server referrer ("referer") strings.  It is small, providing one class
and one function.

In this current version (1.0) the primary benefit is to tell you
whether the web hit was forwarded from a search engine; and if so,
which engine, and with what search terms.  It knows about the major
search engines used by North Americans, and the plan is to add more
over time.

Some ways this can be useful:

 - Automatic analysis of visitor behavior for your Python-based
   website
 - Report search-engine origin info of visitors who take certain
   actions, such as filling out a request-for-quote form
 - Algorithmic SEO

Pyreferrer works with Python 2.6 and 2.7.  With a quick and easy patch
from 2to3, it also works great with Python 3.

INSTALL

Copy pyreferrer.py into your python path.

USAGE

Like so:

import pyreferrer

# Use the Referrer class, unless performance really matters for your
# application.  In that case use the referral_info function.

referrer_string = 'http://www.google.com/search?q=linux+boot+options'

ref = pyreferrer.Referrer(referrer_string)
ref.is_search # True
ref.searchengine # 'google'
ref.searchphrase # 'linux boot options'

ref2 = pyreferrer.Referrer('http://cnn.com')
ref2.is_search # False

# Alternatively, use the referrer_info function, which returns a
# dict instead of instantiating an object.  It's a bit faster
# (by 20-40%).
  
info = pyreferrer.referrer_info(referrer_string)
info['is_search'] # True
info['searchengine'] # 'google'
info['searchphrase'] # 'linux boot options'

info2 = pyreferrer.referrer_info('http://cnn.com')
info2['is_search'] # False

# end.

DOCUMENTATION

The best documentation is the inline code documentation in the source,
pyreferrer.py . See the docs for the Referrer class and the
referrer_info function.

You can generate nice HTML API docs with epydocs, using the "make
api-doc" command.

SEARCH ENGINES

Known search engines are listed in SE_REGEXES in pyreferrer.py.  If
you get a referrer string in your logs that isn't matched, please let
me know.  I'll need the full text of the referrer.

AUTHOR & LICENSE

Made by Aaron Maxwell (amax-at-redsymbol.net).  This software is in
the public domain.
