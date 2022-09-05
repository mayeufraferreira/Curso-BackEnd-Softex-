let n1 = document.getElementById('nota1');
let n2 = document.getElementById('nota2');
let n3 = document.querySelector('span');

function calcular() {
    let c = (Number(n1.value) + Number(n2.value));
    if (c == 20) {
        n3.innerHTML = '<br/>1';
    } else if (c == 19) {
        n3.innerHTML = '<br/>2';
    } else if (c == 18) {
        n3.innerHTML = '<br/>3';
    } else if (c == 17) {
        n3.innerHTML = '<br/>4';
    } else if (c == 16) {
        n3.innerHTML = '<br/>5';
    } else if (c == 15) {
        n3.innerHTML = '<br/>6';
    } else if (c == 14) {
        n3.innerHTML = '<br/>7';
    } else if (c == 13) {
        n3.innerHTML = '<br/>8';
    } else if (c == 12) {
        n3.innerHTML = '<br/>9';
    } else if (c == 11) {
        n3.innerHTML = '<br/>10';
    } else if (c <= 10) {
        n3.innerHTML = '<br/>Não há como conseguir nota suficiente para ser aprovado ainda nesse semestre.';
    } 
}
