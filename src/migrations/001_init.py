"""Peewee migrations -- 001_init.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['model_name']            # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.python(func, *args, **kwargs)        # Run python code
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.drop_index(model, *col_names)
    > migrator.add_not_null(model, *field_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)

"""

import datetime as dt
import peewee as pw
from peewee_migrate import Migrator
from decimal import ROUND_HALF_EVEN

try:
    import playhouse.postgres_ext as pw_pext
except ImportError:
    pass

SQL = pw.SQL


def migrate(migrator: Migrator, database, fake=False, **kwargs):
    """Write your migrations here."""
    @migrator.create_model
    class User(pw.Model):
        id = pw.AutoField()
        user_id = pw.IntegerField(unique=True)
        first_name = pw.CharField(max_length=255)
        loggin_date = pw.DateTimeField()
        registration_date = pw.DateTimeField()
        referal_code = pw.CharField(max_length=255, null=True)

        class Meta:
            table_name = "user"

    @migrator.create_model
    class MonetaryTransaction(pw.Model):
        id = pw.AutoField()
        user = pw.ForeignKeyField(column_name='user_id', field='id', model=migrator.orm['user'], on_delete='cascade')
        created_at = pw.DateTimeField(default=dt.datetime.now())
        money_count = pw.IntegerField()
        transaction_purpose = pw.CharField(max_length=255)

        class Meta:
            table_name = "monetarytransaction"

    @migrator.create_model
    class TokenOperation(pw.Model):
        id = pw.AutoField()
        user = pw.ForeignKeyField(column_name='user_id', field='id', model=migrator.orm['user'], on_delete='cascade')
        created_at = pw.DateTimeField(default=dt.datetime.now())
        token_count = pw.IntegerField()
        request_purpose = pw.CharField(max_length=255)
        request_message = pw.TextField()

        class Meta:
            table_name = "tokenoperation"



def rollback(migrator: Migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    migrator.remove_model('tokenoperation')

    migrator.remove_model('monetarytransaction')

    migrator.remove_model('user')

    migrator.remove_model('basemodel')
