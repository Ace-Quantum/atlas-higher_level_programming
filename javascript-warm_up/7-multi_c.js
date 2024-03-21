#!/usr/bin/node

const args = process.argv;

let i = 0;

if (args.length < 3) {
  console.log('Missing number of occurrences');
} else {
  while (i < args[2]) {
    console.log('C is fun');
    i++;
  }
}
