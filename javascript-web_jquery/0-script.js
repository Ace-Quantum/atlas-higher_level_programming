#!/usr/bin/node

const { JSDOM } = require('jsdom')

const fs = require('fs')
const file = fs.readFileSync('./tester.html', 'utf-8');

const dom = new JSDOM(file);
const doc = dom.window.document;

const header = doc.querySelector("header");

function MakeItRed() {
    header.style.color = "#FF0000";
}

header.addEventListener("load", MakeItRed)
