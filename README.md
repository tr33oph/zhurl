# zhurl
中文域名、URL的punycode互转。

##使用方法

下载zhurl.py到引用它的脚本的工作目录下。

```python
import zhurl
>>> zhurl.encode_url(u'http://www.李嘉诚.com/')
u'http://www.xn--w4rt51b8s1a.com/'
>>> print zhurl.decode_url(u'http://www.xn--w4rt51b8s1a.com/')
http://www.李嘉诚.com/
```
