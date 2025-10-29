# Overview

This project is a small and easy `FastAPI` implementation that represents how can we program and deploy a python
project,
from start to end. It means, in this way, we used a few technologies and tools to develop and deploy our project.

In continue, we will explain about all used technologies and how can we use and run them for a production environments.
So, please follow up us.

## How to set up on lcoal environment

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
