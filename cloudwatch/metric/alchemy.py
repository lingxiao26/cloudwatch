#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from sqlalchemy import create_engine, MetaData, Table, Column
from sqlalchemy import Integer, String, ForeignKey


engine = create_engine('mysql+mysqldb://root@192.168.0.119/blog', echo=True)
md = MetaData(engine)


def create_table(metadata):
    user_table = Table('user', metadata,
                       Column('id', Integer, primary_key=True),
                       Column('name', String(50)),
                       Column('fullname', String(100))
                       )

    address_table = Table('address', metadata,
                          Column('id', Integer, primary_key=True),
                          Column('user_id', None, ForeignKey('user.id')),
                          Column('email', String(128), nullable=False)
                          )

    user_table.create(checkfirst=True)
    address_table.create(checkfirst=True)
    metadata.create_all()

user_table = Table('user', md, autoload=True)
print md.tables