import logging
import psycopg2
from psycopg2.extras import RealDictCursor

"""
Define logger code for printing logging output as a formatted and pretty style. 
"""
logger = logging.getLogger(__name__)
FORMAT = "[%(filename)s:%(lineno)s - %(asctime)s - %(levelname)s - %(funcName)10s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.INFO)

conn = psycopg2.connect(
    host="localhost",
    database="fastapi_test",
    user="postgres",
    port="5432",
    password="password123",
    cursor_factory=RealDictCursor,
)

logger.info(f"{__name__}: Retrieving table data connection was established!")
cursor = conn.cursor()
logger.info(f"{__name__}: {cursor}")
