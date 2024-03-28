#!/usr/bin/node

const request = require('request');
const args = process.argv;

const StarWarsData = 'https://swapi-api.hbtn.io/api/people/18/';

request(StarWarsData, function (error, response, body) {
  if (error) console.log(error);
  const data = JSON.parse(body);

  console.log(data.films.length);
});