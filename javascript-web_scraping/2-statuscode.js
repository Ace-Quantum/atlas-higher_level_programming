#!/usr/bin/node

// const fs = require('fs');
const args = process.argv;
const request = require('request');

request(args[2], (error, response, body) => {
    if (error) console.log(error);
    console.log('code: ' + response.statusCode);
    // console.log(body);
})
