from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, ARRAY

# 数据库类型
from sqlalchemy.orm import Session, declarative_base, relationship

# mymapper_registry = registry()
Base = declarative_base()


class Resource(Base):
    __tablename__ = "RESOURCE"
    uuid = Column(Integer, primary_key=True)
    name = Column(String(64))
    children_uuids = Column(ARRAY(String))


class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    uuids = Column(ARRAY(String))
    name = Column(ARRAY(String))
    fullname = Column(String)
    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
       return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(64), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"