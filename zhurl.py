#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urlparse
import re

def en_punycode(x):
    'Encode a segment of text. Return the origin if only contains ascii.'
    if not x:
        return x
    en = x.encode('punycode')
    if en.endswith('-'): #only ASCII
        return x
    else:
        return "xn--%s"%en

def de_punycode(x):
    'Decode a segment of text. Return the origin if only not suits the url encode pattern: "xn--XXXX".'
    x = str(x)
    if x.startswith('xn--'):
        return x[4:].decode('punycode')
    else:
        return x

def encode_domain(domain):
    return '.'.join([en_punycode(i) for i in domain.split('.')])

def decode_domain(domain):
    return '.'.join([de_punycode(i) for i in domain.split('.')])

def decode_text(text):
    'Decode a segment of text. Use re to replace all text suits the url encode: "xn--XXXX".'
    def rep(x):
        try:
            return de_punycode(x.group(0))
        except:
            return x
    r = re.sub(r'(xn--[a-zA-Z0-9\-]+)', rep, text)
    return r
    
def zhurl(url, flag=False):
    'url: input url. flag: True for decode, False for encode.'
    p = urlparse.urlparse(url)
    if flag:
        domain  = decode_domain(p.netloc)
    else:
        domain  = encode_domain(p.netloc)
    p = list(p)
    p[1] = domain
    return urlparse.urlunparse(p)
    
def decode_url(url):
    return zhurl(url, True)
    
def encode_url(url):
    return zhurl(url, False)
    
if __name__ == '__main__':
    en = encode_url(u'http://www.李嘉诚.中国/index.html?sd=2')
    print en
    print decode_url(en)
    print decode_text(en+en)
    #Output:
    # http://www.xn--w4rt51b8s1a.xn--fiqs8s/index.html?sd=2
    # http://www.李嘉诚.中国/index.html?sd=2
    # http://www.李嘉诚.中国/index.html?sd=2http://www.李嘉诚.中国/index.html?sd=2
    # >>>
