#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = args[2];
let counter = 0;
let listprint = {};

function CompareUserID(a, b) {
    return a.userId - b.userId;
}

request(url, function (error, response, body) {
    if (error) console.log(error);
    const data = JSON.parse(body);
    data.sort(CompareUserID)

    for (let i = 0; i < data.length - 1; i++) {
        let curID = data[i].userId;
        counter = 0;
        while (data[i].userId === curID && i < data.length - 1) {
            if (data[i].completed === true) {
                counter++;
            }
            i++;
        }
        listprint[curID] = counter;
    }
    console.log(listprint)
})


