import unittest

from refsrc import Referral

class TestReferral(unittest.TestCase):
    def test_main(self):
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

            ]
        for ii, td in enumerate(testdata):
            ref = Referral(td['referrer'])
            self.assertEqual(td['referrer'], ref.referrer)
            self.assertEqual(td['is_search'], ref.is_search)
            self.assertEqual(td['searchphrase'], ref.searchphrase)
