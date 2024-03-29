#!/usr/bin/node

const request = require('request');
const args = process.argv;

const url = args[2];

request(url, function (error, response, body) {
    if (error) console.log(error);
    const data = JSON.parse(body);
    let counter = 0;
    let listprint = {};

    for (let i = 0; i < data.length; i++) {
        let curID = data[i].userId;
        console.log("typof data[i]: " + typeof(data[i]))
        console.log("curID : " + curID)
        console.log("data " + i + " : " + data[i])
        while (data[i].userId === curID || i < data.length) {
            if (data[i].completed === true) {
                counter++;
            }
            i++;
        }
        listprint[curID] = counter;
        curID = data[i].userId;
        counter = 0;
    }})


console.log('listprint: ' + listprint)
