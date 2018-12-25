#coding=utf-8
from comicspider import spiderfactory
import re
import json
shenmanhua=spiderfactory.getSpider('https://www.shenmanhua.com/shenyidinv/')

# html=shenmanhua.getSourceCode('https://ac.qq.com/ComicView/index/id/636058/cid/6')
html=shenmanhua.getSourceCode('https://ac.gtimg.com/media/js/ac.page.chapter.view_v2.4.0.js?v=20170622')
with open('ac.page.chapter.view_v2.4.0.js','w') as f:
    f.write(html)