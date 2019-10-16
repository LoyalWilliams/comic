# -*- coding: utf-8 -*-

import pymysql
from scrapy.conf import settings
import datetime
import traceback
import crawler.settings
class ComicscrapyPipeline(object):
    def __init__(self):
        host = settings["MYSQL_HOST"]
        port = settings["MYSQL_PORT"]
        dbname = settings["MYSQL_DBNAME"]
        user = settings["MYSQL_USER"]
        passwd = settings["MYSQL_PASSWD"]
        print host,port,dbname,user,passwd
        self.db = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=dbname, charset='utf8')
        self.cur = self.db.cursor()

    def process_item(self, item, spider):
        sql='''
INSERT INTO comic (author,name,intr,cover,comic_url,comic_type,comic_type2,collection,recommend,praise,roast,last_update_chapter,last_update_time,status,add_time) 
VALUES ('%(author)s','%(name)s','%(intr)s','%(cover)s','%(comic_url)s','%(comic_type)s','%(comic_type2)s',%(collection)d,%(recommend)d,%(praise)d,%(roast)d,'%(last_update_chapter)s','%(last_update_time)s',%(status)d,'%(add_time)s') 
ON DUPLICATE KEY UPDATE author='%(author)s',name='%(name)s',intr='%(intr)s',cover='%(cover)s',comic_url='%(comic_url)s',
comic_type='%(comic_type)s',comic_type2='%(comic_type2)s',collection=%(collection)d,recommend=%(recommend)d,praise=%(praise)d,
roast=%(roast)d,last_update_chapter='%(last_update_chapter)s',last_update_time='%(last_update_time)s',status=%(status)d
'''
        now = datetime.datetime.now()  ##now为datetime（即时间类型）
        timestr = now.strftime("%Y-%m-%d %H:%M:%S")
        item['add_time']=timestr
        sql = sql % dict(item)
        try:
            self.cur.execute(sql)
            self.db.commit()
            return item
        except Exception, e:
            print '########################################################'
            print 'str(Exception):\t', str(Exception)
            print 'str(e):\t\t', str(e)
            print 'repr(e):\t', repr(e)
            print 'e.message:\t', e.message
            print 'traceback.print_exc():';
            traceback.print_exc()
            print 'traceback.format_exc():\n%s' % traceback.format_exc()
            print 'mysql insert exception:'+sql.encode('utf8')
            print '########################################################'

    def close_spider(self,spider):
        self.db.close()

# class TestPipeline(object):
#     def process_item(self, item, spider):
#         print 'hellow'
#         return item
