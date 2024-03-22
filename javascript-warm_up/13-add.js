#!/usr/bin/node

x = 0;

// add();

function add (a, b) {
//   const args = process.argv;

//   const a = parseInt(args[2]);
//   const b = parseInt(args[3]);
  x = (a + b);
  return (x);
}

exports.add = add;
