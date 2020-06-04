from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import insert, select, update, delete, alias, bindparam, join

from schema_table import Users, Addresses

engine = create_engine('sqlite:///example.db', echo=True)
meta = MetaData(bind=engine)

def do_insert():
    ins = Users.insert().values(name='jack', fullname='Jack Jones')
    # ins = insert(Users, values=dict(name='jack', fullname='Jack Jones'))
    import ipdb, pdir; ipdb.set_trace()
    return ins

def do_select():
    sel = select([Users])
    # sel = select([Users.c.id, Users.c.fullname])
    return sel

def do_update():
    up = update(Users).where(Users.c.id == 1).values(fullname='Fire Pokemon')
    return up

    # params = [
    #     {'uid': 2, 'fullname': 'SQL Ninja'},
    #     {'uid': 3, 'fullname': 'Dr. Stone'},
    # ]
    # smt = (
    #     update(Users)
    #     .where(Users.c.id == bindparam('uid'))
    #     .values(fullname=bindparam('fullname'))
    # )
    # with engine.connect() as conn:
    #     conn.execute(smt, params)
    # return ''

def do_delete():
    dl = delete(Users).where(Users.c.id == 2)
    return dl

def insert_address():
    with engine.connect() as conn:
        engine.execute(Addresses.insert().values(user_id=1, email_address='foo@mail.com'))
        engine.execute(Addresses.insert().values(user_id=2, email_address='bar@mail.com'))

def do_join():
    j = join(left=Users, right=Addresses, onclause=Users.c.id == Addresses.c.user_id)
    smt = select([Users, Addresses.c.email_address]).select_from(j)
    return smt

if __name__ == "__main__":
    res = None
    # Note: this should typically is done with context manager.
    conn = engine.connect()

    # smt = do_insert()
    # smt = do_select()
    # smt = do_update()

    # insert_address()
    smt = do_join()

    res = conn.execute(smt)
    import ipdb, pdir; ipdb.set_trace()
