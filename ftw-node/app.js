const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
require('dotenv/config');

const app = express();

//Middlewares
app.use(bodyParser.json());

app.use('/initiateTransfer', (req,res) => {
    //res.send(req.body)
    request({
        method: 'POST',
        body: req.body,
        json: true,
        uri: 'https://api.flutterwave.com/v3/transfers',
        headers: {'Authorization': 'Bearer ' + process.env.secret_key}
      }, function (error, response, body){
        if(!error && response.statusCode == 200){
          res.send(body);
        } else {
            res.send(response.body);
        }
      })
});

app.use('/checkStatus', (req,res) => {
    request({
        method: 'GET',
        json: true,
        uri: 'https://api.flutterwave.com/v3/transfers/'+req.query.id,
        headers: {'Authorization': 'Bearer ' + process.env.secret_key}
      }, function (error, response, body){
        if(!error && response.statusCode == 200){
          res.send(body);
        } else {
            res.send(response.body);
        }
      })
});


  
// routes
app.get('/checkStatus', (req,res) => {
  
});

app.post('/initiateTransfer', (req,res) => {
    
});


// listen to server

app.listen(3000);