import os
import pandas as pd
import logging

class DataExtractor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        
    def leer_csvs(self):
        lista_dataframes_cargados = []
        
        if not os.path.exists(self.folder_path):
            logging.error(f"La Carpeta {self.folder_path} no existe")
            return []
        
        archivos_en_carpeta = os.listdir(self.folder_path)
        
        archivos_csv = [f for f in archivos_en_carpeta if f.endswith('.csv')]
        
        if not archivos_csv:
            logging.warning(f"No se encontraron archivos .csv en {self.folder_path}")
            return []
        
        for nombre_archivo in archivos_csv:
            ruta_completa = os.path.join(self.folder_path, nombre_archivo)
            
            try:
                df_temporal = pd.read_csv(ruta_completa)
                df_temporal['origen_archivo'] = nombre_archivo
                
                lista_dataframes_cargados.append(df_temporal)
                logging.info(f"Archivo cargado: {nombre_archivo} | Filas: {len(df_temporal)}")
                
            except Exception as e:
                logging.error(f"Error leyendo el archivo {nombre_archivo}: {e}")
            
        return lista_dataframes_cargados