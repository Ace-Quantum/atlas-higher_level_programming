#!/usr/bin/node

let x = 0;

function add (a, b) {
  x = (a + b);
  return (x);
}

exports.add = add;
