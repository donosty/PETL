import pandas as pd
from extract import ruta_archivos_sucios

lista_df = []

for i in ruta_archivos_sucios:
    
    df = pd.read_csv(i)
    lista_df.append(df)

class DataTransformer:
    def __init__(self):
        pass
    
    def _normalizar_encabezados(self, df_list):
        
        encabezados_traducidos = ['id_venta', 'fecha', 'articulo', 'cantidad', 'precio', 'ubicacion']
        
        extraccion_df_columnas = df_list[0].columns
        encabezados_viejos = [e for e in extraccion_df_columnas]
        
        mapeo = dict(zip(encabezados_viejos, encabezados_traducidos))
    
        dfs_renombrados = []
        
        for df in df_list:
            
            df.rename(columns=mapeo)    
            dfs_renombrados.append(df)
            
        print(dfs_renombrados)
        return dfs_renombrados
    
    
    
obj = DataTransformer()
obj._normalizar_encabezados(lista_df)