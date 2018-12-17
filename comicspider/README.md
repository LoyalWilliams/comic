# comicspider

## [漫画爬虫，将数据储存到mysql](README.md)
 
 爬取的漫画数据来源于163漫画，https://manhua.163.com
 
 启动命令
 ```python
scrapy crawl manhua163 #或者直接 python start.py
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
 