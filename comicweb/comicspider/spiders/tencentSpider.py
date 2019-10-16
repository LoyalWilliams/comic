#coding=utf-8
import json
import re
import execjs
from comicspider.spiders.defaultSpider import DefaultSpider

class TencentSpider(DefaultSpider):
    baseUrl = 'https://ac.qq.com/'

    # 图片的真实路径为
    def getImgRealPath(self,url):
        html = self.getSourceCode(url)
        # print url
        data = re.findall(r"var DATA\s*= '(.*)'", html)[0]
        nonce = re.findall(r'window\[".*=(.*);', html)[0]
        nonce = execjs.eval(nonce)
        return self.decodeImgpath(data,nonce)

    # ac.page.chapter.view_v2.4.0.js
    # 破解加密算法
    def decodeImgpath(self, DATA, nonce):
        N = re.findall('\d+[a-zA-Z]+', nonce)
        lenN = len(N)
        T = DATA
        while lenN:
            lenN = lenN - 1
            locate = re.sub(r'[a-zA-Z]', '', N[lenN])
            strS = re.sub(r'\d', '', N[lenN])
            locate = int(locate) & 255
            T = T[0:locate] + T[int(locate) + len(strS):]
        js = '''
        function Base(T) {
        	_keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
        	this.decode = function (c) {
        		var a = "",
        		b,
        		d,
        		h,
        		f,
        		g,
        		e = 0;
        		for (c = c.replace(/[^A-Za-z0-9\+\/\=]/g, ""); e < c.length; )
        			b = _keyStr.indexOf(c.charAt(e++)), d = _keyStr.indexOf(c.charAt(e++)), f = _keyStr.indexOf(c.charAt(e++)), g = _keyStr.indexOf(c.charAt(e++)), b = b << 2 | d >> 4, d = (d & 15) << 4 | f >> 2, h = (f & 3) << 6 | g, a += String.fromCharCode(b), 64 != f && (a += String.fromCharCode(d)), 64 != g && (a += String.fromCharCode(h));
        		return a = _utf8_decode(a)
        	};
        	_utf8_decode = function (c) {
        		for (var a = "", b = 0, d = c1 = c2 = 0; b < c.length; )
        			d = c.charCodeAt(b), 128 > d ? (a += String.fromCharCode(d), b++) : 191 < d && 224 > d ? (c2 = c.charCodeAt(b + 1), a += String.fromCharCode((d & 31) << 6 | c2 & 63), b += 2) : (c2 = c.charCodeAt(b + 1), c3 = c.charCodeAt(b + 2), a += String.fromCharCode((d & 15) << 12 | (c2 & 63) << 6 | c3 & 63), b += 3);
        		return a
        	}
        	return this.decode(T)
        }
        '''
        ctx = execjs.compile(js)
        text = ctx.call('Base', T)
        pics = json.loads(text)['picture']
        return [[pic['url'].encode('utf8')] for pic in pics]

tencentSpider=TencentSpider()
