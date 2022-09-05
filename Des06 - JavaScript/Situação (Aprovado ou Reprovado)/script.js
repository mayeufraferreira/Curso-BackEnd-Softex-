let n1 = document.getElementById('nota1');
let n2 = document.getElementById('nota2');
let n3 = document.getElementById('nota3');
let situacao = document.querySelector('span');

function calcularMedia() {
    let media = Number(n1.value) + Number(n2.value) + Number(n3.value);
    let resMedia = media/3;
    if (resMedia >= 7) {
        situacao.innerHTML = `Aluno(a) aprovado(a)!`;
    } else if (resMedia < 7) {
        situacao.innerHTML = `Aluno(a) reprovado(a)!`;
    }
}