from sqlalchemy import create_engine, select
from project.models import User
from project.database import UserTable


engine = create_engine('postgresql://postgres:yourpassword@localhost/postgres')

with engine.connect() as connection:
    result = connection.execute(select(UserTable))

    users = [User(**row) for row in result]

for user in users:
    print(user)
