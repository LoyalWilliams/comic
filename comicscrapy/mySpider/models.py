# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Comic(Base):
    __tablename__ = 'comic'

    id = Column(Integer, primary_key=True)
    comic_id = Column(Integer, nullable=False)
    author = Column(String(50))
    name = Column(String(50))
    intr = Column(String(500))
    last_short_title = Column(String(100))
    cover = Column(String(100), nullable=False)
    comic_url = Column(String(100))
    comic_type = Column(String(20))
    styles = Column(String(200))
    isDelete = Column(TINYINT(1), nullable=False, server_default=text("'0'"))


class ComicChapter(Base):
    __tablename__ = 'comic_chapter'

    id = Column(Integer, primary_key=True)
    comic_id = Column(Integer, nullable=False)
    chapter_id = Column(Integer, nullable=False)
    short_title = Column(String(100))
    urls = Column(String(1000))
    paths = Column(String(1000))
    title = Column(String(100))
    pub_time = Column(DateTime)
    isDelete = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
