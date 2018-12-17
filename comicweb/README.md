# comicweb

## [漫画网站搭建，展示](README.md)
 
  启动命令
 ```python
python start.py #或者直接 python manage.py runserver 8001
```

启动成功后，访问http://localhost:8001/comic/

 <img src='/pic/1.jpg' width=300px></img>
 
 <img src='/pic/2.jpg' width=300px></img>
 
  <img src='/pic/3.jpg' width=300px></img>
  

### Django配置mysql,在文件[/comicweb/comicweb/settings.py](comicweb/comicweb/settings.py)里面配置
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

### 代码结构如下：
 ```markdown
 
comicweb
├─comic
│  └─migrations
├─comicspider
├─comicweb
├─static
│  ├─comic
│  │  ├─css
│  │  ├─images
│  │  ├─img
│  │  └─script
│  └─test
│      ├─css
│      └─script
└─templates
    └─comic
comicweb
├── comic
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20181204_1607.py
│   │   ├── 0003_auto_20181204_1818.py
│   │   ├── 0004_auto_20181204_1906.py
│   │   ├── 0005_auto_20181204_1909.py
│   │   ├── 0006_auto_20181204_2017.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── comicspider
│   ├── __init__.py
│   ├── settings.py
│   ├── spiderfactory.py
│   ├── spiders.py
├── comicweb
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── start.py
├── static
│   ├── comic
│   │   ├── chapterContent.html
│   │   ├── comicInfo.html
│   │   ├── css
│   │   │   ├── global.css
│   │   │   ├── ...
│   │   │   └── view.css
│   │   ├── images
│   │   │   ├── 039ac725a6d64215a61c3d8a9edf9faa.png
│   │   │   ├── 14927c3dd7844200b520e910b993769e.png
│   │   │   ├── ...
│   │   │   └── view-logo-read.png
│   │   ├── img
│   │   ├── script
│   │   │   ├── common.js
│   │   │   ├── jquery-1.9.1.min.js
│   │   │   ├── jquery.cookie.js
│   │   │   ├── jquery.min.js
│   │   │   ├── ...
│   │   │   └── TSB.js
│   │   └── test.html
│   └── test
│       ├── css
│       │   └── toPage.css
│       ├── index.html
│       └── script
│           ├── jquery.min.js
│           └── toPage.js
├── templates
│   └── comic
│       ├── chapterContent.html
│       ├── comicInfo.html
│       ├── index.html
│       ├── search.html
│       └── test.html
└── uwsgi.ini

```