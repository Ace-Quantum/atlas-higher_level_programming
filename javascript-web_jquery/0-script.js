#!/usr/bin/node

const { JSDOM } = require('jsdom');

const dom = new JSDOM('<!DOCTYPE html><html><body></body></html>')
const document = dom.window.document

const header = document.querySelector("header")
header.addEventListener("load", MakeItRed)

function MakeItRed() {
    header.style.color = "#FF0000"
}

// Old code I no longer wish to see
// const { JSDOM } = require('jsdom')

// const fs = require('fs')
// const file = fs.readFileSync('./tester.html', 'utf-8');

// const dom = new JSDOM(file);
// const doc = dom.window.document;

// const header = doc.querySelector("header");

// function MakeItRed() {
//     header.style.color = "#FF0000";
// }

// dom.window.addEventListener("load", MakeItRed)
