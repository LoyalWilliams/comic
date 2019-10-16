#coding=utf-8
from comicspider import spiderfactory
import execjs
import re
import json

spider=spiderfactory.getSpider('https://ac.qq.com/ComicView/index/id/636058/cid/6')

# 测试破解加密算法
def testDecodeImgpath():
    html = spider.getSourceCode('https://ac.qq.com/ComicView/index/id/629632/cid/45')
    data = re.findall(r"var DATA\s*= '(.*)'", html)[0]
    nonce = re.findall(r'window\[".*=(.*);', html)[0]
    nonce = execjs.eval(nonce)
    print spider.decodeImgpath(data,nonce)


# 测试获取图片的真实路径列表
def testGetImgRealPath():
    # print spider.getImgRealPath('https://ac.qq.com/ComicView/index/id/628543/cid/1')
    print spider.getImgRealPath('https://ac.qq.com/ComicView/index/id/635032/cid/14')

# 测试获取漫画的章节列表
def testGetChapters():
    chapters = spider.getChapters('https://ac.qq.com/Comic/comicInfo/id/627718')
    for ch in chapters:
        print ch.get('title'),ch.get('chapterUrl')

# 测试获取第一章图片的真实路径列表
def testFirstChapterImg():
    firstChapter=spider.getChapters('https://ac.qq.com/Comic/comicInfo/id/627718')[0]
    print firstChapter['chapterUrl'],firstChapter['title']
    print spider.getImgRealPath(firstChapter['chapterUrl'])


# testDecodeImgpath()
# testGetImgRealPath()
# testGetChapters()
testFirstChapterImg()

