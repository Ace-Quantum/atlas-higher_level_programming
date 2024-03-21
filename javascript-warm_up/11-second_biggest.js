#!/usr/bin/node

const args = process.argv;
let i = 0;
let biggest = 0;
let second_biggest = 0;

if (args.length < 2) {
  console.log('0');
}

while (args[i] != null) {
  if (parseInt(args[i]) > biggest) {
    second_biggest = biggest;
    biggest = parseInt(args[i]);
  } else if (parseInt(args[i]) > second_biggest) {
    second_biggest = parseInt(args[i]);
  }
  i++;
}

console.log(second_biggest);
