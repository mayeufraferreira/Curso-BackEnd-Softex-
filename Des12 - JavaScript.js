import { Sequelize } from "sequelize";
const sequelize = new Sequelize ('teste', 'root', 'May!123456', {
    host: "localhost",
    dialect: "mysql"
});

sequelize.authenticate().then(function() {
    console.log("Conexão bem sucedida");
}).catch (function(erro){
    console.log("Conexão mal sucedida");
})
