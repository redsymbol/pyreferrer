import unittest

from refsrc import Referral

class TestReferral(unittest.TestCase):
    def test_searchengines(self):
        testdata = [
            {'referrer' : 'http://www.google.com/search?num=30&hl=en&newwindow=1&biw=1136&bih=822&q=linux+boot+options&aq=6&aqi=g10&aql=&oq=linux+boo&gs_rfai=',
             'searchengine' : 'google',
             'searchphrase' : 'linux boot options',
             'is_search' : True,
             },
            {'referrer' : 'http://www.google.de/search?q=tex+math+to+image&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:de:official&client=firefox-a',
             'searchengine' : 'google',
             'searchphrase' : 'tex math to image',
             'is_search' : True,
             },
            {'referrer' : 'http://www.google.co.in/search?q=+++++++Language+Outside+Chomsky+Hierarchy',
             'searchengine' : 'google',
             'searchphrase' : 'Language Outside Chomsky Hierarchy',
             'is_search' : True,
             },
            {'referrer' : 'http://www.bing.com/search?q=automated+quality+assurance&qs=n&sk=&adlt=strict&first=31&FORM=PERE2',
             'searchengine' : 'bing',
             'searchphrase' : 'automated quality assurance',
             'is_search' : True,
             },
            {'referrer' : 'http://search.yahoo.co.jp/search?p=kernel+boot+parameter+linux&search.x=1&fr=top_ga1_sa&tid=top_ga1_sa&ei=UTF-8&aq=&oq=',
             'searchengine' : 'yahoo',
             'searchphrase' : 'kernel boot parameter linux',
             'is_search' : True,
             },
            {'referrer' : 'http://us.m2.yahoo.com/w/ygo-onesearch%3B_ylt=A0WTc0Lmt1ZMnx4ACwLwOS4J?p=aaron+maxwell&submit=oneSearch&.tsrc=attosus&bzc=19454&.intl=us&.lang=en&lat=40.241337&lon=-74.83738&city=Yardley&street=&state=PA&country=US',
             'searchengine' : 'yahoo',
             'searchphrase' : 'aaron maxwell',
             'is_search' : True,
             },
            {'referrer' : 'http://uk.search.yahoo.com/search?p=latex+.png&ei=utf-8&fr=iobit-trans',
             'searchengine' : 'yahoo',
             'searchphrase' : 'latex .png',
             'is_search' : True,
             },
            ]
        for ii, td in enumerate(testdata):
            ref = Referral(td['referrer'])
            self.assertEqual(td['referrer'], ref.referrer)
            self.assertEqual(td['is_search'], ref.is_search)
            self.assertEqual(td['searchphrase'], ref.searchphrase)
