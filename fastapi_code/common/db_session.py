import threading
from datetime import datetime

from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import QueuePool
from sqlalchemy_utils import database_exists
from fastapi_code.seting.config import build_mysql_db_url, settings

SESSION = 'session'
local = threading.local()


class SessionWrapper:
    """
    __enter__ 打开这个类时自动调用
    __exit__  结束时调用
    getattr/setattr/delattr   检查/设置/删除当前线程是否存在
    """
    session_maker: sessionmaker

    initial: bool
    session: Session

    def __init__(self, session_maker: sessionmaker):
        self.session_maker = session_maker

    def __enter__(self) -> Session:
        self.session = getattr(local, SESSION, None)
        self.initial = self.session is None
        if self.initial:
            self.session = self.session_maker()
            setattr(local, SESSION, self.session)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # 如果推出时异常，则执行退出并清理session
            self.clean_local_data()
            self.rollback()
            raise
        try:
            # 退出时commit查询结果
            self.commit()
        except exc.SQLAlchemyError:
            # 如果commit失败，则回退
            self.rollback()
            raise
        finally:
            self.clean_local_data()

    def clean_local_data(self):
        if self.initial:
            delattr(local, SESSION)

    def rollback(self):
        if self.initial:
            self.session.rollback()

    def commit(self):
        if self.initial:
            self.session.commit()


class DatabaseMysql:
    _session_maker: sessionmaker

    def __init__(self):
        self.db_url = build_mysql_db_url()

        self._engine = create_engine(
            self.db_url,
            poolclass=QueuePool,
            # 是否输出sqlalchemy相关日志
            echo=settings.MYSQL_ECHO,
            # 线程数量
            pool_size=settings.MYSQL_POOL_SIZE
        )
        # database_exists会去连接一次数据库，
        # if not database_exists(self._engine.url):
        #     print("db error")

        self._session_maker = sessionmaker(autoflush=False)
        self._session_maker.configure(bind=self._engine)

    def session(self):
        return SessionWrapper(self._session_maker)

    def get_engine(self):
        return self._engine


database = DatabaseMysql()
__all__ = ['database']
