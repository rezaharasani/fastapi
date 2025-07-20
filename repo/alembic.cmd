# alembic init  migrations
#
# alembic revision --autogenerate -m "initial migrations"
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'users'
INFO  [alembic.autogenerate.compare] Detected added table 'posts'
INFO  [alembic.autogenerate.compare] Detected added table 'votes'
  Generating /Users/reza/Projects/GitHub/fastapi/migrations/versions/336f43959f4e_initial_migrations.py ...  done
#
#
# alembic upgrade head (or revision id, e.g. alembic upgrade 336f43959f4e)
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 336f43959f4e, initial migrations
#
#
# alembic current
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
336f43959f4e (head)#
#
#
# alembic history
<base> -> 336f43959f4e (head), initial migrations
#
#
# alembic history --verbose
Rev: 336f43959f4e (head)
Parent: <base>
Path: /Users/reza/Projects/GitHub/fastapi/migrations/versions/336f43959f4e_initial_migrations.py

    initial migrations

    Revision ID: 336f43959f4e
    Revises:
    Create Date: 2025-07-20 17:21:19.577850
#
#
# alembic revision -m "add a column to account table"
#
# alembic downgrade 0e8d60b06dee
#