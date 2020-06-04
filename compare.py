from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import insert, select, update, delete, alias, bindparam, join

from schema_table import Users, Addresses

engine = create_engine('sqlite:///example.db', echo=True)

def raw_sql():
    sql = '''
    SELECT Users.id, Users.name
    FROM Users
    '''
    return sql


def sql_alchemy():
    smt = select([Users])
    return smt


def downstream_query():
    smt = sql_alchemy().limit(1)
    return smt


if __name__ == "__main__":
    print(
        engine.execute(raw_sql())
        .fetchall()
    )
    # print(
    #     engine.execute(downstream_query())
    #     .fetchall()
    # )
