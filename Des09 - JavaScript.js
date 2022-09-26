function Banco (conta, saldo, tipo, agencia) {
    this.conta = conta;
    this.saldo = saldo;
    this.tipo = tipo;
    this.agencia = agencia;

    this.buscarSaldo = function() {
        console.log("Saldo: R$ " + this.saldo);
    };

    this.deposito = function(valor) {
        var soma = Number(this.saldo) + Number(valor);
        this.saldo = soma; //o saldo recebe um valor novo que é o saldo anterior + o valor depositado
        console.log("Saldo pós depósito: R$ " + soma);
    };

    this.saque = function(valor) {
        var subtracao = Number(this.saldo) - Number(valor);
        this.saldo = subtracao; //o saldo recebe um valor novo que é o saldo anterior + o valor sacado
        console.log("Saldo pós saque: R$ " + subtracao);
    };

    this.numConta = function() {
        console.log("Número da conta: " + this.conta);
    };
}


//teste
var minhaConta = new Banco("12345-6", 35.00, "Corrente", "007");
minhaConta.buscarSaldo();
minhaConta.deposito(65);
minhaConta.saque(10);
minhaConta.numConta();
