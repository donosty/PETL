import logging
import os
from src.extract import DataExtractor
from src.transform import DataTransformer
from src.load import DataLoader
from dotenv import load_dotenv

def setup_logging():
    os.makedirs('logs', exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/pipeline.log"),
            logging.StreamHandler()
        ]
    )


def run_pipeline():
    setup_logging()
    logging.info("Iniciando Pipeline ETL de Ventas")
    
    load_dotenv()
    
    try:
        logging.info("-- Paso 1: Extraccion --")
        path_datos = './data/raw'
        extractor = DataExtractor(path_datos)
        lista_dfs = extractor.leer_csvs()
        
        if not lista_dfs:
            logging.warning("No se encontraron archivos para procesar, Finalizando...")
            return
        logging.info(f"Se extrajeron {len(lista_dfs)} DataFrames exitosamente")
        
        
        logging.info("-- Paso 2: Transformacion --")
        transformer = DataTransformer()
        df_limpio = transformer.ejecutar_transformacion(lista_dfs)
        logging.info(f"Datos transformados. Total de filas a cargar: {len(df_limpio)}")
        
        
        logging.info("-- Paso 3: Carga (Load) --")
        loader = DataLoader()
        loader.cargar_datos(df_limpio, 'fact_ventas')
        logging.info("Pipeline finalizado con exito")
        
        
    except Exception as e:
        logging.error(f"Error critivo en el Pipeline: {e}", exc_info=True)
        


if __name__ == "__main__":
    run_pipeline()