# AD_2026_2

Repositorio del curso de Análisis de Datos. Contiene dos clases reutilizables en Python y un notebook que las coordina para cargar un dataset de Hugging Face, transformarlo y generar un resumen en `.txt`.

## Estructura

```
src/
  clases_po/
    hf_loader.py     HFDatasetLoader: descarga un dataset de Hugging Face y lo devuelve como DataFrame
    reportes.py      Reportes: genera y guarda un resumen de un DataFrame en .txt
  sincronicas/
    Semana_1SINC.ipynb          Notebook que ejecuta el flujo completo
    datos/                      CSV exportado por el cargador
    reportes/                   Resumen .txt generado
.github/workflows/              Ejecuta el notebook automáticamente en cada push a main
requirements.txt                Dependencias del proyecto
```

## Flujo del notebook

1. Se importan `HFDatasetLoader` y `Reportes` desde `src/clases_po`.
2. `HFDatasetLoader` descarga `JasonZhouTI/Fast_Food_Restaurants` (split `train`) y devuelve un DataFrame.
3. Transformación mínima: se seleccionan las columnas `name`, `city`, `province`, `latitude` y `longitude`, y el resultado se guarda en `df_t`.
4. `Reportes` recibe `df_t` y genera el resumen en `src/sincronicas/reportes/fast_food_restaurants.txt`.

El resumen incluye filas, columnas, duplicados, tipos de datos, valores nulos por columna y estadísticas numéricas.

## Uso

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Luego abre `src/sincronicas/Semana_1SINC.ipynb`, selecciona el kernel `.venv` y ejecuta todas las celdas en orden.

En Bash, el entorno virtual se activa con `source .venv/bin/activate`. No se ejecuta `.venv/bin/activate` directamente. Cuando está activo, el prompt muestra `(.venv)`.

## Clases

### HFDatasetLoader

```python
from clases_po import HFDatasetLoader

loader = HFDatasetLoader(
    dataset_name="JasonZhouTI/Fast_Food_Restaurants",
    split="train",
    filename="datos/fast_food_restaurants.csv",  # opcional: guarda el DataFrame
)
df = loader.load()
```

Parámetros principales: `dataset_name` (formato `usuario/dataset`), `split`, `config`, `max_rows`, `filename` y `file_type` (`csv`, `json`, `parquet` o `xlsx`).

### Reportes

```python
from clases_po import Reportes

reportes = Reportes()
reportes.imprimir_reporte(df_t)
reportes.guardar_reporte(df_t, "reportes/fast_food_restaurants.txt")
```

## Automatización

El workflow de `.github/workflows` ejecuta el notebook en cada push a `main` y sube al repositorio el notebook, los datos y el reporte regenerados. Antes de volver a hacer push, conviene ejecutar `git pull` para traer ese commit.