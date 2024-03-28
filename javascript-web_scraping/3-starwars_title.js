#!/usr/bin/node

const request = require('request');
const args = process.argv;

const StarWarsData = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request(StarWarsData, function (error, response, body) {
  const data = JSON.parse(body);

  console.log(data.title);
});
