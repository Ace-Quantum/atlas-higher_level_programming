#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = args[2];
const listprint = {};
let counter = 0;

request(url, function (error, response, body) {
    if (error) console.log(error);
    const data = JSON.parse(body);
    for (let key of data) {
        let curID = key.userId;
        while (key.userId === curID) {
            if (key.completed === true) {
                counter++;
            }
            key++;
            console.log('key: ' + key.user)
        }
        listprint[curID] = counter;
        curID = key.userId;
        counter = 0;
    }
    console.log(listprint)
})
