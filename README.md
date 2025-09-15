## FastAPI App:

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
✓ Pytest

### To run and setup this project, run the following commands in your terminal:

Clone the project into your path:

```bazaar
git clone https://gitlab.com/harasani-gitops/fastapi.git
```

Then, change directory in to project folder:

```bazaar
cd fastapi/
```

Finally, run `docker compose` command into related directory. Note that this project includes
two docker compose files. One for development environment, and the another one for production.
So, for testing this project in your local environment, you can the followng command:

```bazaar
docker compose -f docker-compose-dev.yml up -d
```

After runing this command, you can see our service on `http://127.0.0.1:8000` address. If you want
to see docs section, you can put `/docs` at the end of above address to see docs Swagger page.

**Notice**: Before doing anything, set the following variables, as you want to be on your server.
In below, we put some default values to know how to set appropriate values for these variables:

```bazaar
    POSTGRES_SERVER: str = postgres (required)
    POSTGRES_PORT: int = 5432
    POSTGRES_OUT_PORT: str
    POSTGRES_DB: str = fastapi (required)
    POSTGRES_USER: str = postgres
    POSTGRES_PASSWORD: str = password123 (required)

    SECRET_KEY: str (required)
    ALGORITHM: str = HS256 (required)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 (required)

    PROJECT_VERSION: str = 0.1.0-rc1
    ENVIRONMENT: str = Development
```

Variables that have `required` string in front of those, MUST set proper values. All above variables
are places into `.env` file. So, you shuld change them at this file, not anywhere else.
