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
    console.log("before sort: " + data)
    data.sort(CompareUserID)
    console.log("after sort: " + data)

    for (let i = 0; i < data.length - 1; i++) {
        let curID = data[i].userId;
        while (data[i].userId === curID && i < data.length - 1) {
            if (data[i].completed === true) {
                counter++;
            }
            i++;
        }
        listprint[curID] = counter;
        counter = 0;
    }
    console.log(listprint)
})


