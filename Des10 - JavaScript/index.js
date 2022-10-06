import express from 'express';

const app = express();

app.get('/', function (request, response) {
    return response.send("Desenvolvimento do módulo 4 de JavaScript");
});

app.get('/descricao', function (request, response) {
    return response.send("Aprendendo a criar rotas");
});

app.listen(8000);
