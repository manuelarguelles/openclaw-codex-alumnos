"""Ejemplo didáctico de adaptar validación; no es una aplicación resuelta."""

def validar(entrada, salida):
    if salida.get('send_allowed') is not False:
        return ['No se autorizan compras']
    if entrada.get('umbral') is None:
        return [] if salida.get('status') == 'needs_input' and salida.get('preguntas') and not salida.get('propuestas') else ['Falta umbral: pedirlo sin proponer cantidades']
    hechos = {h['id']: h for h in entrada['hechos']}
    for propuesta in salida.get('propuestas', []):
        hecho = hechos.get(propuesta.get('evidence_id'))
        if hecho is None:
            return ['Evidencia desconocida']
        esperado = max(0, entrada['umbral'] - hecho['unidades'])
        if propuesta.get('reponer') != esperado:
            return ['Cantidad no respaldada por el hecho y umbral']
    return [] if salida.get('status') == 'draft' and salida.get('propuestas') else ['Falta propuesta revisable']
