## PANDA (FastAPI Based Project):

This project is my first python and fastapi program that consists of following technology stack:  
✓ Python  
✓ Docker  
✓ Docker Compose
✓ Postman  
✓ FastAPI  
✓ PostgreSQL  
✓ Pydantic  
✓ SQLAlchemy  
✓ Psycopg2    
✓ Alembic  
✓ Git  
✓ Nginx  

The final result of this project represents as following image (Swagger Style):

<img width="1044" height="2028" alt="Project Entire Image" src="https://github.com/user-attachments/assets/fb0b47b0-6bff-4771-b89c-5a117e716f08" />


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
