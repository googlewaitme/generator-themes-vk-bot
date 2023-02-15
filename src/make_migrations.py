from peewee_migrate import Router
from peewee import SqliteDatabase


router = Router(SqliteDatabase('users.db'))

router.run()

