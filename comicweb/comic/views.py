# coding=utf-8
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from comic.models import Comic
from comicspider import spiderfactory


# def getRecommend(request):
#     return render(request, 'comic/chapterContent.html', context)

def getContent(request):
    chapterUrl=request.GET.get('chapterUrl',None)
    comicname=request.GET.get('comicname',None)
    chaptername=request.GET.get('chaptername',None)
    comicid=request.GET.get('comicid',None)
    spider= spiderfactory.getSpider(chapterUrl)
    content=spider.getImgRealPath(chapterUrl)
    comicManager = Comic.comicManager
    comic = comicManager.get(Q(id=int(comicid)))
    infoUrl=comic.comic_url

    context={"content":content,
             'len':len(content),
             'chaptername':chaptername,
             'comicname':comicname,
             'infoUrl':infoUrl,
             'chapterUrl':chapterUrl,
             'comicid':comicid,
             }
    return render(request, 'comic/chapterContent.html',context )

def index(request):
    spider= spiderfactory.getSpider('https://163.bilibili.com')
    recommends=spider.getRecommend()
    comicManager=Comic.comicManager
    for recommend in recommends:
        print recommend['url']
        # recommend['comicid']=comicManager.get(Q(comic_url=recommend['url'])).id
        comiclist=comicManager.filter(Q(comic_url=recommend['url']))
        if(len(comiclist)==0):
            recommend['comicid']=0
        else:
            recommend['comicid'] = comiclist[0].id
    type1=comicManager.getType1()[0:3]
    type2=comicManager.getType2()[0:3]
    type3=comicManager.getType3()[0:3]
    type4=comicManager.getType4()[0:3]
    type5=comicManager.getType5()[0:3]
    type6=comicManager.getType6()[0:3]
    type7=comicManager.getType7()[0:3]
    type8=comicManager.getType8()[0:3]
    k1 = (u'热血,战斗,武侠', type1)
    k2 = (u'恋爱,后宫', type2)
    k3 = (u'恐怖,悬疑', type3)
    k4 = (u'治愈,儿童,唯美', type4)
    k5 = (u'搞笑,萌系', type5)
    k6 = (u'古风,穿越,冒险', type6)
    k7 = (u'校园,都市', type7)
    k8 = (u'魔幻,科幻,玄幻', type8)
    context={'comiclist':[k1,k2,k3,k4,k5,k6,k7,k8],
             'recommends':recommends,
             }
    return render(request,'comic/index.html',context)

def getComicInfo(request):
    infourl=request.GET.get('infourl',None)
    comicid=request.GET.get('comicid',None)
    spider = spiderfactory.getSpider(infourl)
    chapters=spider.getChapters(infourl)
    comic=Comic.comicManager.get_queryset().filter(pk=int(comicid)).get()
    return render(request,'comic/comicInfo.html',{'chapters':chapters,'comic':comic,})

def preChapter(request):
    infoUrl = request.GET.get('infoUrl', None)
    chapterUrl = request.GET.get('chapterUrl', None)
    comicname = request.GET.get('comicname', None)
    comicid = request.GET.get('comicid', None)
    spider= spiderfactory.getSpider(infoUrl)
    chapters=spider.getChapters(infoUrl)
    # print chapters
    preUrl=chapters[0].get('chapterUrl')
    title = chapters[0].get('title')
    for i in range(1,len(chapters)):
        if chapterUrl==chapters[i].get('chapterUrl'):
            preUrl = chapters[i - 1].get('chapterUrl')
            title = chapters[i - 1].get('title')
            break

    content = spider.getImgRealPath(preUrl)
    context = {"content": content,
               'len': len(content),
               'chaptername': title,
               'comicname': comicname,
               'infoUrl': infoUrl,
               'chapterUrl': preUrl,
               'comicid': comicid,
               }
    return render(request, 'comic/chapterContent.html', context)


def nextChapter(request):
    infoUrl = request.GET.get('infoUrl', None)
    chapterUrl = request.GET.get('chapterUrl', None)
    comicname = request.GET.get('comicname', None)
    comicid = request.GET.get('comicid', None)
    spider = spiderfactory.getSpider(infoUrl)
    chapters = spider.getChapters(infoUrl)
    # print chapters
    nextUrl = chapters[len(chapters)-1].get('chapterUrl')
    title=chapters[len(chapters)-1].get('title')
    for i in range(0, len(chapters)):
        if chapterUrl == chapters[i].get('chapterUrl'):
            nextUrl = chapters[i + 1].get('chapterUrl')
            title = chapters[i + 1].get('title')
            break
    content = spider.getImgRealPath(nextUrl)
    context = {"content": content,
               'len': len(content),
               'chaptername': title,
               'comicname': comicname,
               'infoUrl': infoUrl,
               'chapterUrl': nextUrl,
               'comicid': comicid,
               }
    return render(request, 'comic/chapterContent.html', context)

def indexMore(request):
    typenum = request.POST.get('typenum', None)
    page = request.POST.get('page', None)
    typenum=int(typenum)
    page=int(page)
    # 3+(page-1)*6,3+page*6
    comicManager = Comic.comicManager
    if typenum==0:
        comics=comicManager.getType1()
    elif typenum==1:
        comics = comicManager.getType2()
    elif typenum==2:
       comics = comicManager.getType3()
    elif typenum==3:
       comics = comicManager.getType4()
    elif typenum==4:
       comics = comicManager.getType5()
    elif typenum==5:
       comics = comicManager.getType6()
    elif typenum==6:
        comics = comicManager.getType7()
    elif typenum==7:
        comics = comicManager.getType8()
    comics=comics[3+(page-1)*6:3+page*6]
    # print comics.values
    context = {'comics': list(comics.values()),
               }
    return JsonResponse(context)

def search(request):
    comicManager = Comic.comicManager
    keyword=request.GET.get('kw', None)
    comics = comicManager.getComicsByAuthorOrName(keyword)
    k1 = (u'查找结果', comics)
    context = {'comiclist': [k1],
               }
    print keyword
    return render(request, 'comic/search.html', context)
