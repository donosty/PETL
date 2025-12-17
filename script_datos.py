import pandas as pd
import numpy as np
import os

os.makedirs('datos_ventas', exist_ok=True)

data_norte = {
    'id_venta': [101, 102, 103, 104, 105],
    'fecha': ['15/01/2024', '16/01/2024', '17/01/2024', '18/01/2024', '19/01/2024'],
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Laptop'],
    'cantidad': [1, 5, 2, 1, 1],
    'precio_unitario': [1200.00, 20.00, 45.00, 300.00, 1200.00],
    'sucursal': ['Norte', 'norte', 'NORTE', 'Norte', 'Norte']
}
df_norte = pd.DataFrame(data_norte)
df_norte.to_csv('datos_ventas/ventas_norte.csv', index=False)
print("Generado: datos_ventas/ventas_norte.csv")


data_sur = {
    'sale_id': [201, 202, 203, 204],
    'date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18'],
    'item': ['Impresora', 'Laptop', 'Tablet', 'Mouse'],
    'qty': [1, 2, 5, 10],
    'price': [250.50, 1100.00, 300.00, 18.50],
    'branch': ['Sur', 'Sur', 'Sur', 'Sur']
}
df_sur = pd.DataFrame(data_sur)
df_sur.to_csv('datos_ventas/ventas_sur.csv', index=False)
print("Generado: datos_ventas/ventas_sur.csv")


data_este = {
    'id_venta': [301, 302, 303, 304, 305],
    'fecha': ['15-01-2024', np.nan, '17/01/2024', 'error_fecha', '19/01/2024'], 
    'producto': ['Disco Duro', 'Webcam', 'Microfono', 'Cable HDMI', 'Monitor'],
    'cantidad': [2, 1, 1, 10, 2],
    'precio_unitario': [80.00, np.nan, 120.00, 15.00, np.nan], 
    'sucursal': ['Este', 'Este', 'Este', 'Este', 'Este']
}
df_este = pd.DataFrame(data_este)
df_este.to_csv('datos_ventas/ventas_este.csv', index=False)
print("Generado: datos_ventas/ventas_este.csv")
