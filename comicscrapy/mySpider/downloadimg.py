# import requests
# from models import Comic,ComicChapter
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import json 
# import settings
 
# def download_img(img_url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
#     }
#     r = requests.get(img_url, headers=headers, stream=True)
#     # print(r.status_code) # 返回状态码
#     if r.status_code == 200:
#         # 截取图片文件名
#         img_name = img_url.split('/').pop()
#         with open(img_name, 'wb') as f:
#             f.write(r.content)
#         return True
 
 
# if __name__ == '__main__':
#     host = settings.MYSQL_HOST
#     port = settings.MYSQL_PORT
#     dbname = settings.MYSQL_DBNAME
#     user = settings.MYSQL_USER
#     passwd = settings.MYSQL_PASSWD
#     print(host,port,dbname,user,passwd)

    
#     #初始化数据库连接
#     engine = create_engine("mysql+pymysql://"+user+":"+passwd+"@"+host+"/"+dbname,encoding="utf-8",echo=True)
    
#     #创建session类型
#     DBSession = sessionmaker(bind=engine)

#     #创建session对象
#     session = DBSession()
#     comic_chapters = session.query(ComicChapter).all()
#     for i in comic_chapters:
#         print(i.urls)
#     # session.commit()
#     # print(comic_chapters[0]['urls'])
    
    
#     # 下载要的图片
#     # img_url = "http://www.py3study.com/Public/images/article/thumb/random/48.jpg"
#     # ret = download_img(img_url)
#     # if not ret:
#     #     print("下载失败")
#     # print("下载成功")

