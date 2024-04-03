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

    for (let i = 0; i < data.length; i++) {
        let curID = data[i].userId;
        counter = 0; // Reset counter for each user ID

        // Check all subsequent items for the same user ID
        for (let j = i; j < data.length; j++) {
            if (data[j].userId === curID && data[j].completed === true) {
                counter++;
            } else if (data[j].userId !== curID) {
                // Break when encountering a different user ID
                break;
            }
        }

        listprint[curID] = counter;
        i += counter - 1; // Skip the processed items
    }

    console.log(listprint);
});
