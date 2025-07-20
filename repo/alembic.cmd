(.venv) reza@Rezas-MacBook-Pro configuration % alembic init  alembic                    
Creating directory /Users/reza/Projects/GitHub/configuration/alembic ...  done
Creating directory /Users/reza/Projects/GitHub/configuration/alembic/versions ...  done
Generating /Users/reza/Projects/GitHub/configuration/alembic/script.py.mako ...  done
Generating /Users/reza/Projects/GitHub/configuration/alembic/env.py ...  done
Generating /Users/reza/Projects/GitHub/configuration/alembic/README ...  done
Generating /Users/reza/Projects/GitHub/configuration/alembic.ini ...  done
Please edit configuration/connection/logging settings in /Users/reza/Projects/GitHub/configuration/alembic.ini
before proceeding.


(.venv) reza@Rezas-MacBook-Pro configuration % alembic revision -m "create account table"
Generating /Users/reza/Projects/GitHub/configuration/alembic/versions/0e8d60b06dee_create_account_table.py ...  done


(.venv) reza@Rezas-MacBook-Pro configuration % alembic upgrade 0e8d60b06dee
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 0e8d60b06dee, create account table


(.venv) reza@Rezas-MacBook-Pro configuration % alembic revision -m "Add a column to account table"
  Generating
  /Users/reza/Projects/GitHub/configuration/alembic/versions/e8d730325d73_add_a_column_to_account_table.py ...  done


  (.venv) reza@Rezas-MacBook-Pro configuration % alembic current
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
0e8d60b06dee


(.venv) reza@Rezas-MacBook-Pro configuration % alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 0e8d60b06dee -> e8d730325d73, Add a column to account table


(.venv) reza@Rezas-MacBook-Pro configuration % alembic downgrade 0e8d60b06dee
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade e8d730325d73 -> 0e8d60b06dee, Add a column to account table

(.venv) reza@Rezas-MacBook-Pro configuration % alembic history --verbose
Rev: e8d730325d73 (head)
Parent: 0e8d60b06dee
Path: /Users/reza/Projects/GitHub/configuration/alembic/versions/e8d730325d73_add_a_column_to_account_table.py

    Add a column to account table
    
    Revision ID: e8d730325d73
    Revises: 0e8d60b06dee
    Create Date: 2025-07-19 20:22:31.047746

Rev: 0e8d60b06dee
Parent: <base>
Path: /Users/reza/Projects/GitHub/configuration/alembic/versions/0e8d60b06dee_create_account_table.py

    create account table
    
    Revision ID: 0e8d60b06dee
    Revises: 
    Create Date: 2025-07-19 20:13:08.644121