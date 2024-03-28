#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const args = process.argv;

const url = args[2];
const FilePath = args[3];

request(url, function (error, response, body) {
  if (error) console.log(error);
  fs.writeFile(FilePath, body, (err) => {
    if (err) throw err;
  });
});
