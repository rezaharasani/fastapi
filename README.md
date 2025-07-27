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
✓ Jaeger  

The final result of this project represents as following image (Swagger Style):

<img width="1044" height="2028" alt="Project Entire Image" src="https://github.com/user-attachments/assets/fb0b47b0-6bff-4771-b89c-5a117e716f08" />

The following picture represents sample Jaeger output for root endpoint (/):

<img width="1540" height="823" alt="Screenshot 2025-07-27 at 22 47 31" src="https://github.com/user-attachments/assets/91433ea8-1811-4d9d-b33d-8c9eb21fe9ee" />



### Project structure:

```bazaar
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
│   │   ├── __pycache__
│   │   │   ├── auth.cpython-311.pyc
│   │   │   ├── post.cpython-311.pyc
│   │   │   ├── user.cpython-311.pyc
│   │   │   └── vote.cpython-311.pyc
│   │   ├── auth.py
│   │   ├── post.py
│   │   ├── user.py
│   │   └── vote.py
│   ├── schemas.py
│   └── utils.py
├── docker-compose-prod.yml
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
```

Before doing anything, set the following variables, as you want to be on your server. Some of them have default values,
so you can do not set them, if you accept the default values:

```bazaar
POSTGRES_SERVER: str = 'localhost'
POSTGRES_PORT: str = '5432'
POSTGRES_OUT_PORT: str = '5432'
POSTGRES_DB: str = 'postgres'
POSTGRES_USER: str = 'postgres'
POSTGRES_PASSWORD: str

SECRET_KEY: str
ALGORITHM: str
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

PROJECT_VERSION: str = 'Testing'

NGINX_PORT: str = '80'
```
