"""Generación del resumen.txt a partir de los resultados reales de la ejecución."""
from datetime import datetime
from pathlib import Path


class GeneradorResumenTXT:
    """Recibe los resultados de las clases CSV y JSON y escribe un resumen .txt."""

    def __init__(self, url_csv, url_json):
        self.url_csv = url_csv
        self.url_json = url_json
        self.ruta_resumen = None

    def _seccion(self, titulo, url, resultados):
        lineas = [
            titulo,
            "-" * 60,
            f"URL de origen: {url}",
            f"Clase utilizada: {resultados['clase']}",
            f"Métodos utilizados: {', '.join(resultados['metodos_usados'])}",
            f"Archivo importado: {resultados['archivo_importado']}",
            f"Nuevo archivo guardado: {resultados['ruta_guardado']}",
            f"Registros importados: {resultados['registros_importados']}",
            f"Registros en el archivo guardado: {resultados['registros_finales']}",
            "Modificaciones realizadas:",
        ]
        lineas += [f"  - {m}" for m in resultados["modificaciones"]]
        return lineas

    def generar(self, resultados_csv, resultados_json, ruta_resumen):
        """Escribe el resumen y devuelve la ruta del archivo."""
        total = (
            resultados_csv["registros_importados"]
            + resultados_json["registros_importados"]
        )
        lineas = [
            "RESUMEN DE EJECUCIÓN - AE2",
            "=" * 60,
            f"Generado: {datetime.now():%Y-%m-%d %H:%M:%S}",
            "Clases: ManejadorCSV, ManejadorJSON, GeneradorResumenTXT",
            f"Registros procesados en total (importados): {total}",
            "",
            *self._seccion("ARCHIVO CSV", self.url_csv, resultados_csv),
            "",
            *self._seccion("ARCHIVO JSON", self.url_json, resultados_json),
            "",
        ]
        destino = Path(ruta_resumen)
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text("\n".join(lineas), encoding="utf-8")
        self.ruta_resumen = destino
        return destino

    def leer(self):
        """Devuelve el contenido del resumen generado."""
        return self.ruta_resumen.read_text(encoding="utf-8")
