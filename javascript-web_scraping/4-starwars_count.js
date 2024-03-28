#!/usr/bin/node

const { title } = require('process');
const request = require('request');
const args = process.argv;

const StarWarsData = args[2];
let i = 0;

// console.log(StarWarsData)

request(StarWarsData, function (error, response, body) {
  if (error) console.log(error);
  const data = JSON.parse(body);
  for (const key in data.results) {
    // console.log('hello?')
    // console.log(data.results[key])
    for (const secondkey in data.results[key].characters) {
      // console.log('howdy')
      tokens = (data.results[key].characters[secondkey].split('/'));
      if (tokens[5] === '18') {
        i++;
      }
    }
  }
  console.log(i);
});

// console.log(data.title);
// for (title in data){
//   console.log(data.title)
// }
//   for (let obj in data) {
//     obj = data.characters
//     for (const num in obj){
//         console.log(obj.num);
//     }
//   }
