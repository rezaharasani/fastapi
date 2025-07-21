
@REM Docker Commands:
# docker run -d -p 5434:5432 -e POSTGRES_PASSWORD=secret --name postgres postgres
# ========================================================================================
# docker exec -it postgres createdb -U postgres fastapi
# ========================================================================================
# docker exec -it postgres psql -U postgres -d fastapi


@REM Docker Compose Commands
# docker compose -f docker-compose.yml up -d
[+] Running 2/2
 ✔ Network fastapi_metanet1  Created                                                                                     0.0s
 ✔ Container postgres        Started
# ========================================================================================
# docker compose ps
NAME       IMAGE             COMMAND                  SERVICE    CREATED          STATUS          PORTS
postgres   postgres:latest   "docker-entrypoint.s…"   postgres   41 seconds ago   Up 41 seconds   0.0.0.0:5434->5432/tcp, [::]:5434->5432/tcp
# ========================================================================================
# docker compose logs -f
postgres  | The files belonging to this database system will be owned by user "postgres".
postgres  | This user must also own the server process.
postgres  |
...
...
postgres  | 2025-07-20 18:06:41.605 UTC [1] LOG:  database system is ready to accept connections
# ========================================================================================
# docker compose down
[+] Running 2/2
 ✔ Container postgres        Removed                                                                                                   0.2s
 ✔ Network fastapi_metanet1  Removed