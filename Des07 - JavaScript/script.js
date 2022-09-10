var nome = prompt("Vamos calcular! Qual é o seu nome?");
const agradecimento = (nome) => `Olá ${nome}! Muito obrigado por usar essa calculadora!`;
alert(agradecimento(nome));

function inserir (num) {
    var numero = document.getElementById('resultado').innerHTML;
    document.getElementById('resultado').innerHTML = numero + num;
}

function limpar () {
    document.getElementById('resultado').innerHTML = "";
}

function calcular() {
    var resultado = document.getElementById('resultado').innerHTML;
    document.getElementById('resultado').innerHTML = eval(resultado);
}