#coding=utf-8
import re
from comicspider.spiders.defaultSpider import DefaultSpider

class ShenmanhuaSpider(DefaultSpider):
    baseUrl = 'https://www.shenmanhua.com/'

    def getChapters(self,url):
        chapters=DefaultSpider.getChapters(self,url)
        chapters.reverse()
        return chapters

    # 获取服务器域名接口 https://server.cnmanhua.com/mhpic.asp?callback=__cr.setLine
    # 图片的真实路径为 https:// + 域名 + /comic/ + 破解后的mh_info.imgpath +.(mh_info.image_suffix 或者 jpg)+  mh_info.comic_size+ .webp可要可不要;
    def getImgRealPath(self,url):
        html = self.getSourceCode(url)
        info = re.findall(r'var mh_info={(.*?)}', html)[0]
        imgpath = re.findall(r'imgpath:"(.*?)"', info)[0]
        pageid = re.findall(r'pageid:(\d+)', info)[0]
        comic_size = re.findall(r'comic_size:"(.*?)"', info)[0]
        startimg = re.findall(r'startimg:(\d+)', info)[0]
        totalimg = re.findall(r'totalimg:(\d+)', info)[0]
        image_suffix = re.findall(r'image_suffix:"(.*?)"', info)
        if len(image_suffix) != 0:
            image_suffix = image_suffix[0]
        else:
            image_suffix = 'jpg'
        imgpath = self.decodeImgpath(imgpath, int(pageid))
        l = []
        for page in range(int(startimg), int(startimg) + int(totalimg)):
            l.append([
                'https://mhpic.jumanhua.com/comic/' + imgpath + str(page) + '.' + image_suffix + comic_size + '.webp',
                'https://mhpic.jumanhua.com/comic/' + imgpath + str(page) + '.' + image_suffix + comic_size
            ])
        return l

    # 破解加密算法 mh_info.imgpath.replace(/./g,function(a){return String.fromCharCode(a.charCodeAt(0)-mh_info.pageid%10)})
    def decodeImgpath(self, imgpath, pageid):
        path = ''
        for i in imgpath.replace('\\',''):
            path = path + chr(ord(i) - pageid % 10)
        return path


shenmanhua=ShenmanhuaSpider()
