import config
from peewee import *
import datetime as dt


database = SqliteDatabase(config.DATABASE_NAME)


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    user_id = IntegerField(unique=True)
    first_name = CharField()
    loggin_date = DateTimeField()
    registration_date = DateTimeField()
    referal_code = CharField(null=True)
    referal_source = CharField(null=True)


class TokenOperation(BaseModel):
    user = ForeignKeyField(User, on_delete='cascade', backref="operations")
    created_at = DateTimeField(default=dt.datetime.now())
    token_count = IntegerField()
    request_purpose = CharField()
    request_message = TextField()


class MonetaryTransaction(BaseModel):
    user = ForeignKeyField(User, on_delete='cascade', backref="transactions")
    created_at = DateTimeField(default=dt.datetime.now())
    money_count = IntegerField()
    transaction_purpose = CharField()


class Subscription(BaseModel):
    user = ForeignKeyField(User, on_delete='cascade', backref='subscriptions')
    expired_at = DateTimeField()
    start_at = DateTimeField()
    subscription_method = CharField(null=True)  # buy or free
