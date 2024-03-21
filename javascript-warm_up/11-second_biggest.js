#!/usr/bin/node

const args = process.argv;
let i = 0;
let biggest = 0;
let Second_Biggest = 0;

if (args.length < 2) {
  console.log('0');
}

while (args[i] != null) {
  if (parseInt(args[i]) > biggest) {
    Second_Biggest = biggest;
    biggest = parseInt(args[i]);
  } else if (parseInt(args[i]) > Second_Biggest) {
    Second_Biggest = parseInt(args[i]);
  }
  i++;
}

console.log(Second_Biggest);
