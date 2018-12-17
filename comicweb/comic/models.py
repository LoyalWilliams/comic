#coding=utf-8
from django.db import models
from django.db.models import Q,F

class ComicManager(models.Manager):
    def get_queryset(self):
        return super(ComicManager, self).get_queryset()

    def getType1(self):
        '''
        热血,战斗,武侠
        :return:
        '''
        return self.get_queryset().filter(Q(comic_type__contains=u'热血')|
                                          Q(comic_type__contains=u'战斗')|
                                          Q(comic_type__contains=u'武侠'))

    def getType2(self):
        '''
        恋爱,后宫
        :return:
        '''
        return self.get_queryset().filter(Q(comic_type__contains=u'恋爱') |
                                          Q(comic_type__contains=u'后宫'))
    def getType3(self):
        '''
        恐怖,悬疑
        :return:
        '''
        return self.get_queryset().filter(Q(comic_type__contains=u'恐怖') |
                                          Q(comic_type__contains=u'悬疑'))
    def getType4(self):
        '''
        治愈,儿童,唯美
        :return:
        '''
        return self.get_queryset().filter(Q(comic_type__contains=u'治愈') |
                                          Q(comic_type__contains=u'儿童') |
                                          Q(comic_type__contains=u'唯美'))
    def getType5(self):
        '''
        搞笑,萌系
        :return:
        '''
        return self.get_queryset().filter(Q(comic_type__contains=u'搞笑') |
                                          Q(comic_type__contains=u'萌系'))
    def getType6(self):
        '''
        古风,穿越,冒险
        :return:
        '''
        return self.get_queryset().filter(Q(comic_type__contains=u'古风') |
                                          Q(comic_type__contains=u'穿越') |
                                          Q(comic_type__contains=u'冒险'))
    def getType7(self):
        '''
        校园,都市
        :return:
        '''
        return self.get_queryset().filter(Q(comic_type__contains=u'校园') |
                                          Q(comic_type__contains=u'都市'))
    def getType8(self):
        '''
        魔幻,科幻,玄幻
        :return:
        '''
        return self.get_queryset().filter(Q(comic_type__contains=u'魔幻') |
                                          Q(comic_type__contains=u'科幻') |
                                          Q(comic_type__contains=u'玄幻'))
    def getType9(self):
        pass

    def getComicsByAuthorOrName(self,keyword):
        return self.get_queryset().filter(Q(author__contains=keyword) |
                                          Q(name__contains=keyword) )


    def toDict(self):
        return ''


class Comic(models.Model):
    author = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    intr = models.CharField(max_length=500)
    cover = models.CharField(max_length=100)
    comic_url = models.CharField(max_length=100)
    comic_type = models.CharField(max_length=20)
    comic_type2 = models.CharField(max_length=20)
    collection = models.IntegerField(default=0)
    recommend = models.IntegerField(default=0)
    praise = models.BigIntegerField(default=0)
    roast = models.BigIntegerField(default=0)
    last_update_chapter = models.CharField(max_length=50)
    last_update_time = models.DateTimeField()
    status = models.BooleanField(default=False)
    add_time = models.DateTimeField()
    isDelete = models.BooleanField(default=False)

    comicManager=ComicManager()
    class Meta():
        db_table="comic"