from sqlalchemy import text

from fastapi_code.seting.config import SqlDataType, SqlCreate
from fastapi_code.common.db_session import database


class SqlStatement:

    @staticmethod
    def insert_sql(*args, **kwargs):
        table_name = kwargs.get("table_name")
        table_date = kwargs.get("table_date")
        if not isinstance(table_date, dict):
            raise TypeError(table_date)

        col_list = []
        col_date = [dict]
        print(col_date)
        col_list = table_date.keys()
        for col, col_date in table_date.items():
            col_list.append(":" + col)

        insert_table = f"INSERT INTO {table_name} () VALUE "

    @staticmethod
    def create_sql_command(*args, **kwargs):
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
        print(create_table)
        with database.get_engine().connect() as conn:
            conn.execute(text(create_table))


a = ["s", "-ss"]
print(":".join(a))
# SqlStatement.insert_sql(table_name="mzx", table_date={"x": 'INT'})
