#!/usr/bin/node
const args = process.argv;

let i = 0;

while (args[i] != null) {
    i++;
}

if (i === 2) {
  console.log('No argument');
} else {
  i = 0;
  while(args[i] != null) {
  console.log(args[i]);
    i++;
  }
}
