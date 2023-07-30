import os
from enum import Enum

from sqlalchemy import types
from sqlalchemy.dialects.mysql import (TINYINT, SMALLINT, TINYTEXT, YEAR, SET, TINYBLOB,
                                       LONGBLOB, MEDIUMBLOB, LONGTEXT, MEDIUMTEXT)
from pydantic import AnyUrl, BaseSettings


def build_mysql_db_url():
    db_url = AnyUrl.build(
        scheme=MysqlDatabaseConfigEnum.DRIVER.value,
        user=MysqlDatabaseConfigEnum.USERNAME.value,
        password=MysqlDatabaseConfigEnum.PASSWORD.value,
        host=MysqlDatabaseConfigEnum.HOST.value,
        port=MysqlDatabaseConfigEnum.PORT.value,
        path="/" + MysqlDatabaseConfigEnum.DATABASE.value
        )
    return "mysql+"+db_url


class MysqlDatabaseConfigEnum(str, Enum):
    """
    数据库配置相关文件
    继承Enum只会执行一次
    """

    DIALCT = "mysql"

    # 数据库驱动
    DRIVER = "pymysql"

    # 数据库用户名
    USERNAME = "root"

    # 数据库密码
    PASSWORD = "123456"

    # 服务器IP地址
    HOST = "127.0.0.1"

    # 端口号，默认3306
    PORT = "3306"

    # 数据库名
    DATABASE = "python"


class Settings(BaseSettings):
    ENCODING: str = os.getenv("ENCODING", "utf-8")
    # 是否输出sql
    MYSQL_ECHO: bool = os.getenv("MYSQL_ECHO", "False").lower() == "true"
    MYSQL_POOL_SIZE: int = int(os.getenv("MYSQL_POOL_SIZE", "100"))


class SqlCreate(str, Enum):
    IF_NOT_EXITS = "IF NOT EXISTS"
    NOT_NULL = "NOT NULL"
    PRIMARY_KEY = "PRIMARY KEY"
    AUTO_INCREMENT = "AUTO_INCREMENT"
    DEFAULT = "DEFAULT"
    ENGINE = "ENGINE=MyISAM DEFAULT CHARSET=utf8"


class SqlDataType(str, Enum):
    INT = types.Integer
    BIGINT = types.BIGINT
    FLOAT = types.FLOAT
    # 字符串,会自动填充至10位，查找速度快,10是字符长度,char和varchar最长都是255
    CHAR = types.CHAR
    # 字符串自定义长度,节省空间，但是速度慢,定长的列往前放，变长的往后放，比如手机号用char,char和varchar最长都是255
    VARCHAR = types.VARCHAR
    # 日期 YYYY-MM-DD
    DATE = types.DATE
    # 时间 HH:MM:SS
    TIME = types.TIME
    # 时间 YYYY-MM-DD HH:MM:SS
    DATETIME = types.DATETIME
    # 时间戳，对应的数据库是否支持timezone
    TIMESTAMP = types.TIMESTAMP
    # 枚举值 ENUM('x-small','small','medium','large','x-large'),数值只能是其中一个
    ENUM = types.Enum
    # BLOB 最大65K (binary large object)二进制大对象，是一个可以存储二进制文件的容器。
    Blob = "Blob"
    # 2**16 - 1位
    TEXT = types.TEXT
    # 供应商特定类型 sqlalchemy.dialects
    # MySQL自己的类型
    # 年 1999
    YEAR = YEAR
    TINYINT = TINYINT
    SMALLINT = SMALLINT
    # SET('a', 'b', 'c', 'd'),数值只能是集合中数据的任意组合
    SET = SET
    # TinyBlob 最大255B
    TINYBLOB = TINYBLOB
    # MediumBlob 最大16M
    MEDIUMBLOB = MEDIUMBLOB
    # LongBlob 最大4G
    LONGBLOB = LONGBLOB
    # 2**32 - 1位
    LONGTEXT = LONGTEXT
    TINYTEXT = TINYTEXT
    # 2**24 - 1位
    MEDIUMTEXT = MEDIUMTEXT


settings = Settings()


__all__ = ["settings", "build_mysql_db_url", "SqlDataType", "SqlCreate"]
