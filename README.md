[![pipeline status](https://gitlab.com/harasani-gitops/fastapi/badges/main/pipeline.svg)](https://gitlab.com/harasani-gitops/fastapi/-/commits/main) 
[![coverage report](https://gitlab.com/harasani-gitops/fastapi/badges/main/coverage.svg)](https://gitlab.com/harasani-gitops/fastapi/-/commits/main) 
[![Latest Release](https://gitlab.com/harasani-gitops/fastapi/-/badges/release.svg)](https://gitlab.com/harasani-gitops/fastapi/-/releases) 



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


## How to setup on lcoal environment

In order to use, clone the project into your path:

```bazaar
git clone https://github.com/rezaharasani/fastapi.git /your/path/project/fastapi
```

Then, change into current cloned project directory path:

```bazaar
cd /your/path/project/fastapi
```

Run `docker compose` command into the `root` directory.
```shell
docker compose \
    -f composes/docker-compose.yml \
    -f composes/docker-compose-dev.yml \
    --env-file environments/.env.dev up -d
```

The above docker compose command runs the fastapi service and also postgresql database in `dev` environments. Therefore,
it helps you to continue your programming alongside real containerized infrastructure.

As you see, in the project, we divived composes into three seprate files, for each environment. These files can help 
developr to develop, test, and prepare for production environment.

 
However, you can use the following docker compose commands to run our services in specific environments:

🧪 for `Testing`:
```shell
docker compose \
    -f composes/docker-compose.yml \
    -f composes/docker-compose.test.yml \
    --env-file environments/.env.test \
    up --abort-on-container-exit
```

🚀 for `production`:
```shell
docker compose  \
    -f composes/docker-compose.yml \
    -f composes/docker-compose.prod.yml \
    --env-file environments/.env.prod up -d
```

**Note:** The above commands are usually used in set-up dockerized services in a simpler and smaller environments.
Therefore, for grater and real world deployments, we usually use kubernetes and some related tools and infrastructures
to deploy on production. That methods are more complicated and needs more resources and time to deploy. So, untill
now, we just explain an easy and fast deployment for small project. In continue, we will try to represent a real world
production environments and introduce more tools and complicated configs to deploy a kubernetes based deployment.


After runing the above command, you can see our service on `http://127.0.0.1:8000` url. If you want to see docs 
section, you can put `/docs` at the end of above address to see docs Swagger page.

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
