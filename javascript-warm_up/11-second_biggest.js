#!/usr/bin/node

const args = process.argv;
let i = 0;
let biggest = 0;
let SecondBiggest = 0;

if (args.length < 2) {
  console.log('0');
}

while (args[i] != null) {
  if (parseInt(args[i]) > biggest) {
    SecondBiggest = biggest;
    biggest = parseInt(args[i]);
  } else if (parseInt(args[i]) > SecondBiggest) {
    SecondBiggest = parseInt(args[i]);
  }
  i++;
}

console.log(SecondBiggest);
