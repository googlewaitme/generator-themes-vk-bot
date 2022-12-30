import config
from peewee import *


database = SqliteDatabase(config.DATABASE_NAME)


class BaseModel(Model):
	class Meta:
		database = database


class User(BaseModel):
	user_id = IntegerField(unique=True)
	first_name = CharField()
	loggin_date = DateTimeField()
	registration_date = DateTimeField()


def create_tables():
	with database:
		database.create_tables([User])
