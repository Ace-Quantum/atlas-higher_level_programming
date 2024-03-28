#!/usr/bin/node

const request = require('request');
const args = process.argv;

const StarWarsData = 'https://swapi-api.hbtn.io/api/films/' + args[2];

request(StarWarsData, function (error, response, body) {
  if (error) console.log(error);
  const data = JSON.parse(body);

  console.log(data.title);
});
