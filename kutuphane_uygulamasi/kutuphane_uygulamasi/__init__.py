"""import pymysql
pymysql.install_as_MySQLdb()"""
#import MySQLdb

from __future__ import absolute_import, unicode_literals

# Celery uygulaması import ediliyor
from .celery import app as celery_app

__all__ = ('celery_app',)

