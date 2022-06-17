import mysql
import mysql.connector as mysql
import config
import datetime
import sys
from mysite_django.constants import *

class DBHelper:
    def __init__(self) -> None:
        self.__user = DB_USER