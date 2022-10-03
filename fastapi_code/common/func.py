import time

from fastapi_code.common.db_session import database


def insert_database_by_dict(db_name: str, table_name: str, date: dict):
    """
    :param db_name: 数据库名称
    :param table_name: 表名
    :param date: 表数据
    :return: 插入数据成功、失败
    """
    with database.session() as session:
        session.query().filter()


def time_it(func):
    """
    :param func: 装饰器装饰函数
    :return: 打印出函数执行时间，方便调优
    """
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('用时:{}秒'.format(end-start))
    return inner


def dict_value_list_to_list_value_dict(data: dict) -> list:
    """
    :param data: {"x":[1, 2]} or {"x":1]}
    :return: [{"x":1},{"x":2}] or [{"x":1}]
    """
    date_list = []
    tmp_values = list(data.values())
    if isinstance(tmp_values[0], (str, int)):
        date_list.append(data)

    if isinstance(tmp_values[0], list):
        for i in range(len(tmp_values[0])):
            tmp_dict = {}
            for key, v in data.items():
                tmp_dict[key] = v[i]
            date_list.append(tmp_dict)

    return date_list
