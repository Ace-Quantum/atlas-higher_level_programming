#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = args[2];
const listprint = {};
let counter = 0;

request(url, function (error, response, body) {
    if (error) console.log(error);
    const data = JSON.parse(body);

    for (let i = 0; data[i] != null; i++) {
        let curID = data[i].userId;
        console.log(data[i])
        while (data[i].userId === curID) {
            if (data[i].completed === true) {
                counter++;
            }
            i++;
        }
        listprint[curID] = counter;
        curID = data[i].userId;
        counter = 0;
    }})


console.log(listprint)
