from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine('sqlite:///example.db', echo=True)
# meta = MetaData(bind=engine)
Base = declarative_base()


class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)


class Addresses(Base):
    __tablename__ = 'Addresses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(Users.id, name='fk_user_id'))
    email_address = Column(String, nullable=False)


def define_schema():
    Base.metadata.create_all(engine)
    import ipdb, pdir; ipdb.set_trace()


if __name__ == "__main__":
    define_schema()
