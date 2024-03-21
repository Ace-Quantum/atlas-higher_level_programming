#!/usr/bin/node

const args = process.argv;

let a = parseInt(args[2]);
let b = parseInt(args[3]);

function add (a, b) {
  console.log(a + b);
}

add(a, b);
