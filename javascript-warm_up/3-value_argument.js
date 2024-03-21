#!/usr/bin/node
const args = process.argv;

let i = 0;

while (args[i] != null) {
  i++;
}

if (i === 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
