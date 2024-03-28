#!/usr/bin/node

// const fs = require('fs');
const args = process.argv;
const request = require('request');

request(args[2], response => {
    console.log('code:' + response);
})
