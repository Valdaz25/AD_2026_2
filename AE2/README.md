# AE2: manejo de archivos CSV, JSON y TXT

Tres clases de Python coordinadas desde Jupyter: una importa, modifica y guarda un CSV, otra hace lo mismo con un JSON y la tercera genera un `resumen.txt` con los resultados reales de la ejecución.

## Estructura

```
AE2/
  manejador_csv.py             ManejadorCSV (csv.reader y csv.writer)
  manejador_json.py            ManejadorJSON (json.load y json.dump)
  generador_resumen_txt.py     GeneradorResumenTXT
  AE2_manejo_archivos.ipynb    Notebook que coordina el flujo
  datos_originales/            Archivos descargados de Hugging Face (sin modificar)
  datos_modificados/           Nuevo CSV y nuevo JSON con los cambios
  resumen.txt                  Resumen generado por la tercera clase
```

## Origen de los datos

Descargados manualmente de Hugging Face:

- CSV: https://huggingface.co/datasets/fka/prompts.chat/blob/main/prompts.csv
- JSON:https://huggingface.co/datasets/leonorv/slaying/blob/main/slaying.json

## Pasos de ejecución

1. Activar el entorno virtual: `source .venv/bin/activate`
2. Colocar los archivos descargados en `AE2/datos_originales/`.
3. Abrir `AE2/AE2_manejo_archivos.ipynb` y seleccionar el kernel `.venv`.
4. Ejecutar todas las celdas en orden.
5. Revisar `datos_modificados/` y `resumen.txt`.

## Modificaciones realizadas

- CSV: se actualiza un valor, se agrega un registro y se elimina otro.
- JSON: se actualiza un campo, se agrega un registro y se elimina otro.

Los originales no se tocan; los resultados se guardan con nombres nuevos.
