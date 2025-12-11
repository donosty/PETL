import os
import pandas as pd

ruta_data = '/home/donosty/Escritorio/PETL/data/raw/datos_ventas'
        
ruta_archivos_sucios = [os.path.join(ruta_data, nombre_fichero) for nombre_fichero in os.listdir(ruta_data)]