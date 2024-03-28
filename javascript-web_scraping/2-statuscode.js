#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const request = require('request');

request(args[2], function(error, response) {
    console.error('error', error);
    console.log('code:' + response);
})
