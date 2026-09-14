"""Soporte neutral: guarda JSON; no decide el contrato del dominio."""
import json
import re
import sqlite3
import uuid
from pathlib import Path


class Almacen:
    def __init__(self, directorio: Path):
        directorio.mkdir(parents=True, exist_ok=True)
        self.archivo = directorio / 'peticiones.sqlite3'
        with self._conexion() as db:
            db.execute('CREATE TABLE IF NOT EXISTS peticiones (id TEXT PRIMARY KEY, documento TEXT NOT NULL)')

    def _conexion(self):
        return sqlite3.connect(self.archivo)

    @staticmethod
    def _id(identificador):
        if not isinstance(identificador, str) or not re.fullmatch('[0-9a-f]{32}', identificador):
            raise ValueError('ID inválido')

    @staticmethod
    def _json(documento):
        texto = json.dumps(documento, ensure_ascii=False, allow_nan=False)
        texto.encode('utf-8')
        return texto

    def crear(self, entrada):
        identificador = uuid.uuid4().hex
        documento = {'id': identificador, 'entrada': entrada, 'status': 'pending', 'result': None, 'errors': []}
        with self._conexion() as db:
            db.execute('INSERT INTO peticiones VALUES (?, ?)', (identificador, self._json(documento)))
        return documento

    def leer(self, identificador):
        self._id(identificador)
        with self._conexion() as db:
            fila = db.execute('SELECT documento FROM peticiones WHERE id = ?', (identificador,)).fetchone()
        return json.loads(fila[0]) if fila else None

    def guardar_resultado(self, identificador, resultado, estado, errores):
        """El llamador valida el dominio ANTES; esto no comprueba fidelidad."""
        self._id(identificador)
        if estado not in ('ready', 'needs_input', 'error'):
            raise ValueError('Estado inválido')
        with self._conexion() as db:
            db.execute('BEGIN IMMEDIATE')
            fila = db.execute('SELECT documento FROM peticiones WHERE id = ?', (identificador,)).fetchone()
            if fila is None:
                raise KeyError(identificador)
            documento = json.loads(fila[0])
            documento.update(status=estado, errors=errores)
            if estado != 'error':
                documento['result'] = resultado
            db.execute('UPDATE peticiones SET documento = ? WHERE id = ?', (self._json(documento), identificador))
        return documento
