from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine('sqlite:///example.db', echo=True)
meta = MetaData(bind=engine)


Users = Table(
    'Users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
)


Addresses = Table(
    'Addresses', meta,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('Users.id', name='fk_user_id')),
    Column('email_address', String, nullable=False)
)


def define_schema():
    meta.create_all(engine)
    import ipdb, pdir; ipdb.set_trace()


if __name__ == "__main__":
    define_schema()
