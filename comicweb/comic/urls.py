#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getContent',views.getContent,name='getContent'),
    url(r'^$',views.index,name='index'),
    # url(r'^test$',views.test,name='test'),
    url(r'^getComicInfo$',views.getComicInfo,name='getComicsInfo'),
    url(r'^preChapter',views.preChapter,name='preChapter'),
    url(r'^nextChapter',views.nextChapter,name='nextChapter'),
    url(r'^indexMore',views.indexMore,name='indexMore'),
    url(r'^search',views.search,name='search'),
]