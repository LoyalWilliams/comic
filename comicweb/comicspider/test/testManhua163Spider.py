#coding=utf-8
from comicspider import spiderfactory


spider=spiderfactory.getSpider('https://manhua.163.com')

# 测试获取图片的真实路径列表
def testGetImgRealPath():
    print spider.getImgRealPath('https://manhua.163.com/reader/4317076104890059052/4320895779440077948')

testGetImgRealPath()

