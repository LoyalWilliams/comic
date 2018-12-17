# comic

这里主要包括两大部分：


 - [漫画爬虫，将数据储存到mysql](comicspider)
 - [漫画网站搭建，展示](comicweb)
 
 [流溪阁在线漫画](http://47.94.232.43/comic/)
 
 <img src='/pic/1.jpg' width=300px></img>
 
 <img src='/pic/2.jpg' width=300px></img>
 
  <img src='/pic/3.jpg' width=300px></img>
 配置mysql
 ```markdown
DROP TABLE IF EXISTS `comic`;
CREATE TABLE `comic` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `intr` varchar(500) NOT NULL,
  `cover` varchar(100) NOT NULL,
  `comic_url` varchar(100) DEFAULT NULL,
  `comic_type` varchar(20) NOT NULL,
  `comic_type2` varchar(20) NOT NULL,
  `collection` int(11) NOT NULL,
  `recommend` int(11) NOT NULL,
  `praise` bigint(20) DEFAULT NULL,
  `roast` bigint(20) NOT NULL,
  `last_update_chapter` varchar(50) NOT NULL,
  `last_update_time` datetime NOT NULL,
  `status` tinyint(1) NOT NULL DEFAULT '1',
  `add_time` datetime NOT NULL,
  `isDelete` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_key` (`name`,`author`)
) ENGINE=InnoDB AUTO_INCREMENT=1837 DEFAULT CHARSET=utf8;
```
scrapy配置mysql,在文件[comicspider/comicscrapy/comicscrapy/settings.py](comicspider/comicscrapy/comicscrapy/settings.py)里面配置
```markdown
# MONGODB 主机名
MYSQL_HOST = "127.0.0.1"
# MONGODB 端口号
MYSQL_PORT = 3306
# 数据库名称
MYSQL_DBNAME = "comic"
# 存放数据的表名称
MYSQL_TABLENAME = "comic"
MYSQL_USER='root'
MYSQL_PASSWD='123456'

```
Django配置mysql,在文件[comicweb/comicweb/settings.py](comicweb/comicweb/settings.py)里面配置
```markdown
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'comic',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
 代码总览
```markdown

comic
├── comicspider
│   ├── comicscrapy
│   │   ├── comicscrapy
│   │   │   ├── __init__.py
│   │   │   ├── items.py
│   │   │   ├── middlewares.py
│   │   │   ├── pipelines.py
│   │   │   ├── settings.py
│   │   │   └── spiders
│   │   │       ├── __init__.py
│   │   │       ├── manhua163.py
│   │   ├── scrapy.cfg
│   │   ├── scrapy.log
│   │   └── start.py
│   └── comicspider
│       ├── __init__.py
│       ├── settings.py
│       ├── spiderfactory.py
│       └── spiders.py
├── comicweb
│   ├── comic
│   │   ├── admin.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_auto_20181204_1607.py
│   │   │   ├── 0003_auto_20181204_1818.py
│   │   │   ├── 0004_auto_20181204_1906.py
│   │   │   ├── 0005_auto_20181204_1909.py
│   │   │   ├── 0006_auto_20181204_2017.py
│   │   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   ├── comicspider
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── spiderfactory.py
│   │   ├── spiders.py
│   ├── comicweb
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── manage.py
│   ├── start.py
│   ├── static
│   │   ├── comic
│   │   │   ├── chapterContent.html
│   │   │   ├── comicInfo.html
│   │   │   ├── css
│   │   │   │   ├── global.css
│   │   │   │   ├── ...
│   │   │   │   └── view.css
│   │   │   ├── images
│   │   │   │   ├── 039ac725a6d64215a61c3d8a9edf9faa.png
│   │   │   │   ├── 14927c3dd7844200b520e910b993769e.png
│   │   │   │   ├── ...
│   │   │   │   └── view-logo-read.png
│   │   │   ├── img
│   │   │   ├── script
│   │   │   │   ├── common.js
│   │   │   │   ├── jquery-1.9.1.min.js
│   │   │   │   ├── jquery.cookie.js
│   │   │   │   ├── jquery.min.js
│   │   │   │   ├── ...
│   │   │   │   └── TSB.js
│   │   │   └── test.html
│   │   └── test
│   │       ├── css
│   │       │   └── toPage.css
│   │       ├── index.html
│   │       └── script
│   │           ├── jquery.min.js
│   │           └── toPage.js
│   ├── templates
│   │   └── comic
│   │       ├── chapterContent.html
│   │       ├── comicInfo.html
│   │       ├── index.html
│   │       ├── search.html
│   │       └── test.html
│   └── uwsgi.ini
└── requirements.txt

```