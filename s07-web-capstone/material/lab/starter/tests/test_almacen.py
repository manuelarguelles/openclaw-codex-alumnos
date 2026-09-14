import pytest
from almacen import Almacen


def test_reinicio_y_error_conservan_entrada_y_resultado_anterior(tmp_path):
    almacen = Almacen(tmp_path)
    registro = almacen.crear({'hechos': [{'id': 'S1', 'unidades': 3}]})
    identificador = registro['id']
    almacen.guardar_resultado(identificador, {'reponer': 2}, 'ready', [])
    recuperado = Almacen(tmp_path)
    recuperado.guardar_resultado(identificador, None, 'error', ['Evidencia desconocida'])
    actual = recuperado.leer(identificador)
    assert actual['entrada'] == registro['entrada']
    assert actual['result'] == {'reponer': 2}
    assert actual['status'] == 'error'
    recuperado.guardar_resultado(identificador, {'reponer': 1}, 'ready', [])
    assert Almacen(tmp_path).leer(identificador)['result'] == {'reponer': 1}


def test_ruta_no_es_id_y_json_no_finito_no_se_guarda(tmp_path):
    almacen = Almacen(tmp_path)
    with pytest.raises(ValueError):
        almacen.leer('../../fuera')
    with pytest.raises(ValueError):
        almacen.crear({'numero': float('inf')})
    assert not (tmp_path.parent / 'fuera').exists()
