from peewee import PostgresqlDatabase, Model, CharField

db = PostgresqlDatabase(
    "contact_book", user="admin2", password="password", host="localhost"
)


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()
