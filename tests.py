#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zhurl

def test_domain(domain):
    en = zhurl.encode_domain(domain)
    print 'Origin:', domain
    print 'Encoded:', en
    assert  zhurl.decode_domain(en) == domain
    

def test_url(url):
    en = zhurl.encode_url(url)
    print 'Origin:', url
    print 'Encoded:', en
    assert  zhurl.decode_url(en) == url
    
def test_text(text):
    print 'Decoded text:'
    print zhurl.decode_text(text)
    
if __name__ == '__main__':
    test_domain(u'www.李嘉诚.com')
    test_url(u'http://www.李嘉诚.中国/index.php?id=1')
    test_text(u'''
    HTTP/1.1 200 OK
    Server: Apache
    X-Frame-Options: SAMEORIGIN, SAMEORIGIN
    Set-Cookie: qtrans_cookie_test=qTranslate+Cookie+Test; path=/; domain=www.xn--w4rt51b8s1a.com
    ''')