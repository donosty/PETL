import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
import logging

load_dotenv()

class DataLoader:
    
    def __init__(self):
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')
        
        encoded_user = quote_plus(db_user)
        encoded_password = quote_plus(db_password)
        
        self.db_url = f"postgresql+psycopg2://{encoded_user}:{encoded_password}@{db_host}:{db_port}/{db_name}"
        logging.info(f"Conectando a: postgresql+psycopg2://{encoded_user}:***@{db_host}:{db_port}/{db_name}")
        
        self.engine = create_engine(self.db_url)
        
        
    def cargar_datos(self, df, nombre_tabla):
        print(f"Iniciando carga de: {len(df)} registros a {nombre_tabla}...")
        
        try:
            df.to_sql(
                nombre_tabla,
                self.engine,
                if_exists='append',
                index=False,
                method='multi'
            )
            
            print("Carga a Base De Datos exitosa")
            
        except SQLAlchemyError as e:
            print(f"Error insertando datos en SQL: {e}")
            raise e