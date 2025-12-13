import pandas as pd
import numpy as np

from pandas.api.types import is_float_dtype, is_numeric_dtype, is_datetime64_any_dtype
from extract import ruta_archivos_sucios

lista_df = []

df_fechas = pd.DataFrame({
    "fecha":["2025/01/01", "2025/01/02", "2025/01/03", "NaN"]
})

for i in ruta_archivos_sucios:
    
    df = pd.read_csv(i)
    lista_df.append(df)

class DataTransformer:
    
    def __init__(self):
        pass
    
    
    def _normalizar_encabezados(self, df_list):
        
        encabezados_traducidos = ['id_venta', 'fecha', 'articulo', 'cantidad', 'precio', 'ubicacion']
        dfs_renombrados = []
        
        for df in df_list:
            df.columns = encabezados_traducidos  
            dfs_renombrados.append(df)
            
        return dfs_renombrados
    
    
    def _unificar_dataframe(self, df_list):
        
        df_concatenado = pd.concat(df_list, axis=0, ignore_index=True)
        return df_concatenado
    
    
    def _limpiar_fechas_y_manejar_nulos(self, df):
        
        df['fecha'] = pd.to_datetime(df["fecha"], format='mixed', errors='coerce')
            
        df_limpio = df.dropna(subset=['fecha'])
        return df_limpio
    
    
    def _limpiar_texto(str, df):
        
        df['articulo'] = df['articulo'].str.upper()
        df['ubicacion'] = df['ubicacion'].str.capitalize()
        
        return df
    
    
    def _manejar_nulos_y_tipos_numericos(self, df):
        
        cantidad_int = is_numeric_dtype(df['cantidad'])
        precio_float = is_float_dtype(df['precio'])
        
        if not cantidad_int or not precio_float:
            df['cantidad'] = df['cantidad'].astype(np.int64)
            df['precio'] = df['precio'].astype(np.float64)
            
        promedio_precios = df['precio'].mean()
        df = df.fillna({'precio':promedio_precios})
        
        return df
    
    
obj = DataTransformer()
dfs1 = obj._normalizar_encabezados(lista_df)
dfs2 = obj._unificar_dataframe(dfs1)
#print(dfs2.info())
dfs3 = obj._limpiar_fechas_y_manejar_nulos(df_fechas)
print(dfs2)

#dfs4 = obj._limpiar_texto(dfs2)
#print(dfs4)