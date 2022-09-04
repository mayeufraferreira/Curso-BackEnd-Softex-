let n1 = document.querySelector('#num1');
let n2 = document.querySelector('#num2');
let resultado = document.querySelector('span');

function somar() {
    resultado.innerHTML = Number(n1.value) + Number(n2.value);
}

function subtrair () {
    resultado.innerHTML = Number(n1.value) - Number(n2.value);
}

function multiplicar () {
    resultado.innerHTML = Number(n1.value) * Number(n2.value);
}

function dividir () {
    let divReal = Number(n1.value) / Number(n2.value);
    let resto = Number(n1.value) % Number(n2.value);
    resultado.innerHTML = `<br/> Divisão real: ${divReal} | Resto da divisão inteira: ${resto}`;
}