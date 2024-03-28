#!/usr/bin/node

const request = require('request');
const args = process.argv;

const StarWarsData = args[2];
let i = 0;

request(StarWarsData, function (error, response, body) {
  if (error) console.log(error);
  const data = JSON.parse(body);
  for (const key in data.results) {
    for (const secondkey in data.results[key].characters) {
      const tokens = (data.results[key].characters[secondkey].split('/'));
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
