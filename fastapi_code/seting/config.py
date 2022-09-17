import os
from enum import Enum

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
    MYSQL_ECHO: bool = os.getenv("MYSQL_ECHO", "False").lower() == "true"
    MYSQL_POOL_SIZE: int = int(os.getenv("MYSQL_POOL_SIZE", "100"))


settings = Settings()


__all__ = ["settings", "build_mysql_db_url"]
