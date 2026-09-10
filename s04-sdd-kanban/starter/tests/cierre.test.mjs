import test from 'node:test';
import assert from 'node:assert/strict';
import { evaluarCierre } from '../validar-cierre.mjs';

const aprobado = () => ({
  criterios: ['CA1', 'CA2'],
  evidencias: [
    { criterio: 'CA1', resultado: 'PASS', referencia: 'evidencias/prueba-1.txt' },
    { criterio: 'CA2', resultado: 'PASS', referencia: 'evidencias/prueba-2.txt' }
  ],
  revision: 'APROBADA',
  autorizacion: true
});
test('permite proponer Hecho con todos los criterios, revisión y autorización', () => {
  assert.equal(evaluarCierre(aprobado()).estado, 'Hecho');
});
test('deja en Revisión cuando falta un criterio', () => {
  const x=aprobado(); x.evidencias.pop();
  assert.equal(evaluarCierre(x).estado, 'Revisión');
});
test('rechaza una evidencia FAIL', () => {
  const x=aprobado(); x.evidencias[0].resultado='FAIL';
  assert.equal(evaluarCierre(x).estado, 'Revisión');
});
test('rechaza una referencia vacía', () => {
  const x=aprobado(); x.evidencias[0].referencia='  ';
  assert.equal(evaluarCierre(x).estado, 'Revisión');
});
test('espera autorización humana exacta', () => {
  const x=aprobado(); x.autorizacion=false;
  assert.equal(evaluarCierre(x).estado, 'Revisión');
});
test('no interpreta la cadena false como autorización', () => {
  const x=aprobado(); x.autorizacion='false';
  assert.equal(evaluarCierre(x).estado, 'Revisión');
});
test('exige revisión aprobada', () => {
  const x=aprobado(); x.revision='PENDIENTE';
  assert.equal(evaluarCierre(x).estado, 'Revisión');
});
test('una lista vacía no demuestra que todo se cumplió', () => {
  const x=aprobado(); x.criterios=[]; x.evidencias=[];
  assert.equal(evaluarCierre(x).estado, 'Revisión');
});
test('entradas inválidas producen razones sin romper el proceso', () => {
  for(const x of [null, {}, {criterios:'CA1'}, {criterios:[null],evidencias:[null]}]) {
    const r=evaluarCierre(x);
    assert.equal(r.estado, 'Revisión'); assert.ok(r.razones.length);
  }
});
test('criterios duplicados se rechazan', () => {
  const x=aprobado(); x.criterios=['CA1','CA1'];
  assert.equal(evaluarCierre(x).estado, 'Revisión');
});
test('evidencias contradictorias no se aceptan', () => {
  const x=aprobado(); x.evidencias.push({criterio:'CA1',resultado:'FAIL',referencia:'nuevo-fallo.txt'});
  assert.equal(evaluarCierre(x).estado, 'Revisión');
});
test('evaluar no altera la entrada', () => {
  const x=aprobado(), antes=structuredClone(x); evaluarCierre(x);
  assert.deepEqual(x,antes);
});
