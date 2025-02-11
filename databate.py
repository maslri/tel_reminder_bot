from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    DateTimeField,
    ForeignKeyField,
    BooleanField,
)

db = SqliteDatabase("db.sqlite3")


class baseModel(Model):
    class Meta:
        database = db


class User(baseModel):
    name = CharField()
    user_id = CharField(primary_key=True)

    class Meta:
        database = db


class Task(baseModel):
    user = ForeignKeyField(User, backref="task")
    title = CharField()
    description = CharField()
    datetime = DateTimeField()
    is_done = BooleanField(default=False)

    class Meta:
        database = db


db.connect()
db.create_tables([User, Task])
db.close()
