#!/usr/bin/node

const args = process.argv;
let i = 0;
let biggest = 0;
let second_biggest = 0;

if (args.length < 2) {
  console.log('0');
}

while (args[i] != null) {
  if (args[i] > biggest) {
    second_biggest = biggest;
    biggest = args[i];
  }
  i++;
}

console.log(second_biggest);
