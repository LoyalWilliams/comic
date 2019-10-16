#coding=utf-8
from comicspider import spiderfactory


spider=spiderfactory.getSpider('https://163.bilibili.com')

# 测试获取图片的真实路径列表
def testGetImgRealPath():
    print spider.getImgRealPath('https://163.bilibili.com/reader/4317076104890059052/4320895779440077948')

# 测试获取漫画的章节列表
def testGetChapters():
    print spider.getChapters('https://163.bilibili.com/source/4317076104890059052')

# 测试获取第一章图片的真实路径列表
def testFirstChapterImg():
    firstChapter=spider.getChapters('https://163.bilibili.com/source/4317076104890059052')[0]
    print firstChapter['chapterUrl'],firstChapter['title']
    print spider.getImgRealPath(firstChapter['chapterUrl'])



# testGetImgRealPath()
# testGetChapters()
testFirstChapterImg()