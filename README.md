## PANDA (FastAPI Based Project):

This project is my first python and fastapi program that consists of following technology stack:  
✓ Python  
✓ Docker  
✓ Postman  
✓ FastAPI  
✓ PostgreSQL  
✓ Pydantic  
✓ SQLAlchemy  
✓ Psycopg2  
✓ Unittest  
✓ Alembic  
✓ Git  
✓ Heroku  

The final result of this project represents as following image (Swagger Style):

<img width="1269" height="689" alt="Screenshot 2025-07-15 at 17 27 25" src="https://github.com/user-attachments/assets/557c655a-9661-4eb3-8df0-75921688cefa" />

### Project structure:  
```bazaar
reza@Rezas-MacBook-Pro fastapi % tree                                  
.
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── oauth2.py
│   ├── routers
│   │   ├── auth.py
│   │   ├── post.py
│   │   ├── user.py
│   │   └── vote.py
│   ├── schemas.py
│   └── utils.py
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 336f43959f4e_initial_migrations.py
│       └── ba92276cdf52_add_phone_number_column_to_users_table.py
├── nginx
│   └── app.conf
├── README.md
└── requirements.txt

6 directories, 24 files
```