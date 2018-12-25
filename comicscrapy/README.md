# comicspider

## [漫画爬虫，将数据储存到mysql](README.md)
 
 爬取的漫画数据来源于163漫画，https://manhua.163.com
 
 启动命令
 ```python
scrapy crawl manhua163 #或者直接 python start.py
```
### scrapy配置mysql,在文件[/comicspider/comicscrapy/comicscrapy/settings.py](comicspider/comicscrapy/comicscrapy/settings.py)里面配置
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

### 代码结构如下：
```markdown
comicspider
├── comicscrapy
│   ├── comicscrapy
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders
│   │       ├── __init__.py
│   │       ├── manhua163.py
│   ├── scrapy.cfg
│   ├── scrapy.log
│   └── start.py
├── comicspider
│   ├── __init__.py
│   ├── settings.py
│   ├── spiderfactory.py
│   ├── spiders.py
└── test


```
 