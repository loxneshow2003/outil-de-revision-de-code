const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

let rules = [];

app.post('/add-rule', (req, res) => {
    const { check, comment } = req.body;
    rules.push({ check, comment });
    res.status(201).send('Règle ajoutée.');
});

app.post('/review', (req, res) => {
    const { code } = req.body;
    const comments = rules.map(rule => {
        return eval(rule.check + '(code)') ? '' : rule.comment;
    }).filter(comment => comment);
    res.json(comments);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Serveur en cours d\'exécution sur le port ${PORT}`);
});