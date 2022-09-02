import sqlalchemy
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey

# 数据库类型
from sqlalchemy.orm import Session, registry, declarative_base, relationship

from fastapi_code.fastapi_db.model import Base

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

DB_URI = "{}+{}://{}:{}@{}:{}/{}"
charset = DB_URI.format(DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

print(charset)
# 创建数据库引擎

engine = create_engine(charset)


def insert_sql(engine):
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE IF NOT EXISTS some_table (x int, y int) "))
        # 写入数据
        conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [{"x": 1, "y": 1}, {"x": 2, "y": 4}])
        conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"), [{"x": 11, "y": 12}, {"x": 13, "y": 14}])
        # 更新数据
        update_sql = text("UPDATE some_table SET y=:y WHERE x=:x")
        update_date = [{"x": 11, "y": 11}, {"x": 13, "y": 13}]
        conn.execute(update_sql, update_date)
        print(type(engine))
    pass


def get_model():
    with engine.connect() as conn:
        # 执行基本的sql语法
        result = conn.execute(text("SELECT x, y FROM some_table"))
        for row in result:
            # sqlalchemy.engine.row.LegacyRow 对象，values 是一个元组，可以.column出对应的值
            print(type(row))
            print(dir(row))
            print(row.y)
            print(row)
        for row in result.mappings():
            # 转化为字典
            print(type(row))
            print(row)


def sql_model(metadata_obj):
    user_table = Table(
        "user_account",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("fullname", String(20))
    )
    print(user_table.c.keys())


def sql_model_update(metadata_obj):
    user_table = Table(
        "user_account",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30)),
        Column("fullname", String(20)),
        Column("fullname_copy", String(20))
    )
    print(user_table.c.keys())


def create_table_into_databse():
    global metadata_obj
    metadata_obj = MetaData()
    sql_model(metadata_obj)
    # create_all通过该对象传入数据库，创建表，如果不存在则创建，如果存在则不创建
    metadata_obj.create_all(engine)
    # drop_all 通过该对象传入数据库，删除表
    metadata_obj.drop_all(engine)


# create_table_into_databse()
metadata_obj = MetaData()
sql_model_update(metadata_obj)



# emit CREATE statements given ORM registry
mapper_registry.metadata.create_all(engine)

# the identical MetaData object is also present on the
# declarative base 继承base的表如果不存则创建
Base.metadata.create_all(engine)

# sandy = User(name="sandy", fullname="Sandy Cheeks")
# mapper_registry = registry()
# Base = mapper_registry.generate_base()
#
# class User(Base):
#     __table__ = user_table
#
#     addresses = relationship("Address", back_populates="user")
#
#     def __repr__(self):
#         return f"User({self.name!r}, {self.fullname!r})"
#
# class Address(Base):
#     __table__ = address_table
#
#     user = relationship("User", back_populates="addresses")
#
#     def __repr__(self):
#         return f"Address({self.email_address!r})"

print("sss")
# print(sandy.addresses)
