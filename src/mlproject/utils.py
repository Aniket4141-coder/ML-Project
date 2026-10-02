import os
import sys
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from src.mlproject.logger import logging
from src.mlproject.exception import CustomException

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        # Build database connection URI
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")

        # Read table cleanly without warning
        df = pd.read_sql_query("SELECT * FROM students", con=engine)
        logging.info("SQL data read completed successfully")
        return df

    except Exception as e:
        raise CustomException(e, sys)