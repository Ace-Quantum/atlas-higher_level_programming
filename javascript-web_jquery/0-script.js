#!/usr/bin/node

const doc = require('./tester.html')
const header = doc.querySelector("header");

header.addEventListener("load", doc)

function MakeItRed() {
    header.style.color = "#FF0000";
}
