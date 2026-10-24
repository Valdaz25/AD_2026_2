"""Manejo de archivos JSON: importar, modificar y guardar."""
import json
from pathlib import Path


def _corto(valor, maximo=60):
    """Recorta textos largos para que el resumen sea legible."""
    texto = str(valor)
    return texto if len(texto) <= maximo else texto[:maximo] + "..."


class ManejadorJSON:
    """Importa un JSON con json.load, lo modifica y lo guarda con json.dump.

    Trabaja con JSON cuya información está en una lista de objetos, ya sea en
    la raíz del archivo o dentro de una clave del objeto raíz.
    """

    def __init__(self, ruta_origen, clave_registros=None):
        self.ruta_origen = Path(ruta_origen)
        self.clave_registros = clave_registros
        self.ruta_guardado = None
        self.datos = None
        self.registros_importados = 0
        self.modificaciones = []
        self.metodos_usados = []

    def importar(self):
        """Lee el JSON local con json.load."""
        with open(self.ruta_origen, encoding="utf-8") as archivo:
            self.datos = json.load(archivo)
        self.registros_importados = len(self.registros)
        self.metodos_usados.append("importar")
        return self.datos

    @property
    def registros(self):
        """Lista de registros: la raíz si es lista, o la clave que contiene la lista."""
        if isinstance(self.datos, list):
            return self.datos
        if isinstance(self.datos, dict):
            if self.clave_registros is None:
                for clave, valor in self.datos.items():
                    if isinstance(valor, list):
                        self.clave_registros = clave
                        break
            if self.clave_registros is not None:
                return self.datos[self.clave_registros]
        raise ValueError(
            "No se encontró una lista de registros. Indica clave_registros al crear el objeto."
        )

    def actualizar_valor(self, indice, campo, nuevo_valor):
        """Cambia el valor de un campo en un registro y registra el cambio."""
        valor_anterior = self.registros[indice].get(campo)
        self.registros[indice][campo] = nuevo_valor
        self.modificaciones.append(
            f"Actualizado: registro {indice}, campo '{campo}': "
            f"'{_corto(valor_anterior)}' -> '{_corto(nuevo_valor)}'"
        )
        self.metodos_usados.append("actualizar_valor")

    def agregar_registro(self, registro):
        """Agrega un registro nuevo (diccionario)."""
        self.registros.append(registro)
        self.modificaciones.append(f"Agregado: registro nuevo {({k: _corto(v) for k, v in registro.items()})}")
        self.metodos_usados.append("agregar_registro")

    def eliminar_registro(self, indice):
        """Elimina un registro por su posición."""
        eliminado = self.registros.pop(indice)
        self.modificaciones.append(f"Eliminado: registro {indice}")
        self.metodos_usados.append("eliminar_registro")
        return eliminado

    def guardar(self, ruta_destino):
        """Guarda un nuevo JSON con json.dump."""
        destino = Path(ruta_destino)
        destino.parent.mkdir(parents=True, exist_ok=True)
        with open(destino, "w", encoding="utf-8") as archivo:
            json.dump(self.datos, archivo, ensure_ascii=False, indent=2)
        self.ruta_guardado = destino
        self.metodos_usados.append("guardar")
        return destino

    def resultados(self):
        """Devuelve lo ocurrido en la ejecución, para el resumen."""
        return {
            "clase": "ManejadorJSON",
            "archivo_importado": str(self.ruta_origen),
            "ruta_guardado": str(self.ruta_guardado),
            "registros_importados": self.registros_importados,
            "registros_finales": len(self.registros),
            "modificaciones": list(self.modificaciones),
            "metodos_usados": list(self.metodos_usados),
        }
