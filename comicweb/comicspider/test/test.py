#coding=utf-8
from comicspider import spiderfactory
import re
import json
shenmanhua=spiderfactory.getSpider('https://www.shenmanhua.com/shenyidinv/')
def testChapters():
    print shenmanhua.getChapters('https://www.shenmanhua.com/shenyidinv/')

# testChapters()

# with open('test2.html','w') as f:
#     f.write(shenmanhua.getSourceCode('https://www.shenmanhua.com/shenyidinv/6003.html'))
# 加密算法 mh_info.imgpath.replace(/./g,function(a){return String.fromCharCode(a.charCodeAt(0)-mh_info.pageid%10)})
# 获取服务器接口 https://server.cnmanhua.com/mhpic.asp?callback=__cr.setLine
pageid=1433782
imgpath="U\'4H\'G9\'C7\';G\'G7\':E\'DD\'G7\'CD\'C3\'G7\'C7\'D5\'4H\'G9\'CE\'CE8\'G:\'CH\';FIS\'4H"
path=''
for i in imgpath:
    path = path+chr(ord(i)-pageid%10)
print path
# print imgpath
def decodeImgpath(imgpath,pageid):
    path = ''
    for i in imgpath:
        path = path + chr(ord(i) - pageid % 10)
    return path

html=shenmanhua.getSourceCode('https://www.shenmanhua.com/doupocangqiong/dpcq_5h.html')
with open('test2.html','w') as f:
    f.write(html)
pattern=re.compile(r'var mh_info={(.*?)}')
# imgpath:"P+8L+K=+HH+?J+K:+H>+?<+K;+?:+?6+K?+?=+G>+K<+>H+><+K;+>>+><+K=+>?+>>+8L:8:+K>+GL+?JMW+8L",startimg:2,totalimg:13,mhid:"jueshitangmen",mhname:"绝世唐门",pageid:1591276,pagename:"第424话 雪舞极冰域",pageurl:"424",readmode:1,maxpreload:5,defaultminline:1,domain:"cnmanhua.com",comic_size:"-smh.middle",default_price:99,price:0,time_diff:1631310830,image_suffix:"jpg"
info = re.findall(pattern,html)[0]
imgpath= re.findall(r'imgpath:"(.*?)"',info)[0]
print info
pageid= re.findall(r'pageid:(\d+)',info)[0]
print 'imgpath:',len(imgpath.replace('\\',''))

# F'4H'G8';8';9'G9'C2'D6'G:':D':F'G9'C;'D;'G8':D':8'G7'::':8'G9':;'::'4H7'G:'CH';F'4H
# F\'4H\'G8\';8\';9\'G9\'C2\'D6\'G:\':D\':F\'G9\'C;\'D;\'G8\':D\':8\'G7\'::\':8\'G9\':;\'::\'4H7\'G:\'CH\';F\'4H

# print pageid,type(pageid)
# print decodeImgpath(imgpath,int(pageid))

#         var i = lines[chapter_id].use_line,
#         o = "." + (mh_info.image_suffix || "jpg").toLowerCase(),
#         t = parseInt(mh_info.startimg) + e - 1 + o,
#         n = "https://" + i + "/comic/" + mh_info.imgpath + t;
#         return __cr.switchWebp(n, mh_info.comic_size)

# 获取服务器域名接口 https://server.cnmanhua.com/mhpic.asp?callback=__cr.setLine
# 图片的真实路径为 https:// + 域名 + /comic/ + 破解后的mh_info.imgpath +.(mh_info.image_suffix 或者 jpg)+  mh_info.comic_size+ .webp可要可不要;
def getImgRealPath(html):
    info = re.findall(r'var mh_info={(.*?)}', html)[0]
    imgpath = re.findall(r'imgpath:"(.*?)"', info)[0]
    pageid = re.findall(r'pageid:(\d+)', info)[0]
    comic_size = re.findall(r'comic_size:"(.*?)"', info)[0]
    startimg = re.findall(r'startimg:(\d+)', info)[0]
    totalimg = re.findall(r'totalimg:(\d+)', info)[0]
    image_suffix = re.findall(r'image_suffix:"(.*?)"', info)
    if len(image_suffix)!=0:
        image_suffix=image_suffix[0]
    else:
        image_suffix='jpg'
    imgpath = decodeImgpath(imgpath,int(pageid))
    l=[]
    for page in range(int(startimg),int(startimg)+int(totalimg)):
        l.append('https://mhpic.jumanhua.com/comic/'+imgpath+str(page)+'.'+image_suffix+comic_size+'.webp')
    return l

# print getImgRealPath()
