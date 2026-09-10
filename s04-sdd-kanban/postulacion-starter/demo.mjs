import {readFileSync} from "node:fs";
import {analizarOferta} from "./analizar-oferta.mjs";
const entrada=JSON.parse(readFileSync(new URL("./fixtures.json",import.meta.url)));
console.log(JSON.stringify(analizarOferta(entrada),null,2));
