from sqlalchemy import Table, MetaData, Column, Integer, String


metadata = MetaData()

UserTable = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String)
)
