"""Manejo de archivos CSV: importar, modificar y guardar."""
import csv
import sys
from pathlib import Path

# Algunos CSV tienen campos de texto muy largos; se quita el límite por defecto.
csv.field_size_limit(sys.maxsize)


def _corto(valor, maximo=60):
    """Recorta textos largos para que el resumen sea legible."""
    texto = str(valor)
    return texto if len(texto) <= maximo else texto[:maximo] + "..."


class ManejadorCSV:
    """Importa un CSV con csv.reader, lo modifica y lo guarda con csv.writer."""

    def __init__(self, ruta_origen):
        self.ruta_origen = Path(ruta_origen)
        self.ruta_guardado = None
        self.encabezados = []
        self.filas = []
        self.registros_importados = 0
        self.modificaciones = []
        self.metodos_usados = []

    def importar(self):
        """Lee el CSV local. La primera fila son los encabezados."""
        with open(self.ruta_origen, newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            self.encabezados = next(lector)
            self.filas = list(lector)
        self.registros_importados = len(self.filas)
        self.metodos_usados.append("importar")
        return self.filas

    def actualizar_valor(self, indice_fila, columna, nuevo_valor):
        """Cambia el valor de una celda y registra el cambio."""
        posicion = self.encabezados.index(columna)
        valor_anterior = self.filas[indice_fila][posicion]
        self.filas[indice_fila][posicion] = str(nuevo_valor)
        self.modificaciones.append(
            f"Actualizado: fila {indice_fila}, columna '{columna}': "
            f"'{_corto(valor_anterior)}' -> '{_corto(nuevo_valor)}'"
        )
        self.metodos_usados.append("actualizar_valor")

    def agregar_registro(self, registro):
        """Agrega una fila nueva a partir de un diccionario {columna: valor}."""
        fila = [str(registro.get(columna, "")) for columna in self.encabezados]
        self.filas.append(fila)
        self.modificaciones.append(f"Agregado: registro nuevo {({k: _corto(v) for k, v in registro.items()})}")
        self.metodos_usados.append("agregar_registro")

    def eliminar_registro(self, indice_fila):
        """Elimina una fila por su posición."""
        eliminado = self.filas.pop(indice_fila)
        self.modificaciones.append(f"Eliminado: fila {indice_fila} {[_corto(c) for c in eliminado]}")
        self.metodos_usados.append("eliminar_registro")

    def guardar(self, ruta_destino):
        """Guarda un nuevo CSV con encabezados usando csv.writer."""
        destino = Path(ruta_destino)
        destino.parent.mkdir(parents=True, exist_ok=True)
        with open(destino, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.filas)
        self.ruta_guardado = destino
        self.metodos_usados.append("guardar")
        return destino

    def resultados(self):
        """Devuelve lo ocurrido en la ejecución, para el resumen."""
        return {
            "clase": "ManejadorCSV",
            "archivo_importado": str(self.ruta_origen),
            "ruta_guardado": str(self.ruta_guardado),
            "registros_importados": self.registros_importados,
            "registros_finales": len(self.filas),
            "modificaciones": list(self.modificaciones),
            "metodos_usados": list(self.metodos_usados),
        }
