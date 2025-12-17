# Retail ETL Pipeline

Un pipeline de Ingeniería de Datos automatizado construido en Python que ingesta, transforma y carga datos de ventas diarios en un Data Warehouse (PostgreSQL).

## Arquitectura
El proyecto sigue una arquitectura **ETL (Extract, Transform, Load)** orientada a objetos:

1.  **Extract:** Ingesta archivos CSV heterogéneos de múltiples fuentes (Norte, Sur, Este).
2.  **Transform (Pandas):**
    * Normalización de encabezados (Traducción EN -> ES).
    * Limpieza de fechas (Formatos mixtos).
    * Estandarización de texto y manejo de nulos.
    * Enriquecimiento de datos (Cálculo de totales).
3.  **Load (PostgreSQL):** Inserción eficiente en base de datos usando SQLAlchemy.

## Tecnologías
* **Python 3.12**
* **Pandas:** Manipulación de datos.
* **SQLAlchemy & Psycopg2:** Conexión a Base de Datos.
* **PostgreSQL:** Almacenamiento final.
* **Docker:** (Próximamente para containerización).

## ⚙️ Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/donosty/PETL.git](https://github.com/donosty/PETL.git)
    cd PETL
    ```

2.  **Configurar entorno virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Configurar Variables de Entorno:**
    Crea un archivo `.env` en la raíz con tus credenciales:
    ```ini
    DB_HOST=localhost
    DB_NAME=retail_db
    DB_USER=postgres
    DB_PASSWORD=tu_password
    DB_PORT=5432
    ```

4.  **Generar Datos de Prueba:**
    ```bash
    python generar_datos.py
    ```

5.  **Ejecutar Pipeline:**
    ```bash
    python main.py
    ```

## Estructura de la Base de Datos
La tabla `fact_ventas` incluye auditoría de ingestión y trazabilidad del archivo origen.

---
Hecho con 🐍 y ☕ por Donosty