const express = require('express');
const path = require('path');
const request = require('request');
const _ = require('underscore');

const app = express();
app.use('/public', express.static('public'));


app.get('/', (req, res) => {
	request.get({
		uri: 'http://localhost:3000/public/data/data.json'
	}, (error, response, body) => {
		if (error) return console.log('Error:', error);

		const data = JSON.parse(body);

		res.send(data);
	});
});



app.listen(3000);
console.log('Express server started on port 3000');
