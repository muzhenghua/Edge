from sqlalchemy import text

from fastapi_code.common.func import time_it, dict_value_list_to_list_value_dict
from fastapi_code.seting.config import SqlDataType, SqlCreate
from fastapi_code.common.db_session import database


class SqlStatement:

    @staticmethod
    @time_it
    def insert_sql(*args, **kwargs):
            """
            :param args:
            :param kwargs: 以字典的形式传入
            表名“table_name”
            数据“table_date”，eg:多行{"x":["1","2"]}，单行{"x":"1"},单行{"x":["1"]}
            :return:
            在示例中 提交更改 ，我们执行了一个INSERT语句，在该语句中我们似乎能够同时向数据库中插入多行。
            对于那些 对数据进行操作，但不返回结果集 ，
            即 DML 像“INSERT”这样的语句不包括“RETURNING”这样的短语，
            我们可以发送 多参数 到 Connection.execute() 方法，
            方法是传递字典列表而不是单个字典，从而允许针对每个参数集分别调用单个SQL语句：
            """
            table_name = kwargs.get("table_name")
            table_data = kwargs.get("table_date")
            if not table_data:
                raise ValueError(table_data)
            if not isinstance(table_data, dict):
                raise TypeError(table_data)
            col_list = table_data.keys()

            data_list = dict_value_list_to_list_value_dict(table_data)
            insert_table = f"INSERT INTO {table_name} ({', '.join(col_list)})" \
                           f" VALUES ({', '.join(list(':' + i for i in col_list))})"
            with database.get_engine().connect() as conn:
                conn.execute(text(insert_table), data_list)

    def merge_sql(self):
        pass

    def update_sql(self):
        pass

    def delete_sql(self):
        pass

    @staticmethod
    def create_sql(*args, **kwargs):
        """
        :param args:
        :param kwargs: 以字典的形式传入
            表名“table_name”
            数据“table_date”，eg:{字段名:字段类型}
        :return:
        """
        table_name = kwargs.get("table_name")
        table_date: dict = kwargs.get("table_date")
        if not isinstance(table_date, dict):
            raise TypeError(table_date)
        col_date_list = []
        for col, col_sql in table_date.items():
            if col_sql.split()[0] not in SqlDataType.__members__:
                raise ValueError(col_sql)
            col_date_list.append(col + " " + col_sql)

        create_table = f"CREATE TABLE {SqlCreate.IF_NOT_EXITS.value} {table_name} " \
                       f"({','.join(col_date_list)}) " \
                       f"{SqlCreate.ENGINE.value}" 
        with database.get_engine().connect() as conn:
            conn.execute(text(create_table))


a = ["s", "-ss"]
# print(":".join(a))
SqlStatement.insert_sql(table_name="mzx", table_date={"x": 1, "y": 2})
