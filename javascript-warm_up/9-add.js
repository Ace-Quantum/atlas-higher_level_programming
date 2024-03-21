#!/usr/bin/node

const args = process.argv;

a = parseInt(args[2]);
b = parseInt(args[3]);

function add(a, b) {
  console.log(a + b);
}

add(a, b);
