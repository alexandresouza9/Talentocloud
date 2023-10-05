const numerosDaSorte = [37, 14, 26, 5, 94, 87];

const paresMenorQue50 = numerosDaSorte.filter(numero => numero % 2 === 0 && numero < 50);
const menorQue50 = numerosDaSorte.filter(numero => numero < 50);
const maiorQue50 = numerosDaSorte.filter(numero => numero > 50);

console.log('Números pares e menores que 50:', paresMenorQue50);
console.log('Números menores que 50:', menorQue50);
console.log('Números maiores que 50:', maiorQue50);