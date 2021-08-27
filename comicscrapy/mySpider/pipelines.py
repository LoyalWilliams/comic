# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from mySpider import settings
from mySpider.models import Comic,ComicChapter
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class MyspiderPipeline:
    def __init__(self):
        host = settings.MYSQL_HOST
        port = settings.MYSQL_PORT
        dbname = settings.MYSQL_DBNAME
        user = settings.MYSQL_USER
        passwd = settings.MYSQL_PASSWD
        print(host,port,dbname,user,passwd)
        self.comics={}
     
        #初始化数据库连接
        engine = create_engine("mysql+pymysql://"+user+":"+passwd+"@"+host+"/"+dbname,encoding="utf-8",echo=True)
        
        #创建session类型
        DBSession = sessionmaker(bind=engine)
        
        #创建session对象
        self.session = DBSession()
        
    def process_item(self, item, spider):
        comic=Comic(comic_id=item['comic_id'],name=item['name'],intr=item['intr']
        ,cover=item['cover'],last_short_title=item['last_short_title'],author=item['author'])
        self.comics[item['comic_id']]=comic
        comic_chapter=ComicChapter(comic_id=item['comic_id'],chapter_id=item['chapter_id'],short_title=item['chapter_short_title'],
        urls=item['urls'],title=item['chapter_title'],pub_time=item['chapter_time'])
        #添加到session
        # session.add_all([new_user1,new_user2,new_user3])
        self.session.add_all([comic_chapter])
        
        #提交即保存到数据库
        self.session.commit()
#         try:
#             self.cur.execute(sql)
#             self.db.commit()
#             return item
#         except Exception, e:
#             print '########################################################'
#             print 'str(Exception):\t', str(Exception)
#             print 'str(e):\t\t', str(e)
#             print 'repr(e):\t', repr(e)
#             print 'e.message:\t', e.message
#             print 'traceback.print_exc():';
#             traceback.print_exc()
#             print 'traceback.format_exc():\n%s' % traceback.format_exc()
#             print 'mysql insert exception:'+sql.encode('utf8')
#             print '########################################################'

    def close_spider(self,spider):
        
        self.session.add_all(self.comics.values())
        self.session.commit()
        #关闭session
        self.session.close()
