#!/usr/bin/node

const args = process.argv;

let i = 0;
let str = ''

if (args.length < 3) {
  console.log('Missing size');
}

while (i < args[2]) {
  str = str + 'X';
  i++;
}

i = 0;

while (i < args[2]) {
  console.log(str);
  i++;
}
