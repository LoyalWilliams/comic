#coding=utf-8
from comicspider import spiderfactory
import re

spider=spiderfactory.getSpider('https://www.shenmanhua.com/shenyidinv/')

# 测试获取图片的真实路径列表
def testGetImgRealPath():
    print spider.getImgRealPath('https://www.shenmanhua.com/jueshitangmen/424.html')

# 测试获取漫画的章节列表
def testGetChapters():
    print spider.getChapters('https://www.shenmanhua.com/fengqicanglan/')

# 测试获取第一章图片的真实路径列表
def testFirstChapterImg():
    firstChapter=spider.getChapters('https://www.shenmanhua.com/fengqicanglan/')[0]
    print firstChapter['chapterUrl'],firstChapter['title']
    print spider.getImgRealPath(firstChapter['chapterUrl'])



testGetImgRealPath()
# testGetChapters()
# testFirstChapterImg()

