const cores = ['amarelo', 'azul', 'branco'];

function listarCores() {
    for (const e of cores) {
        console.log(e);
    }
}

listarCores();
console.log();

var celular = {
    marca:'motorola', 
    tela:'6.5"', 
    RAM:'4GB'
};

function listarCelular() {
    for (const propriedade in celular) {
        console.log(`${propriedade}: ${celular[propriedade]}`);
    }
}

listarCelular();