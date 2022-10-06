import express from 'express';

const app = express();

app.get('/', function (request, response) {
    return response.send("Desenvolvimento do módulo 4 de JavaScript");
});

app.listen(8000);
