import pandas as pd
import numpy as np
import logging

class DataTransformer:
    
    def __init__(self):
        pass
    
    
    def _normalizar_encabezados(self, df_list):
        
        encabezados_sql = [
            'id_venta_original', 
            'fecha_venta', 
            'producto', 
            'cantidad', 
            'precio_unitario', 
            'sucursal',
            'origen_archivo'
        ]
        
        dfs_renombrados = []
        
        for df in df_list:
            df.columns = encabezados_sql  
            dfs_renombrados.append(df)
            
        return dfs_renombrados
    
    
    def _unificar_dataframe(self, df_list):
        
        df_concatenado = pd.concat(df_list, axis=0, ignore_index=True)
        return df_concatenado
    
    
    def _limpiar_fechas_y_manejar_nulos(self, df):
        
        df['fecha_venta'] = pd.to_datetime(df["fecha_venta"], format='mixed', errors='coerce')
            
        df_limpio = df.dropna(subset=['fecha_venta'])
        return df_limpio
    
    
    def _limpiar_texto(self, df):
        
        df['producto'] = df['producto'].str.upper()
        df['sucursal'] = df['sucursal'].str.capitalize()
        
        return df
    
    
    def _manejar_nulos_y_tipos_numericos(self, df):
        
        df['precio_unitario'] = pd.to_numeric(df['precio_unitario'], errors='coerce')
        df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce').fillna(0).astype(int)
        
        promedio_precios = df['precio_unitario'].mean()
        
        df['precio_unitario'] = df['precio_unitario'].fillna(promedio_precios)
        df['precio_unitario'] = df['precio_unitario'].round(2)
        
        return df
    
    
    def _enriquecer_datos(self, df):
        
        df['total_venta'] = df['cantidad'] * df['precio_unitario']
        
        return df
    
    
    def ejecutar_transformacion(self, lista_dfs_sucios):
        logging.info("Iniciando transformacion de los datos...")
        
        lista_norm = self._normalizar_encabezados(lista_dfs_sucios)
        
        df_sucio = self._unificar_dataframe(lista_norm)
        
        df_fechas = self._limpiar_fechas_y_manejar_nulos(df_sucio)
        
        df_texto = self._limpiar_texto(df_fechas)
        
        df_nulos = self._manejar_nulos_y_tipos_numericos(df_texto)
        
        df_final = self._enriquecer_datos(df_nulos)

        return df_final    
    
