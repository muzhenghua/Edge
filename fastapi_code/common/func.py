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
