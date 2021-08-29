# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from mySpider import settings
from mySpider.models import Comic, ComicChapter
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request


class MyspiderPipeline:
    def __init__(self):
        host = settings.MYSQL_HOST
        port = settings.MYSQL_PORT
        dbname = settings.MYSQL_DBNAME
        user = settings.MYSQL_USER
        passwd = settings.MYSQL_PASSWD
        print(host, port, dbname, user, passwd)
        self.comics = {}

        # 初始化数据库连接
        engine = create_engine("mysql+pymysql://"+user+":" +
                               passwd+"@"+host+"/"+dbname, encoding="utf-8", echo=True)

        # 创建session类型
        DBSession = sessionmaker(bind=engine)

        # 创建session对象
        self.session = DBSession()

    def process_item(self, item, spider):
        comic = Comic(comic_id=item['comic_id'], name=item['name'], intr=item['intr'],
                      cover=item['cover'], last_short_title=item['last_short_title'], author=item['author'])
        self.comics[item['comic_id']] = comic
        # comic_chapter = ComicChapter(comic_id=item['comic_id'], chapter_id=item['chapter_id'], short_title=item['chapter_short_title'],
        #                              urls=item['urls'], title=item['chapter_title'], pub_time=item['chapter_time'], paths=item['paths'])
        # 添加到session
        # session.add_all([new_user1,new_user2,new_user3])
        # self.session.add_all([comic_chapter])

        # 提交即保存到数据库
        # self.session.commit()
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

    def close_spider(self, spider):

        self.session.add_all(self.comics.values())
        self.session.commit()
        # 关闭session
        self.session.close()


class ImgDownloadPipeline(ImagesPipeline):
    default_headers = {
        'accept': 'image/webp,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'cookie': 'bid=yQdC/AzTaCw',
        'referer': 'https://www.douban.com/photos/photo/2370443040/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def get_media_requests(self, item, info):
        for image_url in json.loads(item['urls']):
            self.default_headers['referer'] = image_url
            yield Request(image_url, headers=self.default_headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['paths'] = json.dumps(image_paths)

        return item
